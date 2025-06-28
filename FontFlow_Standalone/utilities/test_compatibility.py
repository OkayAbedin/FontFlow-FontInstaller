#!/usr/bin/env python3
"""
Test script for Font Installer
Quick verification that all components work correctly.
"""

import sys
import os
import zipfile
import tempfile
from pathlib import Path

def test_imports():
    """Test that all required modules can be imported."""
    try:
        import tkinter as tk
        from tkinter import ttk, filedialog, messagebox
        import shutil
        import ctypes
        import threading
        print("✓ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_windows_api():
    """Test Windows API access."""
    try:
        import ctypes
        gdi32 = ctypes.windll.gdi32
        user32 = ctypes.windll.user32
        print("✓ Windows API access successful")
        return True
    except Exception as e:
        print(f"✗ Windows API error: {e}")
        return False

def test_gui_creation():
    """Test GUI creation without showing window."""
    try:
        import tkinter as tk
        from tkinter import ttk
        
        root = tk.Tk()
        root.withdraw()  # Hide window
        
        # Test creating widgets
        frame = ttk.Frame(root)
        button = ttk.Button(frame, text="Test")
        listbox = tk.Listbox(frame)
        progress = ttk.Progressbar(frame)
        
        root.destroy()
        print("✓ GUI components created successfully")
        return True
    except Exception as e:
        print(f"✗ GUI creation error: {e}")
        return False

def create_test_zip():
    """Create a test ZIP file with a dummy font file."""
    try:
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as zip_file:
            zip_path = zip_file.name
            
        with zipfile.ZipFile(zip_path, 'w') as zf:
            # Create a dummy TTF file (not a real font, just for testing)
            zf.writestr('test_font.ttf', b'dummy font data')
            zf.writestr('readme.txt', b'This is a test font package')
            
        print(f"✓ Test ZIP file created: {zip_path}")
        return zip_path
    except Exception as e:
        print(f"✗ ZIP creation error: {e}")
        return None

def test_zip_extraction():
    """Test ZIP file extraction."""
    zip_path = create_test_zip()
    if not zip_path:
        return False
        
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                
            # Check if files were extracted
            extracted_files = list(Path(temp_dir).rglob('*'))
            font_files = [f for f in extracted_files if f.suffix.lower() in ['.ttf', '.otf']]
            
            if font_files:
                print(f"✓ ZIP extraction successful, found {len(font_files)} font files")
                success = True
            else:
                print("✗ No font files found after extraction")
                success = False
                
        # Cleanup
        os.unlink(zip_path)
        return success
        
    except Exception as e:
        print(f"✗ ZIP extraction error: {e}")
        if zip_path and os.path.exists(zip_path):
            os.unlink(zip_path)
        return False

def main():
    """Run all tests."""
    print("Font Installer - System Compatibility Test")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 6):
        print(f"✗ Python {sys.version} is too old. Python 3.6+ required.")
        return False
    else:
        print(f"✓ Python {sys.version} is compatible")
    
    # Check Windows
    if sys.platform != 'win32':
        print(f"✗ Platform {sys.platform} is not supported. Windows only.")
        return False
    else:
        print("✓ Running on Windows")
     
    # Run tests
    tests = [
        test_imports,
        test_windows_api,
        test_gui_creation,
        test_zip_extraction
    ]
    
    results = []
    for test in tests:
        results.append(test())
        
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 All tests passed! Font Installer should work correctly.")
        print("\nTo run the application:")
        print("  python font_installer.py")
        print("  or double-click: run_font_installer.bat")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        
    return all(results)

if __name__ == "__main__":
    main()
