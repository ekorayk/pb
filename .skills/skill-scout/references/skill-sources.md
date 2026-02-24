# Skill Sources Database

## Tier 1 — High Quality, Verified

### Anthropic Official
- **Repo:** https://github.com/anthropics/skills
- **License:** Apache 2.0 (examples), Proprietary (document skills)
- **Skills:** mcp-builder, webapp-testing, frontend-design, skill-creator, pdf, xlsx, docx, pptx, algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, internal-comms, slack-gif-creator, theme-factory, web-artifacts-builder
- **Quality:** Highest — reference implementation of the Agent Skills spec
- **Install:** `git clone --depth 1 https://github.com/anthropics/skills.git` → `skills/` dir

### Trail of Bits Security
- **Repo:** https://github.com/trailofbits/skills
- **License:** Creative Commons
- **Plugins (23):**
  - `building-secure-contracts` — 11 sub-skills: Algorand, Cairo, Cosmos, Solana, Substrate, TON vulnerability scanners + audit prep, code maturity, guidelines, workflow, token integration
  - `audit-context-building` — line-by-line code audit, mental model building
  - `static-analysis` — CodeQL, Semgrep integration
  - `variant-analysis` — find similar vulnerability patterns
  - `semgrep-rule-creator` — custom Semgrep rules
  - `semgrep-rule-variant-creator` — Semgrep rule variants
  - `entry-point-analyzer` — state-changing entry points, attack surface
  - `insecure-defaults` — insecure default configurations
  - `differential-review` — security-focused git diff review
  - `fix-review` — detect bugs introduced by fix commits
  - `sharp-edges` — footgun designs, dangerous patterns
  - `constant-time-analysis` — timing side-channel detection
  - `spec-to-code-compliance` — code vs specification audit
  - `property-based-testing` — security property-based tests
  - `yara-authoring` — YARA rules for threat detection
  - `burpsuite-project-parser` — Burp Suite file parsing
  - `firebase-apk-scanner` — Firebase config in APKs
  - `dwarf-expert` — DWARF debugging format
  - `modern-python` — Python security patterns
  - `testing-handbook-skills` — ToB testing handbook
  - `culture-index` — security culture assessment
- **Quality:** Highest — world-class security firm
- **Install:** `git clone --depth 1 https://github.com/trailofbits/skills.git` → `plugins/` dir

### obra/superpowers (Dev Workflow)
- **Repo:** https://github.com/obra/superpowers | https://github.com/obra/superpowers-marketplace
- **License:** Open source
- **Skills:** brainstorming, writing-plans, executing-plans, test-driven-development, systematic-debugging, verification-before-completion, + others
- **Quality:** High — battle-tested methodology, spec-driven development
- **Install:** `git clone --depth 1 https://github.com/obra/superpowers-marketplace.git` → `skills/` dir

### coreyhaines31/marketingskills (Marketing & SEO)
- **Repo:** https://github.com/coreyhaines31/marketingskills
- **Website:** https://www.marketing-skills.com/
- **License:** Open source
- **Skills:** page-cro, pricing-strategy, programmatic-seo, copywriting, content-strategy, launch-strategy, seo-audit, schema-markup, ab-test-setup, analytics-tracking, competitor-alternatives, copy-editing, email-sequence, form-cro, free-tool-strategy, marketing-ideas, marketing-psychology, onboarding-cro, paid-ads, paywall-upgrade-cro, popup-cro, product-marketing-context, referral-program, signup-flow-cro, social-content
- **Quality:** High — built by marketing professional, used in 200+ projects
- **Install:** `git clone --depth 1 https://github.com/coreyhaines31/marketingskills.git` → `skills/` dir

### harperaa/secure-claude-skills (OWASP)
- **Repo:** https://github.com/harperaa/secure-claude-skills
- **License:** Open source
- **Skills:** input-validation, auth-security, security-headers, rate-limiting, dependency-security, security-testing, csrf-protection, error-handling, payment-security + security awareness sub-skills
- **Quality:** High — comprehensive OWASP Top 10 coverage, Next.js optimized
- **Install:** `git clone --depth 1 https://github.com/harperaa/secure-claude-skills.git`

## Tier 2 — Good Quality, Specialized

### BehiSecc/VibeSec-Skill
- **Repo:** https://github.com/BehiSecc/VibeSec-Skill
- **Skills:** vibesec (single skill — bug hunter perspective)
- **Quality:** Medium-High — attacker mindset, catches SQLi/XSS/prompt injection

### fr33d3m0n/skill-threat-modeling
- **Repo:** https://github.com/fr33d3m0n/skill-threat-modeling
- **Skills:** threat-modeling (8-phase STRIDE workflow)
- **Quality:** High — professional-grade STRIDE → CWE → CAPEC → ATT&CK chain

### TheCraigHewitt/seomachine
- **Repo:** https://github.com/TheCraigHewitt/seomachine
- **Website:** https://www.seomachine.io/
- **Skills:** Full SEO workspace — /research, /write, /optimize, /analyze-existing
- **Quality:** High — integrates GA4, GSC, DataForSEO, WordPress publishing

### huifer/claude-code-seo
- **Repo:** https://github.com/huifer/claude-code-seo
- **Skills:** Next.js SEO assistant — 100-point audit, 6 dimensions, 27+ commands
- **Quality:** Medium-High — Next.js specific

### davila7/claude-code-templates
- **Repo:** https://github.com/davila7/claude-code-templates
- **Skills:** 600+ agents, 200+ commands, marketing-strategy-pmm, content-creator
- **Quality:** Medium — massive collection, individual quality varies

### alirezarezvani/claude-skills
- **Repo:** https://github.com/alirezarezvani/claude-skills
- **Skills:** Modular packages + factory toolkit for generating skills at scale
- **Quality:** Medium — good for bulk skill generation

### wrsmith108/varlock-claude-skill
- **Repo:** https://github.com/wrsmith108/varlock-claude-skill
- **Skills:** Secure environment variable management
- **Quality:** Medium-High — addresses real Claude Code .env leak issue

### wrsmith108/claude-skill-security-auditor
- **Repo:** https://github.com/wrsmith108/claude-skill-security-auditor
- **Skills:** npm dependency audit with CVE extraction
- **Quality:** High — structured npm audit parsing

## Tier 3 — Discovery & Aggregation

### Awesome Lists (Curated Directories)
| List | URL | Stars | Focus |
|------|-----|-------|-------|
| awesome-claude-code | https://github.com/hesreallyhim/awesome-claude-code | 23K+ | Most comprehensive |
| awesome-agent-skills | https://github.com/VoltAgent/awesome-agent-skills | High | 200+ curated official skills |
| awesome-claude-skills | https://github.com/travisvn/awesome-claude-skills | High | Actively maintained |
| awesome-claude-skills | https://github.com/BehiSecc/awesome-claude-skills | 4K+ | Security focus |
| awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills | Medium | General |
| antigravity-awesome-skills | https://github.com/sickn33/antigravity-awesome-skills | Medium | 713+ skills, role bundles |

### Web Marketplaces
| Platform | URL | Scale |
|----------|-----|-------|
| SkillsMP | https://skillsmp.com | 70K+ indexed skills |
| SkillHub | https://skillhub.club | 7K+ AI-evaluated |
| claude-plugins.dev | https://claude-plugins.dev | Community registry |
| mcpservers.org | https://mcpservers.org/claude-skills | Categorized catalog |
| awesomeclaude.ai | https://awesomeclaude.ai | Visual directory |
| skills.sh | https://skills.sh | Individual skill pages |

### GitHub Search Patterns
```bash
# Find skills by domain
gh search repos "claude skills <domain>" --sort stars --limit 10
gh search repos "agent skills <domain>" --sort stars --limit 10
gh search repos "SKILL.md <keyword>" --sort stars --limit 5

# Find skills by framework
gh search repos "claude code <framework> skill" --sort stars --limit 10
```

## Agent Skills Specification
- **Standard:** https://agentskills.io/specification
- **Spec Repo:** https://github.com/agentskills/agentskills
- **Compatibility:** Claude Code, OpenAI Codex CLI, Gemini CLI, GitHub Copilot, Cursor, Antigravity, VS Code
