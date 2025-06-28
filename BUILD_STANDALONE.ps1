# Font Installer - Standalone Builder (PowerShell)
Write-Host "Font Installer - Standalone Builder" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "This script will:" -ForegroundColor Green
Write-Host "1. Install PyInstaller (if needed)" -ForegroundColor Yellow
Write-Host "2. Build a standalone FontInstaller.exe" -ForegroundColor Yellow
Write-Host "3. Create a distribution folder" -ForegroundColor Yellow
Write-Host ""
Write-Host "No Python knowledge required - just run this script!" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to continue or Ctrl+C to cancel" | Out-Null

Write-Host ""
Write-Host "Starting build process..." -ForegroundColor Green
Write-Host ""

try {
    # Run the build script
    python build_standalone.py
    
    Write-Host ""
    Write-Host "Build process completed!" -ForegroundColor Green
    Write-Host "Check the FontInstaller_Standalone folder for the results." -ForegroundColor Cyan
    
} catch {
    Write-Host ""
    Write-Host "Error during build process:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "Make sure Python is installed and available in PATH." -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to exit"
