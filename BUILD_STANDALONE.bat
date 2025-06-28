@echo off
echo FontFlow - Standalone Builder
echo ====================================
echo.
echo This script will:
echo 1. Install PyInstaller (if needed)
echo 2. Build a standalone FontInstaller.exe
echo 3. Create a distribution folder
echo.
echo No Python knowledge required - just run this script!
echo.
pause
echo.
echo Starting build process...
echo.

python build_standalone.py

echo.
echo Build process completed!
echo Check the FontInstaller_Standalone folder for the results.
echo.
pause
