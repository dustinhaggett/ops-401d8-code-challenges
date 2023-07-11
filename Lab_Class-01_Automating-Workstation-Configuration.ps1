# Enable Windows Defender Real-Time Protection

# Check if Windows Defender Real-Time Protection is already enabled
$realTimeProtectionStatus = Get-MpPreference | Select-Object -ExpandProperty DisableRealtimeMonitoring

if ($realTimeProtectionStatus -eq $false) {
    Write-Output "Windows Defender Real-Time Protection is already enabled."
} else {
    # Enable Windows Defender Real-Time Protection
    Set-MpPreference -DisableRealtimeMonitoring $false
    Write-Output "Windows Defender Real-Time Protection has been successfully enabled."
}
