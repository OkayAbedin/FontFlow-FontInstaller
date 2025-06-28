# Font Installer - Quick Start Guide

## 🎯 What This Does
A simple, modern Windows application that automatically installs TTF and OTF fonts from ZIP files.

## 🚀 How to Use

### Method 1: Standalone Executable (Recommended)
- **Download `FontInstaller_Standalone` folder**
- **Double-click `FontInstaller.exe`** - No Python required!
- **That's it!** - Ready to use immediately

### Method 2: Double-click Python scripts (requires Python)
- **`run_font_installer.bat`** - Simple batch file launcher
- **`run_font_installer.ps1`** - PowerShell launcher with admin check

### Method 3: Command line (requires Python)
```bash
python font_installer.py
```

## 📦 Standalone Version Benefits
- ✅ **No Python installation required** - Everything bundled
- ✅ **Single executable file** - Just run FontInstaller.exe
- ✅ **No dependencies** - Completely self-contained
- ✅ **Professional distribution** - Perfect for sharing
- ✅ **Same features** - Full functionality included
- ✅ **Faster startup** - Optimized performance

## 📋 Step-by-Step Usage

1. **Start the application** using one of the methods above
2. **Click "Select ZIP Files"** to choose your font archives
3. **Review** the selected files in the list
4. **Click "Install Fonts"** to start the installation
5. **Watch the progress** as fonts are extracted and installed
6. **Done!** Fonts are immediately available in all applications

## ✨ Features

- **Modern UI Design** - Beautiful, clean interface with modern typography and icons
- **Smart Permission Handling** - Automatic fallback with multiple directory options
- **Robust User Installation** - Multiple fallback directories ensure installation success
- **Bulk Processing** - Handle multiple ZIP files at once
- **Auto-Detection** - Finds TTF, OTF, TTC, OTC files automatically
- **Real-time Progress** - Live status updates with progress indicators
- **Error Handling** - Clear error messages and recovery options
- **Thread-Safe** - Non-blocking installation process
- **Instant Feedback** - Visual status indicators with emojis and modern styling

## 🔧 Technical Notes

- **Modern UI Framework** - Enhanced tkinter with modern styling and typography
- **No External Dependencies** - Uses only Python standard library
- **Windows API Integration** - Proper font registration with `AddFontResourceW`
- **Smart Installation Logic** - System-wide with automatic user-level fallback
- **Temporary File Cleanup** - Automatic cleanup of extracted files
- **Font Format Support** - TTF, OTF, TTC, OTC formats
- **Visual Feedback** - Modern progress indicators and status icons

## 💡 Tips

- **Permission Modes** - The app shows whether you're in Admin or User mode
- **Multiple Fallback Locations** - Tries several user directories if one fails
- **No Admin Required** - User-level installation works perfectly in multiple locations
- **Multiple ZIP files** can be selected at once
- **Nested folders** in ZIP files are supported
- **Duplicate fonts** are handled gracefully
- **No restart required** - fonts available immediately
- **Modern Visual Feedback** - Icons and status updates keep you informed

## 🛠️ Files in This Package

### **Main Application:**
- `FontInstaller.exe` - **Standalone executable (recommended!)**
- `font_installer.py` - Python source version

### **Build System:**
- `build_standalone.py` - Creates standalone executable
- `BUILD_STANDALONE.bat` - Easy build script (Windows)
- `BUILD_STANDALONE.ps1` - PowerShell build script
- `build_requirements.txt` - Build dependencies

### **Testing & Documentation:**
- `test_compatibility.py` - System compatibility checker
- `test_font_directories.py` - Font directory access tester
- `create_test_fonts.py` - Creates test ZIP files for testing
- `README.md` - Detailed documentation
- `QUICK_START.md` - This file
- `STANDALONE_GUIDE.md` - Complete standalone distribution guide

### **Launch Scripts (for Python version):**
- `run_font_installer.bat` - Windows batch launcher
- `run_font_installer.ps1` - PowerShell launcher
- `requirements.txt` - Python dependencies (none needed!)

## 🔍 Troubleshooting

**Application won't start?**
- **Standalone version:** Just double-click `FontInstaller.exe` - no setup needed!
- **Python version:** Run `python test_compatibility.py` to check your system
- Ensure you have the correct version for your system (64-bit Windows)

**Want to build your own executable?**
- Run `BUILD_STANDALONE.bat` to create your own standalone version
- Check `STANDALONE_GUIDE.md` for complete build instructions

**Fonts not installing?**
- The app automatically tries multiple user directories for maximum compatibility
- Run `python test_font_directories.py` to check directory access
- Check that ZIP files contain actual font files
- Ensure font files aren't corrupted
- If all user directories fail, try running as Administrator

**Need help?**
- Check the detailed `README.md` file
- Check `STANDALONE_GUIDE.md` for standalone version info
- Run the compatibility test first

---
**Ready to install some fonts?**
- **Standalone:** Double-click `FontInstaller.exe` 🚀
- **Python:** Double-click `run_font_installer.bat` 🎨
