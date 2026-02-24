---
name: shared-miniconda-project-env
description: Configure and enforce a shared Miniconda installation with per-project isolated Conda environments, package caches, and pip caches stored inside the project folder. Use when asked to set up Python/Conda on Windows, create a project-specific env from a shared Miniconda path, keep all downloads and install artifacts inside project root, or generate copy-paste instructions for IDE AI assistants.
---

<!-- TR-INFO:
EN Name: shared-miniconda-project-env
TR Ad: Paylasimli Miniconda Proje Ortami
EN Description: Configure and enforce a shared Miniconda installation with per-project isolated Conda environments, package caches, and pip caches stored inside the project folder. Use when asked to set up Python/Conda on Windows, create a project-specific env from a shared Miniconda path, keep all downloads and install artifacts inside project root, or generate copy-paste instructions for IDE AI assistants.
TR Aciklama: Paylasimli Miniconda uzerinden proje-ozel conda ortami ve cache yapisini proje klasoru icinde tutarak standart kurulum saglar.
-->

# Shared Miniconda Project Env

## Overview

Enforce one shared Miniconda install while isolating every project into its own local env and caches.
Prevent package installs, downloads, and build artifacts from leaking outside project root.

## Inputs

Collect these values before running commands:
1. `miniconda_root` (example: `D:\tools\miniconda3`)
2. `project_root` (absolute path to current project)
3. `env_name` (example: `radx`, `api`, `ml`)
4. `python_version` (default: `3.11`)

## Miniconda Path Selection Rule

1. If `miniconda_root` is not explicitly provided, stop and ask the user before any setup step:
- `Hangi Miniconda yolunu kullanmami istersin?`
2. If helpful, show candidate paths and ask user to choose:
- current shell command: ``(Get-Command conda -ErrorAction SilentlyContinue).Path``
- common locations: `C:\miniconda3`, `C:\Users\<user>\miniconda3`, `D:\tools\miniconda3`, `F:\code\miniconda`
3. Do not guess a Miniconda path and continue silently.
4. Continue only after user confirms the exact root path (folder that contains `Scripts\conda.exe`).

## Hard Rules

1. Never install dependencies into Conda `base`.
2. Never run global `pip install` without project env context.
3. Always keep Conda envs under `<project_root>\.conda\envs`.
4. Always keep Conda package cache under `<project_root>\.conda\pkgs`.
5. Always keep pip cache under `<project_root>\.pip-cache`.
6. Always set `CONDARC` to `<project_root>\.condarc` before Conda operations.
7. Always confirm `miniconda_root` with user if it is missing or ambiguous.

## Standard Workflow (Windows PowerShell)

1. Run the setup script:

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\shared-miniconda-project-env\scripts\setup-project-conda.ps1 `
  -ProjectRoot "<PROJECT_ROOT>" `
  -MinicondaRoot "<MINICONDA_ROOT>" `
  -EnvName "<ENV_NAME>" `
  -PythonVersion "3.11"
```

2. Use the env for commands:

```powershell
& "<MINICONDA_ROOT>\Scripts\conda.exe" run -p "<PROJECT_ROOT>\.conda\envs\<ENV_NAME>" python --version
& "<MINICONDA_ROOT>\Scripts\conda.exe" run -p "<PROJECT_ROOT>\.conda\envs\<ENV_NAME>" python -m pip install <package>
```

## Manual Fallback (If Script Cannot Run)

```powershell
$projectRoot = "<PROJECT_ROOT>"
$minicondaRoot = "<MINICONDA_ROOT>"
$envName = "<ENV_NAME>"

New-Item -ItemType Directory -Force "$projectRoot\.conda\envs" | Out-Null
New-Item -ItemType Directory -Force "$projectRoot\.conda\pkgs" | Out-Null
New-Item -ItemType Directory -Force "$projectRoot\.pip-cache" | Out-Null

@"
envs_dirs:
  - $projectRoot\.conda\envs
pkgs_dirs:
  - $projectRoot\.conda\pkgs
auto_activate_base: false
"@ | Set-Content -Encoding ASCII "$projectRoot\.condarc"

$env:CONDARC = "$projectRoot\.condarc"
$env:PIP_CACHE_DIR = "$projectRoot\.pip-cache"

& "$minicondaRoot\Scripts\conda.exe" create -p "$projectRoot\.conda\envs\$envName" python=3.11 -y
& "$minicondaRoot\Scripts\conda.exe" run -p "$projectRoot\.conda\envs\$envName" python --version
```

## IDE AI Prompt Template

Use this exact request when delegating to another IDE agent:

```text
Bu projede paylasilan Miniconda kurulumu olarak <MINICONDA_ROOT> kullan.
Proje ici izole env olustur: <PROJECT_ROOT>\\.conda\\envs\\<ENV_NAME>.
Conda package cache: <PROJECT_ROOT>\\.conda\\pkgs.
Pip cache: <PROJECT_ROOT>\\.pip-cache.
<PROJECT_ROOT>\\.condarc olustur ve CONDARC'i bu dosyaya ayarla.
Base ortamina kurulum yapma. Tum kurulum/indirme artefactlari yalnizca <PROJECT_ROOT> altinda kalsin.
```

See `references/ide-prompt-template.md` for copy-paste variants.


