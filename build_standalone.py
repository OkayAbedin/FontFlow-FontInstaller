#!/usr/bin/env python3
"""
Build script for Font Installer
Creates a standalone executable using PyInstaller
"""

import subprocess
import sys
import os
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        import PyInstaller
        print("✓ PyInstaller is already installed")
        return True
    except ImportError:
        print("📦 Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller>=5.0"])
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install PyInstaller: {e}")
            return False

def create_executable():
    """Create standalone executable using PyInstaller."""
    print("🔨 Building standalone executable...")
    
    # PyInstaller command with options for a clean, standalone build
    cmd = [
        sys.executable, "-m", "PyInstaller",  # Use python -m PyInstaller
        "--onefile",                    # Create single executable file
        "--windowed",                   # Hide console window (GUI app)
        "--name=FontInstaller",         # Name of executable
        "--clean",                      # Clean PyInstaller cache
        "--noconfirm",                  # Overwrite without asking
        "font_installer.py"             # Main script
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✓ Executable created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def create_distribution_folder():
    """Create a distribution folder with the executable and supporting files."""
    print("📁 Creating distribution folder...")
    
    dist_folder = Path("FontInstaller_Standalone")
    dist_folder.mkdir(exist_ok=True)
    
    # Files to include in distribution
    files_to_copy = [
        ("dist/FontInstaller.exe", "FontInstaller.exe"),
        ("README.md", "README.md"),
        ("QUICK_START.md", "QUICK_START.md"),
        ("test_compatibility.py", "test_compatibility.py"),
        ("test_font_directories.py", "test_font_directories.py"),
        ("create_test_fonts.py", "create_test_fonts.py"),
    ]
    
    # Copy files to distribution folder
    import shutil
    for src, dst in files_to_copy:
        src_path = Path(src)
        dst_path = dist_folder / dst
        
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print(f"  ✓ Copied {src} -> {dst}")
        else:
            print(f"  ⚠️  Missing {src}")
    
    return dist_folder

def create_installer_script():
    """Create a simple installer batch script."""
    installer_script = '''@echo off
echo Font Installer - Standalone Distribution
echo =========================================
echo.
echo This standalone version includes:
echo - FontInstaller.exe (main application)
echo - Supporting documentation and test scripts
echo - No Python installation required!
echo.
echo To run the Font Installer:
echo 1. Double-click FontInstaller.exe
echo 2. Or run from command line: FontInstaller.exe
echo.
echo Test scripts (requires Python if you want to run them):
echo - test_compatibility.py - Check system compatibility
echo - test_font_directories.py - Test font directory access
echo - create_test_fonts.py - Create test font files
echo.
echo Ready to install fonts!
echo.
pause
'''
    
    with open("FontInstaller_Standalone/INSTALL_INFO.bat", "w") as f:
        f.write(installer_script)
    
    print("✓ Created installer info script")

def main():
    """Main build process."""
    print("Font Installer - Standalone Build System")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("font_installer.py").exists():
        print("❌ Error: font_installer.py not found")
        print("Please run this script from the FontInstaller directory")
        return False
    
    # Step 1: Install PyInstaller
    if not install_pyinstaller():
        return False
    
    # Step 2: Create executable
    if not create_executable():
        return False
    
    # Step 3: Create distribution folder
    dist_folder = create_distribution_folder()
    
    # Step 4: Create installer info
    create_installer_script()
    
    print("\n" + "=" * 50)
    print("🎉 Build completed successfully!")
    print(f"📁 Distribution folder: {dist_folder.absolute()}")
    print(f"🚀 Executable: {dist_folder / 'FontInstaller.exe'}")
    print("\nTo distribute:")
    print(f"1. Share the entire '{dist_folder}' folder")
    print("2. Users can run FontInstaller.exe directly (no Python needed!)")
    print("3. Include INSTALL_INFO.bat for user instructions")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
