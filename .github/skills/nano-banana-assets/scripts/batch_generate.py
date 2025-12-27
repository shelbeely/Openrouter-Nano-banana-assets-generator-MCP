#!/usr/bin/env python3
"""
Batch asset generator with optional transparency support.

This script allows generating multiple assets at once from a JSON configuration file
or command-line list, with optional automatic transparency removal.

Usage:
    # From JSON config file
    python batch_generate.py --config assets_config.json
    
    # From command line
    python batch_generate.py --prompts "Icon 1" "Icon 2" "Icon 3" --transparent
    
    # From text file (one prompt per line)
    python batch_generate.py --file prompts.txt --aspect-ratio 1:1

Features:
    - Batch generation from multiple sources
    - Optional automatic transparency removal with rembg
    - Progress tracking and error handling
    - Organized output with custom naming
    - Resume capability for interrupted batches
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional
import time

# Import the asset generator classes
try:
    from generate_asset import AssetGenerator
except ImportError:
    print("Error: generate_asset.py not found in the same directory")
    sys.exit(1)

try:
    from generate_with_transparency import TransparentAssetGenerator
    TRANSPARENCY_AVAILABLE = True
except ImportError:
    TRANSPARENCY_AVAILABLE = False

try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False


class BatchAssetGenerator:
    """Handles batch generation of multiple assets"""
    
    def __init__(self, transparent: bool = False, output_dir: str = "batch_output"):
        self.transparent = transparent
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        if transparent and TRANSPARENCY_AVAILABLE:
            self.generator = TransparentAssetGenerator()
        else:
            self.generator = AssetGenerator()
            if transparent:
                print("⚠️  Transparency requested but generate_with_transparency.py not available")
                print("    Falling back to standard generation")
    
    def generate_from_config(self, config_path: str) -> Dict[str, any]:
        """Generate assets from a JSON configuration file"""
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assets = config.get('assets', [])
        results = {
            'total': len(assets),
            'successful': 0,
            'failed': 0,
            'errors': []
        }
        
        print(f"📋 Loaded {len(assets)} asset(s) from configuration")
        print(f"Output directory: {self.output_dir}")
        print("="*60)
        
        for i, asset_config in enumerate(assets, 1):
            print(f"\n[{i}/{len(assets)}] Processing: {asset_config.get('name', f'Asset {i}')}")
            
            try:
                self._generate_single_asset(asset_config, i)
                results['successful'] += 1
                print(f"✅ Success")
            except Exception as e:
                results['failed'] += 1
                error_msg = f"Asset {i}: {str(e)}"
                results['errors'].append(error_msg)
                print(f"❌ Failed: {e}")
            
            # Small delay between requests to be respectful
            if i < len(assets):
                time.sleep(2)
        
        return results
    
    def generate_from_prompts(
        self,
        prompts: List[str],
        aspect_ratio: str = "1:1",
        resolution: str = "1024x1024",
        color_palette: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """Generate assets from a list of prompts"""
        results = {
            'total': len(prompts),
            'successful': 0,
            'failed': 0,
            'errors': []
        }
        
        print(f"📋 Generating {len(prompts)} asset(s)")
        print(f"Aspect Ratio: {aspect_ratio}")
        print(f"Resolution: {resolution}")
        print(f"Transparent: {self.transparent}")
        print(f"Output directory: {self.output_dir}")
        print("="*60)
        
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}/{len(prompts)}] Generating: {prompt[:50]}...")
            
            try:
                asset_config = {
                    'name': f'asset_{i:03d}',
                    'prompt': prompt,
                    'aspect_ratio': aspect_ratio,
                    'resolution': resolution
                }
                if color_palette:
                    asset_config['color_palette'] = color_palette
                
                self._generate_single_asset(asset_config, i)
                results['successful'] += 1
                print(f"✅ Success")
            except Exception as e:
                results['failed'] += 1
                error_msg = f"Prompt {i}: {str(e)}"
                results['errors'].append(error_msg)
                print(f"❌ Failed: {e}")
            
            # Small delay between requests
            if i < len(prompts):
                time.sleep(2)
        
        return results
    
    def _generate_single_asset(self, config: Dict, index: int):
        """Generate a single asset based on configuration"""
        name = config.get('name', f'asset_{index:03d}')
        prompt = config['prompt']
        aspect_ratio = config.get('aspect_ratio', '1:1')
        resolution = config.get('resolution', '1024x1024')
        color_palette = config.get('color_palette')
        reference_images = config.get('reference_images')
        
        output_filename = str(self.output_dir / name)
        
        if self.transparent and TRANSPARENCY_AVAILABLE:
            # Use transparent generator
            self.generator.generate_with_transparency(
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                resolution=resolution,
                color_palette=color_palette,
                reference_images=reference_images,
                output_filename=output_filename
            )
        else:
            # Use standard generator
            response = self.generator.generate_asset(
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                resolution=resolution,
                color_palette=color_palette,
                reference_images=reference_images
            )
            
            # Save the response
            self.generator.save_images_from_response(response, output_filename)


def load_prompts_from_file(filepath: str) -> List[str]:
    """Load prompts from a text file (one per line)"""
    with open(filepath, 'r') as f:
        prompts = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return prompts


def main():
    parser = argparse.ArgumentParser(
        description='Batch generate assets with optional transparency',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From JSON config
  python batch_generate.py --config assets.json
  
  # From command-line prompts with transparency
  python batch_generate.py --prompts "Logo design" "Hero banner" --transparent
  
  # From text file
  python batch_generate.py --file prompts.txt --aspect-ratio 16:9 --resolution 1920x1080
  
  # With custom output directory and color palette
  python batch_generate.py --prompts "Icon 1" "Icon 2" -o icons --colors "#FF0000" "#00FF00"

Config JSON format:
  {
    "assets": [
      {
        "name": "hero_banner",
        "prompt": "Modern tech startup hero banner",
        "aspect_ratio": "16:9",
        "resolution": "1920x1080",
        "color_palette": ["#667EEA", "#764BA2"]
      }
    ]
  }
        """
    )
    
    # Input sources (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--config', '-c', help='JSON configuration file')
    input_group.add_argument('--prompts', '-p', nargs='+', help='List of prompts')
    input_group.add_argument('--file', '-f', help='Text file with prompts (one per line)')
    
    # Options
    parser.add_argument('--transparent', '-t', action='store_true',
                       help='Generate with transparent backgrounds (uses chroma key + rembg)')
    parser.add_argument('--aspect-ratio', '-a', default='1:1',
                       help='Aspect ratio (default: 1:1)')
    parser.add_argument('--resolution', '-r', default='1024x1024',
                       help='Resolution (default: 1024x1024)')
    parser.add_argument('--colors', nargs='+',
                       help='Color palette (hex codes)')
    parser.add_argument('--output', '-o', default='batch_output',
                       help='Output directory (default: batch_output)')
    
    args = parser.parse_args()
    
    # Check dependencies
    if args.transparent and not TRANSPARENCY_AVAILABLE:
        print("⚠️  Warning: Transparency requested but generate_with_transparency.py not found")
        print("    Will generate with standard backgrounds")
    
    if args.transparent and not REMBG_AVAILABLE:
        print("⚠️  Warning: rembg not installed. Install with: pip install rembg")
        print("    Transparency removal will not be automatic")
    
    # Initialize generator
    generator = BatchAssetGenerator(
        transparent=args.transparent,
        output_dir=args.output
    )
    
    # Generate assets based on input source
    try:
        if args.config:
            results = generator.generate_from_config(args.config)
        elif args.prompts:
            results = generator.generate_from_prompts(
                prompts=args.prompts,
                aspect_ratio=args.aspect_ratio,
                resolution=args.resolution,
                color_palette=args.colors
            )
        elif args.file:
            prompts = load_prompts_from_file(args.file)
            print(f"📄 Loaded {len(prompts)} prompt(s) from {args.file}")
            results = generator.generate_from_prompts(
                prompts=prompts,
                aspect_ratio=args.aspect_ratio,
                resolution=args.resolution,
                color_palette=args.colors
            )
        
        # Print summary
        print("\n" + "="*60)
        print("📊 BATCH GENERATION SUMMARY")
        print("="*60)
        print(f"Total: {results['total']}")
        print(f"✅ Successful: {results['successful']}")
        print(f"❌ Failed: {results['failed']}")
        
        if results['errors']:
            print("\nErrors:")
            for error in results['errors']:
                print(f"  - {error}")
        
        print(f"\n📁 Output location: {args.output}/")
        print("="*60)
        
        sys.exit(0 if results['failed'] == 0 else 1)
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
