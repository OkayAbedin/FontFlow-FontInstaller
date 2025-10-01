# FontFlow Changelog

## [v1.1.0] - 2024-10-01 - Registry Persistence Fix

### 🔧 Fixed
- **CRITICAL**: Fonts now persist across computer reboots
  - Added proper Windows registry registration for both system and user installations
  - Fonts are now permanently registered in `HKEY_LOCAL_MACHINE` (system) or `HKEY_CURRENT_USER` (user)
  - Fixed issue where fonts would disappear after restarting the computer

### ✨ Improved
- Enhanced font name detection and registry entry creation
- Better error handling for registry operations
- More detailed installation feedback showing registry registration status
- Updated success messages to confirm persistence across reboots

### 🔧 Technical Changes
- Added `winreg` module import for Windows registry operations
- Implemented `get_font_name_from_file()` helper for proper font naming
- Enhanced `install_font_file()` method with registry registration
- Added registry key creation fallback for missing user font keys
- Improved error reporting for registry-related failures

### 📝 Documentation
- Updated README with font persistence information
- Added technical details about registry registration
- Created test script (`test_registry_fix.py`) to verify registry functionality

---

## [v1.0.0] - Initial Release

### ✨ Features
- Modern GUI for font installation from ZIP files
- Support for TTF, OTF, TTC, and OTC fonts
- Automatic system-wide and user-level installation fallback
- Real-time progress tracking
- Bulk font installation from multiple ZIP files
- Comprehensive error handling
- Standalone executable version