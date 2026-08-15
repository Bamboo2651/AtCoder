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

Write-Host "[AtCoder] Installing atcoder-cli 2.2.0 globally." -ForegroundColor Cyan
& $npmCommand.Source install --global atcoder-cli@2.2.0
if ($LASTEXITCODE -ne 0) {
    throw "Failed to install atcoder-cli."
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
Write-Host "Run 'acc login' once on this PC, then use 'acc new abcXXX' from:"
Write-Host "  $repoRoot"
