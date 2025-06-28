#!/usr/bin/env python3
"""
Convert PNG icon to ICO format for better Windows compatibility.
"""

from PIL import Image
import os

def convert_png_to_ico():
    """Convert icon.png to icon.ico"""
    if not os.path.exists("icon.png"):
        print("❌ icon.png not found!")
        return False
    
    try:
        # Open PNG image
        img = Image.open("icon.png")
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create multiple sizes for ICO (Windows standard sizes)
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # Resize to multiple sizes and save as ICO
        img.save("icon.ico", format='ICO', sizes=sizes)
        
        print("✓ Successfully converted icon.png to icon.ico")
        print("  Created with sizes: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256")
        return True
        
    except Exception as e:
        print(f"❌ Error converting icon: {e}")
        return False

if __name__ == "__main__":
    print("FontFlow - Icon Converter")
    print("=" * 30)
    convert_png_to_ico()
