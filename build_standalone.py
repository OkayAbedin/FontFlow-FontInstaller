#!/usr/bin/env python3
"""
Build script for FontFlow
Creates a standalone executable using PyInstaller
"""

import subprocess
import sys
import os
from pathlib import Path

def convert_icon():
    """Convert PNG icon to ICO format for Windows compatibility."""
    if not Path("icon.png").exists():
        print("⚠️  icon.png not found - skipping icon conversion")
        return False
    
    try:
        from PIL import Image
        
        # Open PNG image
        img = Image.open("icon.png")
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create multiple sizes for ICO (Windows standard sizes)
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # Save as ICO
        img.save("icon.ico", format='ICO', sizes=sizes)
        
        print("✓ Converted icon.png to icon.ico")
        return True
        
    except ImportError:
        print("⚠️  PIL/Pillow not found - install with: pip install Pillow")
        print("⚠️  Continuing without icon conversion...")
        return False
    except Exception as e:
        print(f"⚠️  Error converting icon: {e}")
        return False

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
        "--name=FontFlow",         # Name of executable
        "--icon=icon.ico",              # Application icon
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
    
    dist_folder = Path("FontFlow_Standalone")
    dist_folder.mkdir(exist_ok=True)
    
    # Files to include in distribution
    files_to_copy = [
        ("dist/FontFlow.exe", "FontFlow.exe"),
        ("README.md", "README.md"),
        ("icon.ico", "icon.ico"),
    ]
    
    # Utility files for utilities subdirectory
    utility_files = [
        ("test_compatibility.py", "utilities/test_compatibility.py"),
        ("test_font_directories.py", "utilities/test_font_directories.py"),
        ("create_test_fonts.py", "utilities/create_test_fonts.py"),
    ]
    
    # Copy files to distribution folder
    import shutil
    
    # Copy main files
    for src, dst in files_to_copy:
        src_path = Path(src)
        dst_path = dist_folder / dst
        
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print(f"  ✓ Copied {src} -> {dst}")
        else:
            print(f"  ⚠️  Missing {src}")
    
    # Create utilities directory and copy utility files
    utilities_dir = dist_folder / "utilities"
    utilities_dir.mkdir(exist_ok=True)
    
    for src, dst in utility_files:
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
echo FontFlow - Standalone Distribution
echo ===================================
echo.
echo This standalone version includes:
echo - FontFlow.exe (main application)
echo - Supporting documentation and test scripts
echo - No Python installation required!
echo.
echo To run FontFlow:
echo 1. Double-click FontFlow.exe
echo 2. Or run from command line: FontFlow.exe
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
    
    with open("FontFlow_Standalone/INSTALL_INFO.bat", "w") as f:
        f.write(installer_script)
    
    print("✓ Created installer info script")

def main():
    """Main build process."""
    print("FontFlow - Standalone Build System")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("font_installer.py").exists():
        print("❌ Error: font_installer.py not found")
        print("Please run this script from the FontFlow directory")
        return False
    
    # Step 1: Convert icon to ICO format
    convert_icon()
    
    # Step 2: Install PyInstaller
    if not install_pyinstaller():
        return False
    
    # Step 3: Create executable
    if not create_executable():
        return False
    
    # Step 4: Create distribution folder
    dist_folder = create_distribution_folder()
    
    # Step 5: Create installer info
    create_installer_script()
    
    print("\n" + "=" * 50)
    print("🎉 Build completed successfully!")
    print(f"📁 Distribution folder: {dist_folder.absolute()}")
    print(f"🚀 Executable: {dist_folder / 'FontFlow.exe'}")
    print("\nTo distribute:")
    print(f"1. Share the entire '{dist_folder}' folder")
    print("2. Users can run FontFlow.exe directly (no Python needed!)")
    print("3. Include INSTALL_INFO.bat for user instructions")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
