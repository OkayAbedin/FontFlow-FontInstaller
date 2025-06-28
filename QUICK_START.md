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

- **Modern GUI** - Clean, intuitive Windows-native interface
- **Bulk Processing** - Handle multiple ZIP files at once
- **Auto-Detection** - Finds TTF, OTF, TTC, OTC files automatically
- **Progress Tracking** - Real-time status updates
- **Error Handling** - Clear error messages and recovery
- **Thread-Safe** - Non-blocking installation process

## 🔧 Technical Notes

- **No External Dependencies** - Uses only Python standard library
- **Windows API Integration** - Proper font registration with `AddFontResourceW`
- **Temporary File Cleanup** - Automatic cleanup of extracted files
- **Font Format Support** - TTF, OTF, TTC, OTC formats

## 💡 Tips

- **Run as Administrator** for best results (recommended but not required)
- **Multiple ZIP files** can be selected at once
- **Nested folders** in ZIP files are supported
- **Duplicate fonts** are handled gracefully
- **No restart required** - fonts available immediately

## 🛠️ Files in This Package

- `font_installer.py` - Main application
- `test_compatibility.py` - System compatibility checker
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
- Try running as Administrator
- Check that ZIP files contain actual font files
- Ensure font files aren't corrupted

**Need help?**
- Check the detailed `README.md` file
- Run the compatibility test first

---
**Ready to install some fonts? Double-click `run_font_installer.bat` to get started!** 🎨
