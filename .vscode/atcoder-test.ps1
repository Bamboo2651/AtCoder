param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

$ErrorActionPreference = "Stop"
$workspaceRoot = Split-Path -Parent $PSScriptRoot
$sourceFile = Get-Item -LiteralPath $FilePath
$problemDirectory = $sourceFile.Directory.FullName
$testDirectory = Join-Path $problemDirectory "test"
$ojPath = Join-Path $workspaceRoot "myenv\Scripts\oj.exe"
$pythonPath = Join-Path $workspaceRoot "myenv\Scripts\python.exe"

if ($sourceFile.Extension -ne ".py") {
    throw "Open a Python file before running this task: $FilePath"
}

if (-not (Test-Path -LiteralPath $testDirectory -PathType Container)) {
    throw "Test directory not found: $testDirectory`nOpen main.py in a task created by acc new."
}

if (-not (Test-Path -LiteralPath $ojPath -PathType Leaf)) {
    throw "online-judge-tools not found: $ojPath"
}

if (-not (Test-Path -LiteralPath $pythonPath -PathType Leaf)) {
    throw "Virtual environment Python not found: $pythonPath"
}

$pythonCommand = '"' + $pythonPath + '" -u "' + $sourceFile.FullName + '"'

Push-Location $problemDirectory
try {
    Write-Host "[AtCoder] Running sample tests for $($sourceFile.FullName)" -ForegroundColor Cyan
    & $ojPath test -N -c $pythonCommand
    $testExitCode = $LASTEXITCODE

    if ($testExitCode -ne 0) {
        Write-Host "[Abort] Test failed. Submission canceled." -ForegroundColor Red
        exit $testExitCode
    }

    Write-Host "  o: Official contest submission (only while the contest is running)" -ForegroundColor Cyan
    Write-Host "  p: Practice submission (only after the contest has ended)" -ForegroundColor Cyan
    $answer = (Read-Host "Choose submission mode [o/p, Enter=cancel]").Trim().ToLowerInvariant()
    if ($answer -notin @("o", "p")) {
        Write-Host "[Canceled] The solution was not submitted." -ForegroundColor Yellow
        exit 0
    }

    $submitScript = Join-Path $PSScriptRoot "atcoder-submit.ps1"
    & $submitScript -FilePath $sourceFile.FullName -SubmissionMode $answer
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
