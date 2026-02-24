param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot,

    [Parameter(Mandatory = $true)]
    [string]$MinicondaRoot,

    [Parameter(Mandatory = $true)]
    [string]$EnvName,

    [Parameter(Mandatory = $false)]
    [string]$PythonVersion = "3.11",

    [Parameter(Mandatory = $false)]
    [switch]$PersistCondarc
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Ensure-Directory([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

function Main {
    $resolvedProjectRoot = [System.IO.Path]::GetFullPath($ProjectRoot)
    $resolvedMinicondaRoot = [System.IO.Path]::GetFullPath($MinicondaRoot)
    $condaExe = Join-Path $resolvedMinicondaRoot "Scripts\\conda.exe"

    if (-not (Test-Path -LiteralPath $condaExe)) {
        throw "conda.exe bulunamadi: $condaExe"
    }

    Ensure-Directory -Path $resolvedProjectRoot

    $condaRoot = Join-Path $resolvedProjectRoot ".conda"
    $envsDir = Join-Path $condaRoot "envs"
    $pkgsDir = Join-Path $condaRoot "pkgs"
    $pipCacheDir = Join-Path $resolvedProjectRoot ".pip-cache"
    $condarcPath = Join-Path $resolvedProjectRoot ".condarc"
    $envPath = Join-Path $envsDir $EnvName

    Ensure-Directory -Path $envsDir
    Ensure-Directory -Path $pkgsDir
    Ensure-Directory -Path $pipCacheDir

    @"
envs_dirs:
  - $envsDir
pkgs_dirs:
  - $pkgsDir
auto_activate_base: false
"@ | Set-Content -Encoding ASCII -Path $condarcPath

    $env:CONDARC = $condarcPath
    $env:PIP_CACHE_DIR = $pipCacheDir

    if ($PersistCondarc) {
        setx CONDARC $condarcPath | Out-Null
    }

    if (-not (Test-Path -LiteralPath $envPath)) {
        & $condaExe create -p $envPath "python=$PythonVersion" -y
    } else {
        Write-Host "Conda env zaten var: $envPath"
    }

    $pythonExe = Join-Path $envPath "python.exe"
    if (Test-Path -LiteralPath $pythonExe) {
        $pythonVersion = & $pythonExe --version 2>&1
        $pipVersion = & $pythonExe -m pip --version 2>&1
    } else {
        # Fallback for uncommon env layouts.
        $pythonVersion = & $condaExe run -p $envPath python --version 2>&1
        $pipVersion = & $condaExe run -p $envPath python -m pip --version 2>&1
    }

    Write-Host ""
    Write-Host "Kurulum tamamlandi."
    Write-Host "ProjectRoot : $resolvedProjectRoot"
    Write-Host "Miniconda   : $resolvedMinicondaRoot"
    Write-Host "EnvPath     : $envPath"
    Write-Host "CONDARC     : $condarcPath"
    Write-Host "PIP_CACHE   : $pipCacheDir"
    Write-Host "Python      : $pythonVersion"
    Write-Host "Pip         : $pipVersion"
    Write-Host ""
    Write-Host "Calistirma ornegi:"
    Write-Host "& `"$condaExe`" run -p `"$envPath`" python --version"
}

Main
