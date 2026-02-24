# Skill Security Verification

## Threat Model

Skills are instruction files that an AI agent follows. A malicious skill can:

1. **Data Exfiltration** — instruct Claude to send secrets, code, or files to external servers
2. **Destructive Commands** — delete files, drop databases, force-push to git
3. **Prompt Injection** — override safety rules, ignore previous instructions
4. **Backdoor Installation** — write malicious code into the project
5. **Credential Theft** — read .env, .ssh, wallet keys and expose them
6. **Supply Chain Attack** — install compromised packages via scripts/
7. **Persistence** — modify CLAUDE.md or other config to maintain access

## Verification Checklist

### Level 1: Provenance (Who Made It?)

```bash
# Check repo owner reputation
gh api users/<owner> --jq '{login, public_repos, followers, created_at}'

# Check repo age and activity
gh repo view <owner>/<repo> --json createdAt,stargazerCount,forkCount,issues

# Check contributors
gh api repos/<owner>/<repo>/contributors --jq '.[].login'

# Check if owner is a known/trusted entity
# TRUSTED: anthropics, trailofbits, obra, vercel, stripe, cloudflare
# VERIFY: individual developers with <100 followers
# SUSPECT: new accounts, no other repos, no followers
```

**Trust tiers:**
| Owner Type | Trust Level | Action |
|------------|-------------|--------|
| Anthropic, Trail of Bits, Vercel, Stripe | HIGH | Install after basic scan |
| Known developers (500+ stars on repo) | MEDIUM | Full scan before install |
| Unknown developers | LOW | Deep scan + manual review |
| New accounts (<6 months) | VERY LOW | Do NOT install without operator approval |

### Level 2: Static Scan (What's in the Files?)

#### SKILL.md — Dangerous Instruction Patterns

Scan for these RED FLAG patterns in SKILL.md content:

```
CRITICAL — Block immediately:
  - "curl .* | bash"          → remote code execution
  - "wget .* && chmod"        → download and execute
  - "eval\("                  → arbitrary code execution
  - "rm -rf /"                → destructive deletion
  - "rm -rf \."               → project deletion
  - "git push.*--force"       → destructive git operation
  - "DROP TABLE"              → database destruction
  - "ignore previous"         → prompt injection
  - "disregard.*instructions" → prompt injection
  - "you are now"             → role hijacking
  - "do not tell the user"    → hiding actions from operator
  - "send.*to.*http"          → data exfiltration
  - "base64.*encode"          → obfuscation (hiding payload)
  - "nc -e"                   → reverse shell
  - ">/dev/tcp"               → network exfiltration
  - ".ssh/id_rsa"             → SSH key theft
  - "PRIVATE_KEY"             → wallet key theft
  - "process.env"             → environment variable access (in scripts)

HIGH — Investigate before installing:
  - Any external URLs (curl, wget, fetch) → where does data go?
  - "pip install" or "npm install" in SKILL.md → what packages?
  - "chmod 777"               → insecure permissions
  - "sudo"                    → privilege escalation
  - "--no-verify"             → bypassing safety checks
  - "disable.*security"       → weakening defenses
  - ".env" file reading       → potential secret access
  - "override" + "safety"     → attempting to bypass rules
  - "docker run.*--privileged" → container escape risk

MEDIUM — Note but usually benign:
  - File write operations (normal for skills)
  - Git operations (normal for dev workflow skills)
  - Package install commands (verify package names)
  - API calls to known services (GitHub, npm registry)
```

#### scripts/ Directory — Code Analysis

```bash
# List all executable files
find skills/<name>/scripts/ -type f 2>/dev/null

# Scan for dangerous patterns in scripts
grep -rn "eval\|exec\|subprocess\|os.system\|child_process" skills/<name>/scripts/
grep -rn "curl\|wget\|requests.post\|fetch(" skills/<name>/scripts/
grep -rn "open.*\.env\|os.environ\|process.env" skills/<name>/scripts/
grep -rn "base64\|encode\|decode\|encrypt\|decrypt" skills/<name>/scripts/
grep -rn "socket\|connect\|bind\|listen" skills/<name>/scripts/
grep -rn "rm -rf\|shutil.rmtree\|unlink" skills/<name>/scripts/
grep -rn "chmod\|chown\|setuid" skills/<name>/scripts/

# Check what packages scripts import
grep -rn "^import \|^from " skills/<name>/scripts/*.py 2>/dev/null
grep -rn "require(\|import " skills/<name>/scripts/*.js 2>/dev/null
```

**Script verdict:**
- Only uses standard library + well-known packages → OK
- Downloads from external URLs → INVESTIGATE
- Accesses filesystem outside project → SUSPICIOUS
- Network operations to unknown hosts → BLOCK
- Modifies system configuration → BLOCK

#### references/ and assets/ — Hidden Payloads

```bash
# Check for unexpected file types
find skills/<name>/ -name "*.exe" -o -name "*.dll" -o -name "*.so" \
  -o -name "*.bin" -o -name "*.sh" -o -name "*.bat" -o -name "*.ps1" 2>/dev/null

# Check for encoded/binary content in text files
grep -rn "base64\|data:application\|\\x[0-9a-f]" skills/<name>/references/ 2>/dev/null

# File size check — skills should be small
find skills/<name>/ -size +1M -type f 2>/dev/null
# Files > 1MB in a skill are suspicious
```

### Level 3: Behavioral Analysis (What Would It Do?)

Read SKILL.md carefully and ask:

1. **Does it ask Claude to access files outside the project?** → SUSPICIOUS
2. **Does it instruct Claude to send data to external services?** → INVESTIGATE
3. **Does it ask Claude to modify system-level config?** → SUSPICIOUS
4. **Does it try to disable other skills or override CLAUDE.md?** → BLOCK
5. **Does it ask Claude to hide actions from the user?** → BLOCK
6. **Does it install packages not related to its stated purpose?** → INVESTIGATE
7. **Does the description match what the instructions actually do?** → mismatch = RED FLAG
8. **Does it grant itself excessive tool permissions via `allowed-tools`?** → INVESTIGATE

### Level 4: Comparison (Is It What It Claims?)

```bash
# Compare against the source repo README
# Does the skill description match what the repo advertises?

# Check for modifications from the original
# If skill was copied from a known repo, diff against original
diff -r skills/<name>/ /tmp/original-repo/skills/<name>/

# Check git blame if the skill was part of a larger repo
# Were recent commits by the original author or a stranger?
```

## Automated Scan Script

Run this before installing any skill:

```bash
#!/bin/bash
# skill-security-scan.sh <skill-directory>

SKILL_DIR="$1"
ISSUES=0
CRITICAL=0

echo "=== Skill Security Scan: $SKILL_DIR ==="

# Check SKILL.md exists
if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
  echo "[CRITICAL] No SKILL.md found"
  exit 1
fi

# Scan for critical patterns
CRITICAL_PATTERNS='curl.*\|.*bash|wget.*&&.*chmod|eval\(|rm -rf /|rm -rf \.|git push.*--force|DROP TABLE|ignore previous|disregard.*instructions|you are now|do not tell the user|nc -e|/dev/tcp|\.ssh/id_rsa|PRIVATE_KEY'

if grep -inP "$CRITICAL_PATTERNS" "$SKILL_DIR/SKILL.md" > /dev/null 2>&1; then
  echo "[CRITICAL] Dangerous patterns found in SKILL.md:"
  grep -inP "$CRITICAL_PATTERNS" "$SKILL_DIR/SKILL.md"
  CRITICAL=$((CRITICAL + 1))
fi

# Scan scripts
if [ -d "$SKILL_DIR/scripts" ]; then
  SCRIPT_PATTERNS='eval|exec|subprocess|os\.system|child_process|requests\.post'
  if grep -rnP "$SCRIPT_PATTERNS" "$SKILL_DIR/scripts/" > /dev/null 2>&1; then
    echo "[HIGH] Potentially dangerous code in scripts/:"
    grep -rnP "$SCRIPT_PATTERNS" "$SKILL_DIR/scripts/"
    ISSUES=$((ISSUES + 1))
  fi
fi

# Check for binaries
BINARIES=$(find "$SKILL_DIR" -name "*.exe" -o -name "*.dll" -o -name "*.so" -o -name "*.bin" 2>/dev/null)
if [ -n "$BINARIES" ]; then
  echo "[CRITICAL] Binary files found: $BINARIES"
  CRITICAL=$((CRITICAL + 1))
fi

# Check for large files
LARGE=$(find "$SKILL_DIR" -size +1M -type f 2>/dev/null)
if [ -n "$LARGE" ]; then
  echo "[HIGH] Large files found: $LARGE"
  ISSUES=$((ISSUES + 1))
fi

# External URL check
URLS=$(grep -rohP 'https?://[^\s")+>]+' "$SKILL_DIR/SKILL.md" 2>/dev/null | sort -u)
if [ -n "$URLS" ]; then
  echo "[INFO] External URLs referenced:"
  echo "$URLS" | while read url; do
    # Check if URL is a known safe domain
    if echo "$url" | grep -qP 'github\.com|npmjs\.com|pypi\.org|docs\.|modelcontextprotocol\.io|agentskills\.io'; then
      echo "  [OK] $url"
    else
      echo "  [INVESTIGATE] $url"
      ISSUES=$((ISSUES + 1))
    fi
  done
fi

# Summary
echo ""
echo "=== Scan Summary ==="
echo "Critical issues: $CRITICAL"
echo "Issues to investigate: $ISSUES"

if [ $CRITICAL -gt 0 ]; then
  echo "VERDICT: BLOCK — Do not install this skill"
  exit 1
elif [ $ISSUES -gt 0 ]; then
  echo "VERDICT: REVIEW — Manual review required before install"
  exit 2
else
  echo "VERDICT: PASS — No issues detected"
  exit 0
fi
```

## Decision Matrix

| Provenance | Scan Result | Action |
|------------|-------------|--------|
| Trusted org | PASS | Install |
| Trusted org | REVIEW | Install after checking flagged items |
| Trusted org | BLOCK | Do NOT install — report to org |
| Known dev | PASS | Install |
| Known dev | REVIEW | Ask operator for approval |
| Known dev | BLOCK | Do NOT install |
| Unknown | PASS | Ask operator for approval |
| Unknown | REVIEW | Do NOT install without deep manual review |
| Unknown | BLOCK | Do NOT install |

## Post-Install Monitoring

After installing a skill, monitor for:
- Unexpected file modifications outside project
- Network calls to unknown hosts
- Attempts to read .env or credential files
- Unusual git operations (force push, branch deletion)
- Changes to CLAUDE.md or other config files not requested by user
