$ErrorActionPreference = "Stop"

$workspaceRoot = Split-Path -Parent $PSScriptRoot
$atcoderModule = Join-Path $workspaceRoot "myenv\Lib\site-packages\onlinejudge\service\atcoder.py"

if (-not (Test-Path -LiteralPath $atcoderModule -PathType Leaf)) {
    throw "AtCoder module not found: $atcoderModule"
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$source = [System.IO.File]::ReadAllText($atcoderModule, $utf8).Replace("`r`n", "`n")

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

if (-not $source.Contains("(KB|MB|KiB|MiB)") -and $source.Contains($oldPattern)) {
    $source = $source.Replace($oldPattern, $newPattern)
    $changed = $true
}

if (-not $source.Contains("elif memory_limit_unit == 'MiB':")) {
    $oldKbConversion = "        if memory_limit_unit == 'KB':`n            memory_limit_byte = int(float(memory_limit_value) * 1000)"
    $newKbConversion = "$oldKbConversion`n        elif memory_limit_unit == 'KiB':`n            memory_limit_byte = int(float(memory_limit_value) * 1024)"
    $oldMbConversion = "        elif memory_limit_unit == 'MB':`n            memory_limit_byte = int(float(memory_limit_value) * 1000 * 1000)"
    $newMbConversion = "$oldMbConversion`n        elif memory_limit_unit == 'MiB':`n            memory_limit_byte = int(float(memory_limit_value) * 1024 * 1024)"
    if (-not $source.Contains($oldKbConversion) -or -not $source.Contains($oldMbConversion)) {
        throw "The installed online-judge-tools problem parser is unsupported."
    }
    $source = $source.Replace($oldKbConversion, $newKbConversion).Replace($oldMbConversion, $newMbConversion)
    $changed = $true
}

if (-not $source.Contains("elif tds[3].text.endswith(' MiB')")) {
    $oldTableKbConversion = "        if tds[3].text.endswith(' KB'):`n            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' KB')) * 1000)"
    $newTableKbConversion = "$oldTableKbConversion`n        elif tds[3].text.endswith(' KiB'):`n            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' KiB')) * 1024)"
    $oldTableMbConversion = "        elif tds[3].text.endswith(' MB'):`n            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' MB')) * 1000 * 1000)  # TODO: confirm this is MB truly, not MiB"
    $newTableMbConversion = "$oldTableMbConversion`n        elif tds[3].text.endswith(' MiB'):`n            memory_limit_byte = int(float(utils.remove_suffix(tds[3].text, ' MiB')) * 1024 * 1024)"
    if (-not $source.Contains($oldTableKbConversion) -or -not $source.Contains($oldTableMbConversion)) {
        throw "The installed online-judge-tools contest parser is unsupported."
    }
    $source = $source.Replace($oldTableKbConversion, $newTableKbConversion).Replace($oldTableMbConversion, $newTableMbConversion)
    $changed = $true
}

if ($changed) {
    [System.IO.File]::WriteAllText($atcoderModule, $source, $utf8)
    Write-Host "[AtCoder] Applied MiB compatibility patch to online-judge-tools." -ForegroundColor DarkGray
}
