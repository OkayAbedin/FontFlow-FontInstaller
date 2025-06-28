# Font Installer

A simple, modern Windows application for installing TTF and OTF fonts from ZIP archives.

## Features

- **Modern GUI**: Clean, intuitive interface using native Windows styling
- **Bulk Installation**: Select multiple ZIP files at once
- **Auto-Detection**: Automatically finds TTF, OTF, TTC, and OTC font files within ZIP archives
- **Smart Permission Handling**: 
  - Tries system-wide installation first (requires Administrator privileges)
  - Falls back to user-level installation automatically if admin access is not available
  - Clear feedback about installation type and success rate
- **Progress Tracking**: Real-time progress updates during installation
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Windows Integration**: Properly registers fonts with Windows system

## Requirements

- Windows operating system
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. No additional packages to install - uses built-in Python libraries only!

## Usage

1. **Run the application**:
   ```bash
   python font_installer.py
   ```

2. **Select ZIP files**:
   - Click "Select ZIP Files" button
   - Choose one or multiple ZIP archives containing fonts
   - Selected files will appear in the list

3. **Install fonts**:
   - Click "Install Fonts" button
   - The app will:
     - Extract all font files from the ZIP archives
     - Copy them to Windows Fonts directory
     - Register them with the Windows system
     - Show progress and completion status

4. **Use your fonts**:
   - Installed fonts are immediately available in all applications
   - No restart required

## Supported Font Formats

- **TTF** (TrueType Font)
- **OTF** (OpenType Font)
- **TTC** (TrueType Collection)
- **OTC** (OpenType Collection)

## Notes

- **Administrator Privileges**: 
  - **With Admin**: Fonts install system-wide (available to all users)
  - **Without Admin**: Fonts install for current user only (automatic fallback)
  - The app handles both scenarios gracefully
- **Font Conflicts**: If a font with the same name already exists, the installation may be skipped
- **Automatic Cleanup**: Temporary files are automatically cleaned up after installation
- **Installation Types**: The app will clearly indicate whether fonts were installed system-wide or user-level

## Technical Details

- Uses Windows API (`AddFontResourceW`) for proper font registration
- Implements thread-based installation to keep GUI responsive
- Follows Windows font installation best practices
- Modern tkinter GUI with native Windows styling

## Troubleshooting

**Fonts not appearing in applications**:
- Try restarting the application that should use the font
- User-level fonts may take a moment to appear in some applications
- Check if the font file was corrupted

**Installation fails**:
- The app automatically tries user-level installation if system-wide fails
- Check that ZIP files are not corrupted
- Ensure ZIP files actually contain font files

**Want system-wide installation**:
- Right-click the batch file and "Run as Administrator"
- Or start Command Prompt as Administrator and run `python font_installer.py`

**Application won't start**:
- Ensure Python 3.6+ is installed
- Run `python test_compatibility.py` to check your system
- This application only works on Windows

## License

This project is open source and available under the MIT License.
