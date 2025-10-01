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
🛡️ **Permissions** • Installs system-wide (Administrator privileges required)  
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
| **OS** | Windows 10/11 |
| **Python** | 3.6+ *(only for script version)* |
| **Dependencies** | None *(uses Python standard library)* |
| **Permissions** | Administrator privileges required for system-wide install |

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
  # 🎨 FontFlow — Portable Distribution

  This folder contains the standalone FontFlow application you can distribute as a ZIP.

  Contents
  - `FontFlow.exe` — The standalone executable (recommended for end users)
  - `icon.ico`, `icon.png` — App icons used for shortcuts
  - `INSTALL_INFO.bat` — Optional installation helper (may contain convenience commands)
  - `utilities/` — Developer utilities and tests (not required for normal usage)

  Quick usage (for end users)
  1. Unzip the downloaded ZIP file to a location you prefer. Common locations:
     - `C:\Program Files\FontFlow` (for all users)
     - `C:\Tools\FontFlow` (portable, system-wide for admins)
     - `C:\Users\<you>\Applications\FontFlow` (per-user)

  2. Run the application:
     - Double-click `FontFlow.exe`
     - Or open PowerShell / Command Prompt and run:
  ```powershell
  & "C:\Path\To\FontFlow\FontFlow.exe"
  ```

  Recommended placement
  - For a system-wide install (visible to all users), extract to `C:\Program Files\FontFlow` and run as Administrator when required.
  - For a portable install (no admin required for extraction), place the folder anywhere you like (USB drive, `C:\Tools`, or your user folder).

  Create shortcuts (Start Menu, Desktop)

  - Create a Desktop shortcut (manual):
    1. Right-click `FontFlow.exe` → Send to → Desktop (create shortcut)

  - Create a Start Menu shortcut (per-user):
    1. Open `File Explorer` and enter `%appdata%\Microsoft\Windows\Start Menu\Programs` in the address bar.
    2. Copy a shortcut to `FontFlow.exe` into that folder (Right-click `FontFlow.exe` → Create shortcut → Move the shortcut into the Start Menu folder).

  - Create an All Users Start Menu shortcut (requires Administrator):
    1. Open `C:\ProgramData\Microsoft\Windows\Start Menu\Programs` (you may need elevated permissions).
    2. Place the shortcut there so the app appears for all users.

  PowerShell script to create a Desktop shortcut (example)
  ```powershell
  $W = New-Object -ComObject WScript.Shell
  $s = $W.CreateShortcut("$env:Public\Desktop\FontFlow.lnk")
  $s.TargetPath = 'C:\Path\To\FontFlow\FontFlow.exe'
  $s.IconLocation = 'C:\Path\To\FontFlow\icon.ico'
  $s.Save()
  ```

  Pin to Taskbar or Start
  - Right-click the executable or the shortcut and choose **Pin to taskbar** or **Pin to Start**.
  - Note: Some versions of Windows require you to right-click the shortcut in the Start Menu or Desktop to reveal the pin options.

  Running the script version (developer / source)
  - If you distributed the full source and Python script instead of the EXE, run:
  ```powershell
  python font_installer.py
  ```

  Permissions & Administrator notes
  - Installing fonts system-wide requires Administrator privileges. If the app prompts for elevation, run it as Administrator (right-click → Run as administrator).
  - If you prefer not to give admin rights, you can still extract the ZIP and keep FontFlow portable, but system-wide font installation requires elevation.

  Uninstall / Remove
  - To remove FontFlow simply delete the extracted `FontFlow` folder and any shortcuts you created.

  Troubleshooting
  - If FontFlow doesn't start, make sure Windows Defender or other antivirus didn't block `FontFlow.exe`.
  - If fonts didn't appear in applications after install, try restarting the target application; if that fails, run the installer as Administrator and try again.

  Contact / Support
  - For issues, check the `utilities/` scripts to run local checks, or file an issue with the distributor.

  Enjoy — simple, portable font installation with FontFlow.
