# Font Installer PowerShell Launcher
Write-Host "Font Installer" -ForegroundColor Cyan
Write-Host "=================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "Note: Not running as Administrator. Some fonts may not install properly." -ForegroundColor Yellow
    Write-Host "For best results, right-click and 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Starting Font Installer..." -ForegroundColor Green
Write-Host ""

try {
    python font_installer.py
} catch {
    Write-Host "Error: Could not start Python application" -ForegroundColor Red
    Write-Host "Please ensure Python is installed and available in PATH" -ForegroundColor Red
}

Write-Host ""
Write-Host "Font Installer has closed." -ForegroundColor Green
Read-Host "Press Enter to exit"
