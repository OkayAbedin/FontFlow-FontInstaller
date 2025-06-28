#!/usr/bin/env python3
"""
Test script to verify font directory access and permissions.
"""

import os
import tempfile
import shutil

def test_font_directories():
    """Test various font directory locations for write access."""
    print("Font Directory Access Test")
    print("=" * 40)
    
    # Test directories in order of preference
    test_dirs = [
        ("System Fonts (Admin)", os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')),
        ("User Fonts (Primary)", os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Microsoft', 'Windows', 'Fonts')),
        ("User Fonts (Alt)", os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Fonts')),
        ("Documents/Fonts", os.path.join(os.path.expanduser('~'), 'Documents', 'Fonts')),
        ("Temp/UserFonts", os.path.join(tempfile.gettempdir(), 'UserFonts')),
    ]
    
    working_dirs = []
    
    for name, directory in test_dirs:
        try:
            # Try to create directory
            os.makedirs(directory, exist_ok=True)
            
            # Test write access
            test_file = os.path.join(directory, 'test_write_permissions.tmp')
            with open(test_file, 'w') as f:
                f.write('test')
            
            # Clean up test file
            os.remove(test_file)
            
            print(f"✅ {name}: {directory}")
            working_dirs.append((name, directory))
            
        except PermissionError:
            print(f"❌ {name}: Permission denied - {directory}")
        except Exception as e:
            print(f"❌ {name}: Error - {directory} ({str(e)})")
    
    print("\n" + "=" * 40)
    if working_dirs:
        print(f"✅ Found {len(working_dirs)} accessible font directories!")
        print("Font installation should work with the following locations:")
        for name, directory in working_dirs:
            print(f"   • {name}: {directory}")
    else:
        print("❌ No accessible font directories found!")
        print("This may indicate a permission issue with your user account.")
    
    return len(working_dirs) > 0

def main():
    """Run the directory access test."""
    success = test_font_directories()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 Font installation should work!")
        print("You can run FontFlow with confidence.")
    else:
        print("⚠️  Font installation may have issues.")
        print("Try running as Administrator or contact your system administrator.")

if __name__ == "__main__":
    main()
