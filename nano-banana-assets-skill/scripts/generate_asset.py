#!/usr/bin/env python3
"""
Python helper script for generating assets using OpenRouter API
More flexible than bash script with better JSON handling
"""

import os
import sys
import json
import base64
import requests
from typing import List, Optional, Dict, Any

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"


class AssetGenerator:
    """Helper class for generating assets with OpenRouter"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")
    
    def generate_asset(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        resolution: str = "1080x1080",
        reference_images: Optional[List[str]] = None,
        color_palette: Optional[List[str]] = None,
        logo_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate a single asset"""
        
        # Build comprehensive prompt
        full_prompt = f"""Generate a high-quality web asset with the following specifications:

Description: {prompt}
Aspect Ratio: {aspect_ratio}
Resolution: {resolution}
"""
        
        if color_palette:
            full_prompt += f"\nColor Palette: {', '.join(color_palette)}"
        
        if logo_file:
            full_prompt += "\nLogo: Incorporate the provided logo naturally into the design"
        
        full_prompt += """

Requirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance
- Follow web design best practices"""
        
        # Build content array
        content = []
        
        # Add reference images first
        if reference_images:
            for img in reference_images:
                content.append({
                    "type": "image_url",
                    "image_url": {"url": img}
                })
        
        # Add logo if provided
        if logo_file:
            content.append({
                "type": "image_url",
                "image_url": {"url": logo_file}
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
            "X-Title": "Nano Banana Assets Generator"
        }
        
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
    
    def generate_asset_pack(
        self,
        description: str,
        asset_types: List[str],
        brand_guidelines: Optional[str] = None,
        color_palette: Optional[List[str]] = None,
        reference_images: Optional[List[str]] = None,
        aspect_ratio: str = "1:1",
        resolution: str = "1080x1080"
    ) -> Dict[str, Any]:
        """Generate a pack of related assets"""
        
        # Build prompt
        prompt = f"""Generate a complete, brand-consistent asset pack for web development:

Project Description: {description}

Asset Types to Generate:
"""
        for i, asset_type in enumerate(asset_types, 1):
            prompt += f"{i}. {asset_type}\n"
        
        if brand_guidelines:
            prompt += f"\nBrand Guidelines:\n{brand_guidelines}\n"
        
        if color_palette:
            prompt += f"\nBrand Color Palette: {', '.join(color_palette)}"
        
        prompt += f"""

Default Aspect Ratio: {aspect_ratio}
Default Resolution: {resolution}

Requirements:
- All assets must maintain visual consistency
- Follow the brand guidelines strictly
- Use the provided color palette throughout
- Professional, production-ready quality
- Each asset should be optimized for its specific use case
- Cohesive design language across all assets
- Modern and contemporary style
- Web-optimized output"""
        
        # Build content array
        content = []
        
        if reference_images:
            for img in reference_images:
                content.append({
                    "type": "image_url",
                    "image_url": {"url": img}
                })
        
        content.append({
            "type": "text",
            "text": prompt
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
            "X-Title": "Nano Banana Assets Generator"
        }
        
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
    
    def edit_asset(
        self,
        source_image: str,
        edit_instructions: str,
        preserve_elements: Optional[List[str]] = None,
        aspect_ratio: Optional[str] = None,
        resolution: Optional[str] = None
    ) -> Dict[str, Any]:
        """Edit an existing asset"""
        
        prompt = f"""Edit the provided image with the following instructions:

Edit Instructions: {edit_instructions}
"""
        
        if preserve_elements:
            prompt += f"\nPreserve These Elements: {', '.join(preserve_elements)}"
        
        if aspect_ratio:
            prompt += f"\nTarget Aspect Ratio: {aspect_ratio}"
        
        if resolution:
            prompt += f"\nTarget Resolution: {resolution}"
        
        prompt += """

Editing Requirements:
- Apply edits precisely as instructed
- Maintain image quality and professional appearance
- Preserve specified elements without alteration
- Ensure smooth transitions and natural-looking results
- Output should be web-ready and optimized"""
        
        # Build content array with source image
        content = [
            {
                "type": "image_url",
                "image_url": {"url": source_image}
            },
            {
                "type": "text",
                "text": prompt
            }
        ]
        
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
            "temperature": 0.7,
            "max_tokens": 4096
        }
        
        if aspect_ratio:
            payload["image_config"] = {"aspect_ratio": aspect_ratio}
        
        # Make API call
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
            "X-Title": "Nano Banana Assets Generator"
        }
        
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
    
    def save_images_from_response(self, response: Dict[str, Any], base_filename: str = "asset"):
        """Extract and save images from API response"""
        try:
            images = response["choices"][0]["message"]["images"]
            saved_files = []
            
            for i, img in enumerate(images):
                # Get base64 data URL
                data_url = img.get("image_url", {}).get("url", img.get("url", ""))
                
                if not data_url:
                    continue
                
                # Extract base64 data (remove data:image/png;base64, prefix)
                if "base64," in data_url:
                    base64_data = data_url.split("base64,")[1]
                    
                    # Save to file
                    filename = f"{base_filename}_{i+1}.png"
                    with open(filename, "wb") as f:
                        f.write(base64.b64decode(base64_data))
                    
                    saved_files.append(filename)
                    print(f"Saved: {filename}")
            
            return saved_files
        except Exception as e:
            print(f"Error saving images: {e}")
            return []


def main():
    """Command-line interface"""
    if len(sys.argv) < 2:
        print("Usage: python generate_asset.py <prompt> [aspect_ratio] [resolution]")
        print("Example: python generate_asset.py 'Modern hero banner' '16:9' '1920x1080'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    aspect_ratio = sys.argv[2] if len(sys.argv) > 2 else "1:1"
    resolution = sys.argv[3] if len(sys.argv) > 3 else "1080x1080"
    
    try:
        generator = AssetGenerator()
        
        print(f"Generating asset...")
        print(f"Prompt: {prompt}")
        print(f"Aspect Ratio: {aspect_ratio}")
        print(f"Resolution: {resolution}")
        print()
        
        response = generator.generate_asset(prompt, aspect_ratio, resolution)
        
        # Save response
        with open("response.json", "w") as f:
            json.dump(response, f, indent=2)
        print("Response saved to response.json")
        
        # Extract text content
        text_content = response["choices"][0]["message"].get("content", "")
        if text_content:
            print(f"\nDescription:\n{text_content}")
        
        # Save images
        print("\nExtracting images...")
        saved_files = generator.save_images_from_response(response)
        
        if saved_files:
            print(f"\n✅ Successfully generated {len(saved_files)} image(s)")
        else:
            print("\n⚠️  No images were generated")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
