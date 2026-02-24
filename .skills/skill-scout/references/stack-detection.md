# Stack Detection Patterns

## Language Detection

| File / Pattern | Language |
|----------------|----------|
| `package.json` | JavaScript/TypeScript |
| `tsconfig.json` | TypeScript |
| `requirements.txt`, `pyproject.toml`, `Pipfile` | Python |
| `Cargo.toml` | Rust |
| `go.mod` | Go |
| `Gemfile` | Ruby |
| `composer.json` | PHP |
| `mix.exs` | Elixir |
| `build.gradle`, `pom.xml` | Java/Kotlin |
| `*.csproj`, `*.sln` | C#/.NET |
| `*.swift`, `Package.swift` | Swift |

## Framework Detection

### JavaScript/TypeScript
| File / Dependency | Framework |
|-------------------|-----------|
| `next.config.*` | Next.js |
| `nuxt.config.*` | Nuxt.js |
| `vite.config.*` | Vite |
| `angular.json` | Angular |
| `svelte.config.*` | SvelteKit |
| `astro.config.*` | Astro |
| `remix.config.*` | Remix |
| `gatsby-config.*` | Gatsby |
| dep: `express` | Express.js |
| dep: `fastify` | Fastify |
| dep: `hono` | Hono |
| dep: `elysia` | Elysia (Bun) |

### Python
| File / Dependency | Framework |
|-------------------|-----------|
| dep: `fastapi` | FastAPI |
| dep: `django` | Django |
| dep: `flask` | Flask |
| dep: `starlette` | Starlette |
| dep: `tornado` | Tornado |
| dep: `celery` | Celery (task queue) |
| `manage.py` | Django |
| `alembic.ini` | Alembic (DB migrations) |

### Infra
| File / Pattern | Technology |
|----------------|------------|
| `Dockerfile*` | Docker |
| `docker-compose*` | Docker Compose |
| `.github/workflows/*` | GitHub Actions CI/CD |
| `.gitlab-ci.yml` | GitLab CI |
| `Jenkinsfile` | Jenkins |
| `terraform/`, `*.tf` | Terraform |
| `k8s/`, `helm/` | Kubernetes |
| `ansible/` | Ansible |

### Crypto/Blockchain
| File / Pattern | Technology |
|----------------|------------|
| `*.sol` | Solidity (smart contracts) |
| `hardhat.config.*` | Hardhat |
| `foundry.toml` | Foundry |
| `truffle-config.*` | Truffle |
| dep: `web3`, `web3.py` | Web3 |
| dep: `ethers` | Ethers.js |
| dep: `viem` | Viem |
| dep: `wagmi` | Wagmi (wallet connect) |

### Testing
| File / Dependency | Test Framework |
|-------------------|----------------|
| dep: `jest` | Jest |
| dep: `vitest` | Vitest |
| dep: `mocha` | Mocha |
| dep: `playwright` | Playwright |
| dep: `cypress` | Cypress |
| dep: `pytest` | Pytest |
| dep: `unittest` | Python unittest |
| `*.test.*`, `*.spec.*` files | Tests exist |
| `__tests__/` directory | Tests exist |
| `tests/` directory | Tests exist |

### Database
| File / Dependency | Database |
|-------------------|----------|
| dep: `pg`, `asyncpg` | PostgreSQL |
| dep: `mysql2` | MySQL |
| dep: `mongodb`, `pymongo` | MongoDB |
| dep: `redis`, `ioredis` | Redis |
| dep: `prisma` | Prisma ORM |
| dep: `drizzle-orm` | Drizzle ORM |
| dep: `sqlalchemy` | SQLAlchemy |
| dep: `sequelize` | Sequelize |
| `prisma/schema.prisma` | Prisma |
| `drizzle/` | Drizzle |

## Skill Category Mapping

Based on detected stack, recommend these categories:

```
ALWAYS recommend:
  → verification-before-completion
  → systematic-debugging

IF has_any_code:
  → brainstorming, writing-plans, executing-plans

IF python:
  → tob-modern-python

IF fastapi OR django OR flask:
  → sec-input-validation, sec-auth-security, sec-rate-limiting
  → tob-entry-point-analyzer

IF nextjs OR react OR vue:
  → frontend-design, sec-headers
  → page-cro, seo-audit (if marketing site)

IF docker:
  → tob-insecure-defaults
  → container security skills

IF solidity OR hardhat OR web3:
  → tob-secure-contracts (CRITICAL)

IF has_api:
  → tob-entry-point-analyzer, sec-rate-limiting, sec-auth-security

IF has_tests:
  → test-driven-development, tob-property-testing

IF no_tests:
  → test-driven-development (HIGH PRIORITY), webapp-testing

IF has_env_files:
  → secret guard / varlock skills

IF has_ci_cd:
  → tob-differential-review, sec-dependency-security

IF marketing_or_saas:
  → page-cro, copywriting, pricing-strategy, launch-strategy
  → seo-audit, schema-markup, content-strategy, programmatic-seo

IF mcp_server:
  → mcp-builder

IF has_auth:
  → sec-auth-security, vibesec

IF has_payments:
  → payment security, input validation (CRITICAL)
```
