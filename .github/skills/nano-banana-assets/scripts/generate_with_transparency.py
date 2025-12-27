#!/usr/bin/env python3
"""
Automated script for generating assets with transparent backgrounds.

This script automatically:
1. Generates images with #00FF00 chroma key backgrounds (avoiding fake checkered patterns)
2. Removes the background using rembg (AI-powered)
3. Outputs transparent RGBA PNG files

Usage:
    python generate_with_transparency.py "Your prompt here" [aspect_ratio] [resolution]

Example:
    python generate_with_transparency.py "Kawaii raccoon sticker waving" "1:1" "1024x1024"

Requirements:
    pip install rembg requests
"""

import os
import sys
import json
import base64
import requests
from typing import List, Optional, Dict, Any
from pathlib import Path

# Check if rembg is available
try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False
    print("⚠️  Warning: rembg not installed. Install with: pip install rembg")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"
CHROMA_KEY_COLOR = "#00FF00"  # Bright green for clean removal


class TransparentAssetGenerator:
    """Generator that creates assets with transparent backgrounds"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")
    
    def generate_with_transparency(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        resolution: str = "1024x1024",
        reference_images: Optional[List[str]] = None,
        color_palette: Optional[List[str]] = None,
        output_filename: str = "transparent_asset"
    ) -> Dict[str, Any]:
        """
        Generate an asset with transparent background.
        
        This automatically:
        1. Adds chroma key background to prompt
        2. Generates with OpenRouter
        3. Removes background with rembg
        4. Saves transparent PNG
        """
        
        # Build prompt with chroma key background
        full_prompt = f"""Generate a high-quality asset with the following specifications:

Description: {prompt}

Subject: {prompt}
Composition: Centered, optimized for use as a standalone asset
Action: [Based on prompt description]
Location: Isolated on solid bright green ({CHROMA_KEY_COLOR}) chroma key background
Style: Professional, polished, production-ready
Lighting: Even, soft lighting to minimize shadows on background

Technical Specifications:
- Aspect Ratio: {aspect_ratio}
- Resolution: {resolution}
- Background: Solid bright green ({CHROMA_KEY_COLOR}) for chroma key removal
- No text, no borders, no drop shadows on background
"""
        
        if color_palette:
            full_prompt += f"\nColor Palette for Subject: {', '.join(color_palette)}"
        
        full_prompt += f"""

IMPORTANT: The background MUST be solid bright green ({CHROMA_KEY_COLOR}) only.
This is a chroma key background for automated removal - DO NOT paint checkered patterns.
The subject should be cleanly isolated on the green background.

Requirements:
- Professional, web-ready quality
- Clean separation between subject and background
- Solid {CHROMA_KEY_COLOR} background (no gradients, no patterns)
- Subject positioned clearly on green background"""
        
        # Build content array
        content = []
        
        # Add reference images if provided
        if reference_images:
            for img in reference_images:
                content.append({
                    "type": "image_url",
                    "image_url": {"url": img}
                })
        
        # Add text prompt
        content.append({
            "type": "text",
            "text": full_prompt
        })
        
        # Build request payload
        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "modalities": ["image", "text"],
            "image_config": {
                "aspect_ratio": aspect_ratio
            },
            "temperature": 0.7,
            "max_tokens": 4096
        }
        
        # Make API call
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
            "X-Title": "Nano Banana Transparent Asset Generator"
        }
        
        print(f"🎨 Generating asset with chroma key background ({CHROMA_KEY_COLOR})...")
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        
        result = response.json()
        
        # Extract and process images
        print("✅ Generation complete!")
        
        if REMBG_AVAILABLE:
            print("🔄 Removing background with rembg...")
            self._process_and_save_with_rembg(result, output_filename)
        else:
            print("💾 Saving with green background (rembg not available)...")
            self._save_without_rembg(result, output_filename)
            print(f"\n💡 To remove background, install rembg: pip install rembg")
            print(f"   Or use ImageMagick: convert {output_filename}_1.png -fuzz 5% -transparent '{CHROMA_KEY_COLOR}' transparent.png")
        
        return result
    
    def _process_and_save_with_rembg(self, response: Dict[str, Any], base_filename: str):
        """Process images with rembg to remove background"""
        try:
            images = response["choices"][0]["message"]["images"]
            
            for i, img in enumerate(images):
                # Get base64 data
                data_url = img.get("image_url", {}).get("url", img.get("url", ""))
                
                if not data_url or "base64," not in data_url:
                    continue
                
                # Decode base64
                base64_data = data_url.split("base64,")[1]
                image_bytes = base64.b64decode(base64_data)
                
                # Remove background with rembg
                output_bytes = remove(image_bytes)
                
                # Save transparent PNG
                filename = f"{base_filename}_{i+1}_transparent.png"
                with open(filename, "wb") as f:
                    f.write(output_bytes)
                
                print(f"✅ Saved transparent: {filename}")
                
                # Also save original with green background for reference
                original_filename = f"{base_filename}_{i+1}_original_green.png"
                with open(original_filename, "wb") as f:
                    f.write(image_bytes)
                print(f"📁 Original with green bg: {original_filename}")
            
            print(f"\n🎉 Success! Generated {len(images)} transparent asset(s)")
            
        except Exception as e:
            print(f"❌ Error processing images: {e}")
            print("Falling back to saving with green background...")
            self._save_without_rembg(response, base_filename)
    
    def _save_without_rembg(self, response: Dict[str, Any], base_filename: str):
        """Save images without background removal"""
        try:
            images = response["choices"][0]["message"]["images"]
            
            for i, img in enumerate(images):
                data_url = img.get("image_url", {}).get("url", img.get("url", ""))
                
                if not data_url or "base64," not in data_url:
                    continue
                
                base64_data = data_url.split("base64,")[1]
                filename = f"{base_filename}_{i+1}_green_bg.png"
                
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(base64_data))
                
                print(f"💾 Saved: {filename}")
            
        except Exception as e:
            print(f"❌ Error saving images: {e}")


def main():
    """Command-line interface"""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage: python generate_with_transparency.py <prompt> [aspect_ratio] [resolution]")
        print("Example: python generate_with_transparency.py 'Kawaii raccoon sticker' '1:1' '1024x1024'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    aspect_ratio = sys.argv[2] if len(sys.argv) > 2 else "1:1"
    resolution = sys.argv[3] if len(sys.argv) > 3 else "1024x1024"
    
    print("="*60)
    print("🎨 Transparent Asset Generator")
    print("="*60)
    print(f"Prompt: {prompt}")
    print(f"Aspect Ratio: {aspect_ratio}")
    print(f"Resolution: {resolution}")
    print(f"Chroma Key: {CHROMA_KEY_COLOR}")
    print(f"Background Removal: {'rembg (AI-powered)' if REMBG_AVAILABLE else 'Manual (rembg not installed)'}")
    print("="*60)
    print()
    
    try:
        generator = TransparentAssetGenerator()
        result = generator.generate_with_transparency(
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_filename="asset"
        )
        
        # Save response JSON for debugging
        with open("response.json", "w") as f:
            json.dump(result, f, indent=2)
        
        print("\n" + "="*60)
        print("✅ Complete! Check the generated files above.")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
