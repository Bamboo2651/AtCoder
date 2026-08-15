[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$repoRoot = $PSScriptRoot
$venvRoot = Join-Path $repoRoot "myenv"
$venvPython = Join-Path $venvRoot "Scripts\python.exe"
$ojPath = Join-Path $venvRoot "Scripts\oj.exe"
$requirementsPath = Join-Path $repoRoot "requirements-atcoder.txt"
$templateSource = Join-Path $repoRoot "atcoder-cli-template\python"

function Get-RequiredCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Name,

        [Parameter(Mandatory = $true)]
        [string]$InstallHint
    )

    foreach ($candidate in $Name) {
        $command = Get-Command $candidate -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -ne $command) {
            return $command
        }
    }

    throw "Required command not found: $($Name -join ', '). $InstallHint"
}

$npmCommand = Get-RequiredCommand -Name @("npm.cmd", "npm") -InstallHint "Install Node.js, restart PowerShell, and run this script again."
$pythonLauncher = Get-RequiredCommand -Name @("py.exe", "py", "python.exe", "python") -InstallHint "Install Python for Windows, restart PowerShell, and run this script again."

# A virtual environment contains absolute paths to the Python installation that
# created it, so it cannot be shared between PCs.  Avoid accidentally selecting
# the repository's own (possibly broken) virtual-environment launcher as the
# system Python used to recreate it.
if ($pythonLauncher.Source.StartsWith($venvRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Only the repository-local myenv Python was found. Install Python 3 for this PC, restart PowerShell, and run this script again."
}

Write-Host "[AtCoder] Installing atcoder-cli 2.2.0 globally." -ForegroundColor Cyan
& $npmCommand.Source install --global atcoder-cli@2.2.0
if ($LASTEXITCODE -ne 0) {
    throw "Failed to install atcoder-cli."
}

if (Test-Path -LiteralPath $venvPython -PathType Leaf) {
    & $venvPython -c "import sys; print(sys.executable)" *> $null
    if ($LASTEXITCODE -ne 0) {
        $backupName = "myenv-broken-{0}" -f (Get-Date -Format "yyyyMMdd-HHmmss")
        $backupPath = Join-Path $repoRoot $backupName
        Write-Host "[AtCoder] The existing myenv belongs to another or missing Python installation." -ForegroundColor Yellow
        Write-Host "[AtCoder] Moving it to: $backupPath" -ForegroundColor Yellow
        Move-Item -LiteralPath $venvRoot -Destination $backupPath
    }
}

if (-not (Test-Path -LiteralPath $venvPython -PathType Leaf)) {
    Write-Host "[AtCoder] Creating virtual environment: $venvRoot" -ForegroundColor Cyan
    if ($pythonLauncher.Name -like "py*") {
        & $pythonLauncher.Source -3 -m venv $venvRoot
    }
    else {
        & $pythonLauncher.Source -m venv $venvRoot
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create the Python virtual environment."
    }
}

Write-Host "[AtCoder] Installing Python tools into myenv." -ForegroundColor Cyan
& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    throw "Failed to upgrade pip."
}
& $venvPython -m pip install --requirement $requirementsPath
if ($LASTEXITCODE -ne 0) {
    throw "Failed to install Python requirements."
}

$accCommand = Get-RequiredCommand -Name @("acc.ps1", "acc.cmd", "acc") -InstallHint "Restart PowerShell after installing Node.js and atcoder-cli."
$accPath = $accCommand.Source

Write-Host "[AtCoder] Applying repository-local online-judge-tools compatibility settings." -ForegroundColor Cyan
& (Join-Path $repoRoot ".vscode\patch-onlinejudge-mib.ps1")

Write-Host "[AtCoder] Configuring atcoder-cli." -ForegroundColor Cyan
& $accPath config oj-path $ojPath
& $accPath config default-contest-dirname-format "{ContestID}"
& $accPath config default-task-dirname-format "{tasklabel}"
& $accPath config default-test-dirname-format "test"
& $accPath config default-task-choice "all"
& $accPath config default-template "python"

$configDirectory = ((& $accPath config-dir) | Select-Object -Last 1).Trim()
if ([string]::IsNullOrWhiteSpace($configDirectory)) {
    throw "Failed to detect the atcoder-cli config directory."
}

$templateDestination = Join-Path $configDirectory "python"
New-Item -ItemType Directory -Path $templateDestination -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $templateSource "main.py") -Destination (Join-Path $templateDestination "main.py") -Force
Copy-Item -LiteralPath (Join-Path $templateSource "template.json") -Destination (Join-Path $templateDestination "template.json") -Force

& $accPath check-oj
if ($LASTEXITCODE -ne 0) {
    throw "atcoder-cli could not use online-judge-tools."
}

Write-Host ""
Write-Host "[AtCoder] Local setup completed." -ForegroundColor Green
Write-Host "Next, log in to AtCoder in your browser and register REVEL_SESSION by running:"
Write-Host "  powershell -ExecutionPolicy Bypass -File .\set-acc-session.ps1"
Write-Host "See SETUP.md for the browser steps."
