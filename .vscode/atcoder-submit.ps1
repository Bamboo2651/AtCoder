param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath,

    [ValidateSet("o", "p")]
    [string]$SubmissionMode
)

$ErrorActionPreference = "Stop"
$compatibilityPatch = Join-Path $PSScriptRoot "patch-onlinejudge-mib.ps1"
& $compatibilityPatch

$sourceFile = Get-Item -LiteralPath $FilePath
$problemDirectory = $sourceFile.Directory.FullName
$contestDirectory = $sourceFile.Directory.Parent.FullName
$contestConfig = Join-Path $contestDirectory "contest.acc.json"
$workspaceRoot = Split-Path -Parent $PSScriptRoot
$pythonPath = Join-Path $workspaceRoot "myenv\Scripts\python.exe"
$phaseScript = Join-Path $PSScriptRoot "atcoder-contest-phase.py"

if ($sourceFile.Extension -ne ".py") {
    throw "Open a Python file before running this task: $FilePath"
}

if (-not (Test-Path -LiteralPath $contestConfig -PathType Leaf)) {
    throw "contest.acc.json not found: $contestConfig`nOpen main.py in a task created by acc new."
}

if (-not (Test-Path -LiteralPath $pythonPath -PathType Leaf)) {
    throw "Virtual environment Python not found: $pythonPath"
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$contestData = [System.IO.File]::ReadAllText($contestConfig, $utf8) | ConvertFrom-Json
$taskData = $contestData.tasks | Where-Object {
    $_.directory.path -eq $sourceFile.Directory.Name -and
    $_.directory.submit -eq $sourceFile.Name
} | Select-Object -First 1

if ($null -eq $taskData) {
    throw "This file is not registered as a submission file in contest.acc.json: $FilePath"
}

$contestId = $contestData.contest.id
$taskId = $taskData.id
$problemUrl = "https://atcoder.jp/contests/$contestId/tasks/$taskId"
$submitUrl = "https://atcoder.jp/contests/$contestId/submit?taskScreenName=$taskId"

if ([string]::IsNullOrWhiteSpace($SubmissionMode)) {
    Write-Host "  o: Official contest submission (only while the contest is running)" -ForegroundColor Cyan
    Write-Host "  p: Practice submission (only after the contest has ended)" -ForegroundColor Cyan
    $SubmissionMode = (Read-Host "Choose submission mode [o/p, Enter=cancel]").Trim().ToLowerInvariant()
    if ($SubmissionMode -notin @("o", "p")) {
        Write-Host "[Canceled] The solution was not submitted." -ForegroundColor Yellow
        exit 0
    }
}

Write-Host "[AtCoder] Checking the contest period." -ForegroundColor Cyan
$phaseOutput = & $pythonPath $phaseScript $contestId
if ($LASTEXITCODE -ne 0) {
    throw "Failed to read the contest period from AtCoder."
}

$contestPhase = ($phaseOutput -join "`n") | ConvertFrom-Json

if ($SubmissionMode -eq "o" -and $contestPhase.phase -ne "ongoing") {
    throw "Official submission is available only during the contest. Current phase: $($contestPhase.phase)"
}

if ($SubmissionMode -eq "p" -and $contestPhase.phase -ne "ended") {
    throw "Practice submission is available only after the contest. Current phase: $($contestPhase.phase)"
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$sourceCode = [System.IO.File]::ReadAllText($sourceFile.FullName, $utf8)
Set-Clipboard -Value $sourceCode

Push-Location $problemDirectory
try {
    Write-Host "[AtCoder] Target: $contestId / $taskId" -ForegroundColor Cyan
    Write-Host "[AtCoder] Source code copied to the clipboard." -ForegroundColor Green
    Write-Host "[AtCoder] Paste it, select CPython, and press Submit in the browser." -ForegroundColor Yellow
    Start-Process $submitUrl
    exit 0
}
finally {
    Pop-Location
}
