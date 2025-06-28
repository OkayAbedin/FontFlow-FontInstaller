# Font Installer - Quick Start Guide

## 🎯 What This Does
A simple, modern Windows application that automatically installs TTF and OTF fonts from ZIP files.

## 🚀 How to Use

### Method 1: Double-click to run
- **`run_font_installer.bat`** - Simple batch file launcher
- **`run_font_installer.ps1`** - PowerShell launcher with admin check

### Method 2: Command line
```bash
python font_installer.py
```

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

- `font_installer.py` - Main application with modern UI
- `test_compatibility.py` - System compatibility checker
- `test_font_directories.py` - Font directory access tester
- `create_test_fonts.py` - Creates test ZIP files for testing
- `run_font_installer.bat` - Windows batch launcher
- `run_font_installer.ps1` - PowerShell launcher
- `README.md` - Detailed documentation
- `requirements.txt` - Dependencies (none needed!)
- `QUICK_START.md` - This file

## 🔍 Troubleshooting

**Application won't start?**
- Run `python test_compatibility.py` to check your system
- Ensure Python 3.6+ is installed

**Fonts not installing?**
- The app automatically tries multiple user directories for maximum compatibility
- Run `python test_font_directories.py` to check directory access
- Check that ZIP files contain actual font files
- Ensure font files aren't corrupted
- If all user directories fail, try running as Administrator

**Need help?**
- Check the detailed `README.md` file
- Run the compatibility test first

---
**Ready to install some fonts? Double-click `run_font_installer.bat` to get started!** 🎨
