$ErrorActionPreference = "Stop"

$workspaceRoot = Split-Path -Parent $PSScriptRoot
$atcoderModule = Join-Path $workspaceRoot "myenv\Lib\site-packages\onlinejudge\service\atcoder.py"

if (-not (Test-Path -LiteralPath $atcoderModule -PathType Leaf)) {
    throw "AtCoder module not found: $atcoderModule"
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$source = [System.IO.File]::ReadAllText($atcoderModule, $utf8)

$oldPattern = "(KB|MB)', memory_limit)"
$newPattern = "(KB|MB|KiB|MiB)', memory_limit)"
$oldConversion = @"
        if memory_limit_unit == 'KB':
            memory_limit_byte = int(float(memory_limit_value) * 1000)
        elif memory_limit_unit == 'MB':
            memory_limit_byte = int(float(memory_limit_value) * 1000 * 1000)
"@
$newConversion = @"
        if memory_limit_unit == 'KB':
            memory_limit_byte = int(float(memory_limit_value) * 1000)
        elif memory_limit_unit == 'KiB':
            memory_limit_byte = int(float(memory_limit_value) * 1024)
        elif memory_limit_unit == 'MB':
            memory_limit_byte = int(float(memory_limit_value) * 1000 * 1000)
        elif memory_limit_unit == 'MiB':
            memory_limit_byte = int(float(memory_limit_value) * 1024 * 1024)
"@
$oldTableConversion = @"
        if tds[3].text.endswith(' KB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' KB')) * 1000)
        elif tds[3].text.endswith(' MB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' MB')) * 1000 * 1000)  # TODO: confirm this is MB truly, not MiB
"@
$newTableConversion = @"
        if tds[3].text.endswith(' KB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' KB')) * 1000)
        elif tds[3].text.endswith(' KiB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' KiB')) * 1024)
        elif tds[3].text.endswith(' MB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' MB')) * 1000 * 1000)  # TODO: confirm this is MB truly, not MiB
        elif tds[3].text.endswith(' MiB'):
            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' MiB')) * 1024 * 1024)
"@

$changed = $false

if (-not $source.Contains("(KB|MB|KiB|MiB)")) {
    if (-not $source.Contains($oldPattern) -or -not $source.Contains($oldConversion)) {
        throw "The installed online-judge-tools problem parser is unsupported."
    }
    $source = $source.Replace($oldPattern, $newPattern).Replace($oldConversion, $newConversion)
    $changed = $true
}

if (-not $source.Contains("elif tds[3].text.endswith(' MiB')")) {
    if (-not $source.Contains($oldTableConversion)) {
        throw "The installed online-judge-tools contest parser is unsupported."
    }
    $source = $source.Replace($oldTableConversion, $newTableConversion)
    $changed = $true
}

if ($changed) {
    [System.IO.File]::WriteAllText($atcoderModule, $source, $utf8)
    Write-Host "[AtCoder] Applied MiB compatibility patch to online-judge-tools." -ForegroundColor DarkGray
}
