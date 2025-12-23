#!/usr/bin/env python3
"""
Post-process existing images to remove backgrounds.

This utility script helps remove backgrounds from already-generated images,
either with chroma key removal or AI-powered rembg.

Usage:
    # Process single file with rembg (AI-powered)
    python remove_backgrounds.py image.png
    
    # Process multiple files
    python remove_backgrounds.py image1.png image2.png image3.png
    
    # Process all PNG files in a directory
    python remove_backgrounds.py --directory ./images/
    
    # Use chroma key removal instead of rembg
    python remove_backgrounds.py --chroma-key "#00FF00" image.png
    
    # Batch with custom output directory
    python remove_backgrounds.py --directory ./input/ --output ./transparent/

Requirements:
    pip install rembg Pillow
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional

try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class BackgroundRemover:
    """Handles background removal from images"""
    
    def __init__(self, output_dir: Optional[str] = None, chroma_key: Optional[str] = None):
        self.output_dir = Path(output_dir) if output_dir else None
        self.chroma_key = chroma_key
        
        if self.output_dir:
            self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def process_file(self, input_path: str) -> bool:
        """Process a single image file"""
        input_path = Path(input_path)
        
        if not input_path.exists():
            print(f"❌ File not found: {input_path}")
            return False
        
        # Determine output path
        if self.output_dir:
            output_path = self.output_dir / f"{input_path.stem}_transparent{input_path.suffix}"
        else:
            output_path = input_path.parent / f"{input_path.stem}_transparent{input_path.suffix}"
        
        print(f"Processing: {input_path.name}")
        
        try:
            if self.chroma_key:
                # Use chroma key removal
                self._remove_chroma_key(input_path, output_path)
            elif REMBG_AVAILABLE:
                # Use rembg (AI-powered)
                self._remove_with_rembg(input_path, output_path)
            else:
                print("❌ Neither rembg nor PIL available for processing")
                return False
            
            print(f"✅ Saved: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error processing {input_path.name}: {e}")
            return False
    
    def _remove_with_rembg(self, input_path: Path, output_path: Path):
        """Remove background using rembg (AI-powered)"""
        with open(input_path, 'rb') as f:
            input_data = f.read()
        
        output_data = remove(input_data)
        
        with open(output_path, 'wb') as f:
            f.write(output_data)
    
    def _remove_chroma_key(self, input_path: Path, output_path: Path):
        """Remove chroma key color using PIL"""
        if not PIL_AVAILABLE:
            raise ImportError("PIL/Pillow required for chroma key removal: pip install Pillow")
        
        # Open image
        img = Image.open(input_path).convert('RGBA')
        
        # Parse chroma key color
        chroma = self.chroma_key.lstrip('#')
        if len(chroma) == 6:
            r, g, b = int(chroma[0:2], 16), int(chroma[2:4], 16), int(chroma[4:6], 16)
        else:
            raise ValueError(f"Invalid hex color: {self.chroma_key}")
        
        # Get pixel data
        pixels = img.load()
        width, height = img.size
        
        # Tolerance for color matching (adjust as needed)
        tolerance = 30
        
        # Make chroma key pixels transparent
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                # Check if pixel is close to chroma key color
                if (abs(pixel[0] - r) < tolerance and
                    abs(pixel[1] - g) < tolerance and
                    abs(pixel[2] - b) < tolerance):
                    # Make transparent
                    pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0)
        
        # Save with transparency
        img.save(output_path, 'PNG')
    
    def process_directory(self, directory: str, recursive: bool = False) -> dict:
        """Process all PNG files in a directory"""
        directory = Path(directory)
        
        if not directory.exists():
            print(f"❌ Directory not found: {directory}")
            return {'total': 0, 'successful': 0, 'failed': 0}
        
        # Find PNG files
        if recursive:
            png_files = list(directory.rglob('*.png'))
        else:
            png_files = list(directory.glob('*.png'))
        
        # Filter out already processed files
        png_files = [f for f in png_files if '_transparent' not in f.stem]
        
        results = {
            'total': len(png_files),
            'successful': 0,
            'failed': 0
        }
        
        print(f"Found {len(png_files)} PNG file(s) in {directory}")
        print("="*60)
        
        for i, png_file in enumerate(png_files, 1):
            print(f"\n[{i}/{len(png_files)}]", end=" ")
            if self.process_file(png_file):
                results['successful'] += 1
            else:
                results['failed'] += 1
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description='Remove backgrounds from images using rembg or chroma key',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single file with rembg (AI-powered)
  python remove_backgrounds.py my_image.png
  
  # Multiple files
  python remove_backgrounds.py img1.png img2.png img3.png
  
  # All PNG files in directory
  python remove_backgrounds.py --directory ./images/
  
  # With chroma key removal (for #00FF00 green backgrounds)
  python remove_backgrounds.py --chroma-key "#00FF00" image.png
  
  # Recursive directory processing with custom output
  python remove_backgrounds.py -d ./input/ -o ./output/ --recursive
        """
    )
    
    parser.add_argument('files', nargs='*', help='Image files to process')
    parser.add_argument('--directory', '-d', help='Process all PNG files in directory')
    parser.add_argument('--output', '-o', help='Output directory (default: same as input)')
    parser.add_argument('--chroma-key', '-c', 
                       help='Use chroma key removal with specified color (e.g., "#00FF00")')
    parser.add_argument('--recursive', '-r', action='store_true',
                       help='Process directories recursively')
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.files and not args.directory:
        parser.error("Provide either files or --directory")
    
    # Check dependencies
    if not args.chroma_key and not REMBG_AVAILABLE:
        print("❌ Error: rembg not installed")
        print("   Install with: pip install rembg")
        print("   Or use --chroma-key for manual color removal")
        sys.exit(1)
    
    if args.chroma_key and not PIL_AVAILABLE:
        print("❌ Error: Pillow not installed")
        print("   Install with: pip install Pillow")
        sys.exit(1)
    
    # Initialize remover
    remover = BackgroundRemover(
        output_dir=args.output,
        chroma_key=args.chroma_key
    )
    
    # Process files or directory
    try:
        if args.directory:
            results = remover.process_directory(args.directory, args.recursive)
            
            # Print summary
            print("\n" + "="*60)
            print("📊 PROCESSING SUMMARY")
            print("="*60)
            print(f"Total: {results['total']}")
            print(f"✅ Successful: {results['successful']}")
            print(f"❌ Failed: {results['failed']}")
            
            if args.output:
                print(f"\n📁 Output: {args.output}/")
            else:
                print(f"\n📁 Output: Same directory as input (with '_transparent' suffix)")
            
            sys.exit(0 if results['failed'] == 0 else 1)
        else:
            # Process individual files
            successful = 0
            failed = 0
            
            for filepath in args.files:
                if remover.process_file(filepath):
                    successful += 1
                else:
                    failed += 1
            
            print(f"\n✅ Successful: {successful}/{len(args.files)}")
            if failed > 0:
                print(f"❌ Failed: {failed}/{len(args.files)}")
            
            sys.exit(0 if failed == 0 else 1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
