#!/usr/bin/env python3
"""
Create a test ZIP file with dummy font files for testing FontFlow.
This creates sample font files (not real fonts) to test the application functionality.
"""

import os
import zipfile
import tempfile
from pathlib import Path

def create_test_font_zip(output_path="test_fonts.zip"):
    """Create a test ZIP file with dummy font files."""
    
    # Sample font file content (not real fonts, just for testing)
    font_files = {
        "TestFont-Regular.ttf": b"TTF dummy content for testing - not a real font",
        "TestFont-Bold.ttf": b"TTF dummy content for testing - not a real font",
        "TestFont-Italic.otf": b"OTF dummy content for testing - not a real font",
        "TestFont-BoldItalic.otf": b"OTF dummy content for testing - not a real font",
        "readme.txt": b"This is a test font package created for testing FontFlow.\nThese are not real fonts and will not work as actual fonts.",
        "license.txt": b"Test License\nThis is a dummy license file for testing purposes only.",
        "subfolder/TestFont-Light.ttf": b"TTF dummy content in subfolder - not a real font"
    }
    
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path, content in font_files.items():
                zf.writestr(file_path, content)
                
        print(f"✓ Test ZIP file created: {output_path}")
        print(f"  Contains {len([f for f in font_files.keys() if f.endswith(('.ttf', '.otf'))])} dummy font files")
        print(f"  File size: {os.path.getsize(output_path)} bytes")
        print("\nNote: These are dummy files for testing only, not real fonts!")
        return True
        
    except Exception as e:
        print(f"✗ Error creating test ZIP: {e}")
        return False

def main():
    """Create test font ZIP file."""
    print("FontFlow - Test ZIP Creator")
    print("=" * 40)
    print("Creating a test ZIP file with dummy font files...")
    print()
    
    if create_test_font_zip():
        print()
        print("How to use this test file:")
        print("1. Run the FontFlow application")
        print("2. Select the 'test_fonts.zip' file")
        print("3. Click 'Install Fonts' to test the installation process")
        print()
        print("⚠️  Important: These are dummy files and will NOT work as real fonts!")
        print("   They are only for testing the application functionality.")
    else:
        print("Failed to create test ZIP file.")

if __name__ == "__main__":
    main()
