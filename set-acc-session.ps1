[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$accCommand = Get-Command acc.ps1, acc.cmd, acc -ErrorAction SilentlyContinue | Select-Object -First 1
if ($null -eq $accCommand) {
    throw "acc not found. Run setup-atcoder.ps1 first, then restart PowerShell."
}

$accPath = $accCommand.Source
$configDirectory = ((& $accPath config-dir) | Select-Object -Last 1).Trim()
if ([string]::IsNullOrWhiteSpace($configDirectory)) {
    throw "Failed to detect the atcoder-cli config directory."
}

Write-Host "Copy REVEL_SESSION from the browser developer tools." -ForegroundColor Cyan
Write-Host "The pasted value will not be displayed." -ForegroundColor DarkGray
$secureValue = Read-Host "REVEL_SESSION value" -AsSecureString
$valuePointer = [IntPtr]::Zero
$sessionValue = $null

try {
    $valuePointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureValue)
    $sessionValue = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($valuePointer).Trim().Trim('"')
    $sessionValue = $sessionValue -replace '^REVEL_SESSION=', ''

    if ([string]::IsNullOrWhiteSpace($sessionValue)) {
        throw "REVEL_SESSION is empty."
    }

    $sessionData = [ordered]@{
        cookies = @(
            "REVEL_FLASH="
            "REVEL_SESSION=$sessionValue"
        )
    }
    $sessionJson = $sessionData | ConvertTo-Json -Depth 3
    $sessionPath = Join-Path $configDirectory "session.json"
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($sessionPath, $sessionJson, $utf8)
}
finally {
    if ($valuePointer -ne [IntPtr]::Zero) {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($valuePointer)
    }
    $sessionValue = $null
    $secureValue = $null
}

$sessionStatus = ((& $accPath session) -join "`n").Trim()
if ($sessionStatus -notmatch '(?m)^OK$') {
    throw "acc could not verify the session. Log in again in the browser, copy a fresh REVEL_SESSION value, and retry."
}

Write-Host "[AtCoder] The login cookie was registered for acc." -ForegroundColor Green
