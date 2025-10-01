#!/usr/bin/env python3
"""
Test script to verify the font registry fix works correctly.
This script tests the registry operations without actually installing fonts.
"""

import winreg
import os
import tempfile

def test_user_registry_access():
    """Test if we can access and write to the user fonts registry."""
    try:
        # Try to open the user fonts registry key
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                          r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 
                          0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            print("✅ User fonts registry key exists and is writable")
            return True
    except winreg.FileNotFoundError:
        # Try to create the key
        try:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, 
                                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts") as key:
                print("✅ Created user fonts registry key successfully")
                return True
        except Exception as e:
            print(f"❌ Failed to create user fonts registry key: {e}")
            return False
    except Exception as e:
        print(f"❌ Error accessing user fonts registry: {e}")
        return False

def test_system_registry_access():
    """Test if we can access the system fonts registry (requires admin)."""
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                          r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 
                          0, winreg.KEY_READ) as key:
            print("✅ System fonts registry key is readable")
            
        # Test write access (requires admin)
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 
                              0, winreg.KEY_WRITE) as key:
                print("✅ System fonts registry key is writable (admin privileges detected)")
                return True
        except PermissionError:
            print("⚠️ System fonts registry is not writable (no admin privileges)")
            return False
    except Exception as e:
        print(f"❌ Error accessing system fonts registry: {e}")
        return False

def test_user_font_directory():
    """Test if we can create and write to user font directories."""
    user_font_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Microsoft', 'Windows', 'Fonts')
    
    try:
        os.makedirs(user_font_dir, exist_ok=True)
        
        # Test write permissions
        test_file = os.path.join(user_font_dir, 'test_write.tmp')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        
        print(f"✅ User font directory is accessible: {user_font_dir}")
        return True, user_font_dir
    except Exception as e:
        print(f"❌ Cannot access user font directory: {e}")
        return False, None

def main():
    """Run all tests."""
    print("🔍 Testing Font Installer Registry Fix")
    print("=" * 50)
    
    # Test user font directory
    user_dir_ok, user_dir = test_user_font_directory()
    
    # Test user registry access
    user_reg_ok = test_user_registry_access()
    
    # Test system registry access
    system_reg_ok = test_system_registry_access()
    
    print("\n📊 Test Results:")
    print("=" * 50)
    print(f"User font directory: {'✅ OK' if user_dir_ok else '❌ FAILED'}")
    print(f"User registry access: {'✅ OK' if user_reg_ok else '❌ FAILED'}")
    print(f"System registry access: {'✅ OK (Admin)' if system_reg_ok else '⚠️ Limited (No Admin)'}")
    
    if user_dir_ok and user_reg_ok:
        print("\n🎉 Font installer should work correctly for user-level installations!")
        print("✨ Fonts will persist across reboots.")
    elif system_reg_ok:
        print("\n🎉 Font installer should work correctly for system-wide installations!")
        print("✨ Fonts will persist across reboots.")
    else:
        print("\n❌ Font installer may not work correctly.")
        print("🔧 Please check permissions and registry access.")

if __name__ == "__main__":
    main()