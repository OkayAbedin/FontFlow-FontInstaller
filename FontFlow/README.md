# 🎨 FontFlow

[![Windows](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.6+-green?style=flat-square&logo=python)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/badge/Release-Standalone-purple?style=flat-square)](FontFlow/)

> 🚀 A sleek, modern Windows application for effortless font installation from ZIP archives

<div align="center">
  <img src="icon.png" alt="FontFlow Icon" width="128" height="128">
</div>

## ✨ Features

🎯 **Modern GUI** • Clean, intuitive interface with native Windows styling and custom icon  
📦 **Bulk Installation** • Select and install multiple ZIP files simultaneously  
🔍 **Auto-Detection** • Automatically finds TTF, OTF, TTC, and OTC font files  
🛡️ **Smart Permissions** • Tries system-wide installation, falls back to user-level gracefully  
📊 **Progress Tracking** • Real-time progress updates with detailed feedback  
🔧 **Error Handling** • Comprehensive error handling with user-friendly messages  
⚡ **Windows Integration** • Proper font registration using Windows APIs

## 🚀 Quick Start

### Option 1: Standalone Executable (Recommended)
```bash
# Download and run - no Python required!
./FontFlow/FontFlow.exe
```

### Option 2: Python Script
```bash
# Clone the repository
git clone <repository-url>
cd FontFlow

# Run directly
python font_installer.py
```

## 📋 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11 (or Windows 7+) |
| **Python** | 3.6+ *(only for script version)* |
| **Dependencies** | None *(uses Python standard library)* |
| **Permissions** | User-level *(Admin optional for system-wide install)* |

## 📖 How to Use

### 1️⃣ Launch the Application
```bash
python font_installer.py    # Script version
# OR
FontFlow.exe                # Standalone version
```

### 2️⃣ Select Your Font Archives
- 🖱️ Click **"Select ZIP Files"** button
- 📁 Choose one or multiple ZIP archives containing fonts
- 📝 Selected files will appear in the list

### 3️⃣ Install Fonts
- ⚡ Click **"Install Fonts"** button
- 🔄 The app will automatically:
  - Extract font files from ZIP archives
  - Copy them to Windows Fonts directory
  - Register them with Windows system
  - Show real-time progress updates

### 4️⃣ Enjoy Your New Fonts
- ✅ Fonts are immediately available in all applications
- 🔄 No restart required!
- 🔒 **Fonts persist across computer reboots** (properly registered in Windows registry)

## 🔒 Font Persistence

FontFlow ensures your installed fonts remain available even after restarting your computer by:

- 📝 **Registry Registration**: Fonts are properly registered in the Windows registry
  - System-wide: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts`
  - User-level: `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts`
- 💾 **File Persistence**: Font files are copied to permanent directories
- 🔄 **Windows Integration**: Uses official Windows font APIs for maximum compatibility

## 🎯 Supported Font Formats

| Format | Description | Extension |
|--------|-------------|-----------|
| **TTF** | TrueType Font | `.ttf` |
| **OTF** | OpenType Font | `.otf` |
| **TTC** | TrueType Collection | `.ttc` |
| **OTC** | OpenType Collection | `.otc` |

## 🔧 Installation Types

| Type | Description | Requirements |
|------|-------------|--------------|
| 🌍 **System-wide** | Available to all users | Administrator privileges |
| 👤 **User-level** | Current user only | No special permissions |

> 💡 **Smart Fallback**: FontFlow automatically tries system-wide installation first, then gracefully falls back to user-level if admin access isn't available.

## ⚙️ Technical Details

<details>
<summary>🔧 <strong>Technical Implementation</strong></summary>

- **Windows API Integration**: Uses `AddFontResourceW` for proper font registration
- **Registry Persistence**: Fonts are permanently registered in Windows registry for persistence across reboots
- **Threading**: Implements thread-based installation to maintain responsive GUI
- **Best Practices**: Follows Windows font installation guidelines
- **Modern UI**: Built with tkinter using native Windows styling
- **Error Recovery**: Comprehensive error handling with graceful degradation

</details>

<details>
<summary>📊 <strong>Performance & Compatibility</strong></summary>

- **Lightweight**: ~11MB standalone executable
- **Fast**: Efficient ZIP extraction and font processing
- **Compatible**: Windows 7, 8, 10, 11 support
- **Portable**: No installation required for standalone version
- **Clean**: Automatic temporary file cleanup

</details>

## 🆘 Troubleshooting

<details>
<summary>❓ <strong>Common Issues & Solutions</strong></summary>

### 🔍 **Fonts not appearing in applications**
- Try restarting the application that should use the font
- User-level fonts may take a moment to appear in some apps
- Verify the font file wasn't corrupted during extraction

### ❌ **Installation fails**  
- The app automatically tries user-level installation if system-wide fails
- Check that ZIP files aren't corrupted or password-protected
- Ensure ZIP files actually contain valid font files

### 🛡️ **Want system-wide installation**
- Right-click batch file → **"Run as Administrator"**
- Or launch Command Prompt as Administrator: `python font_installer.py`

### 🚫 **Application won't start**
- Ensure Python 3.6+ is installed (script version only)
- Run `python test_compatibility.py` to check your system
- Note: This application only works on Windows

</details>

## 🏗️ Building from Source

<details>
<summary>🔨 <strong>Create Standalone Executable</strong></summary>

```bash
# Install build dependencies
pip install -r build_requirements.txt

# Build standalone executable
python build_standalone.py

# Or use PowerShell
./BUILD_STANDALONE.ps1
```

**Output**: Complete `FontFlow/` folder ready for distribution

</details>

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 **Report bugs** via GitHub Issues
- 💡 **Suggest features** or improvements  
- 🔧 **Submit pull requests** with enhancements
- 📖 **Improve documentation**

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## ⭐ Show Your Support

If FontFlow helped you manage your fonts more easily, please consider:
- ⭐ **Starring** this repository
- 🐦 **Sharing** with fellow designers and developers
- 🔄 **Contributing** to make it even better

---

<div align="center">
  <strong>Made with ❤️ for the design community</strong><br>
  <em>Simple font installation • Modern interface • Zero hassle</em>
</div>
