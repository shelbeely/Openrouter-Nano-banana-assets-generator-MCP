#!/usr/bin/env python3
"""
Process logo image to remove background using rembg
"""
import sys
from pathlib import Path
from rembg import remove
from PIL import Image

def process_logo(input_path: str, output_path: str):
    """Remove background from image and save with transparency"""
    print(f"Processing image: {input_path}")
    
    # Open the input image
    input_image = Image.open(input_path)
    
    # Remove the background
    print("Removing background...")
    output_image = remove(input_image)
    
    # Save the output image with transparency
    print(f"Saving processed image to: {output_path}")
    output_image.save(output_path, format='PNG')
    
    print(f"✅ Successfully processed logo!")
    print(f"   Input: {input_path}")
    print(f"   Output: {output_path}")
    print(f"   Size: {output_image.size}")

if __name__ == "__main__":
    # Define paths
    repo_root = Path(__file__).parent
    input_path = repo_root / "assets/generated/download (20).jpeg"
    output_path = repo_root / "assets/generated/logo_transparent.png"
    
    # Process the logo
    process_logo(str(input_path), str(output_path))
