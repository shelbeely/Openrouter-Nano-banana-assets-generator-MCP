#!/usr/bin/env python3
"""
Generate assets using ACTUAL OpenTransition website images as visual references
This ensures we match the exact style instead of interpreting it wrong
"""
import sys
import os
import base64
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, call_openrouter, save_generated_images, Path
)

def image_to_base64_url(image_path: str) -> str:
    """Convert image file to base64 data URL"""
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    ext = Path(image_path).suffix.lower()
    mime_type = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
    }.get(ext, 'image/png')
    
    return f"data:{mime_type};base64,{image_data}"

def regenerate_with_actual_references():
    """Use ACTUAL OpenTransition images as references for accurate matching"""
    
    if not OPENROUTER_API_KEY:
        print("❌ ERROR: OPENROUTER_API_KEY environment variable not set")
        sys.exit(1)
    
    repo_root = Path(__file__).parent
    logo_path = repo_root / "assets/generated/logo_transparent.png"
    output_dir = repo_root / "assets/generated/asset_pack"
    output_dir.mkdir(exist_ok=True)
    
    # Load OpenTransition reference images
    ref_dir = repo_root / "opentransition_references"
    og_image = ref_dir / "og-image.png"
    section_bg = ref_dir / "section-background.png"
    
    print("📦 Loading reference images...")
    logo_base64 = image_to_base64_url(str(logo_path))
    og_image_base64 = image_to_base64_url(str(og_image))
    section_bg_base64 = image_to_base64_url(str(section_bg))
    print(f"✅ Loaded: logo, og-image.png (style reference), section-background.png (shapes reference)\n")
    
    # Simple, direct prompts that rely on visual references
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create a hero banner (1920x1080) that matches the EXACT visual style of the reference images:

- Use the EXACT color palette from og-image.png: warm orange (#E68322), peachy cream backgrounds, golden yellow accents
- Copy the butterfly style from og-image.png: orange/yellow butterflies (NOT rainbow)
- Copy the organic shapes from section-background.png: soft teardrop shapes in peachy tones
- Copy the sparkle style: four-pointed stars in golden yellow
- Use the flat illustration style shown in og-image.png
- Include the logo (first reference image) prominently in center
- Match the warm, cohesive aesthetic - NO rainbow, keep it warm orange/peach like the references

Create a wide hero banner using these EXACT visual elements and color scheme."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create Instagram post (1080x1080) matching EXACT style of reference images:

- EXACT colors from og-image.png: warm orange, peachy backgrounds
- Butterflies: orange/yellow like in og-image.png (NOT rainbow)
- Organic shapes: peachy teardrops from section-background.png  
- Sparkles: golden yellow four-pointed stars
- Flat illustration style from og-image.png
- Logo centered
- Square format, warm cohesive aesthetic like references"""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create Instagram story (1080x1920) matching EXACT style of reference images:

- Colors: warm orange & peachy cream from og-image.png
- Butterflies: orange/yellow style from og-image.png
- Shapes: peachy teardrops from section-background.png
- Vertical format, logo visible, warm aesthetic matching references"""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create Facebook cover (ultra-wide) matching EXACT style of reference images:

- Colors: warm orange & peachy from og-image.png
- Butterflies: orange/yellow from og-image.png  
- Shapes: peachy teardrops from section-background.png
- Wide format, logo visible, warm cohesive aesthetic"""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64],
            "prompt": """Create Twitter header (21:9, crop to 3:1) matching EXACT style of reference images:

- Colors & style from og-image.png: warm orange, peachy backgrounds
- Butterflies: orange/yellow like references
- Logo positioned right-of-center
- Warm aesthetic matching og-image.png"""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64],
            "prompt": """Create LinkedIn banner (21:9, crop to 4:1) matching EXACT style of reference images:

- Professional but using og-image.png color palette: warm orange, peachy tones
- Subtle butterflies in orange/yellow
- Logo positioned right
- Warm professional aesthetic"""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "references": [logo_base64, section_bg_base64],
            "prompt": """Create profile picture (1024x1024, circular-safe) matching EXACT style of reference images:

- Background: peachy cream tones from section-background.png
- Logo centered
- Simple, warm aesthetic
- Circular-safe design"""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "references": [logo_base64, og_image_base64],
            "prompt": """Create app icon (1024x1024) matching EXACT style of reference images:

- Background: warm peachy gradient from og-image.png color palette
- Logo simplified and centered
- Simple, clear at small sizes
- Warm orange/peach tones only"""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create app splash screen (1080x1920) matching EXACT style of reference images:

- Colors & style from og-image.png: warm orange, peachy backgrounds
- Shapes from section-background.png: peachy teardrops
- Butterflies: orange/yellow from og-image.png
- Logo centered
- Warm welcoming aesthetic"""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": """Create community banner (1920x1080) matching EXACT style of reference images:

- Full style from og-image.png: warm orange, peachy backgrounds, orange/yellow butterflies
- Organic shapes from section-background.png
- More butterflies and connecting elements showing community
- Logo visible
- Warm cohesive aesthetic matching references exactly"""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} using ACTUAL OpenTransition images as references...\n")
    print("🎨 Method: Providing actual website images to AI for visual matching\n")
    print("  ✓ og-image.png → color palette, butterfly style, flat illustration\n")
    print("  ✓ section-background.png → organic shape style\n")
    print("  ✓ logo_transparent.png → brand logo integration\n")
    
    all_generated_files = []
    
    for idx, asset in enumerate(assets, 1):
        print(f"[{idx}/{len(assets)}] Generating {asset['name']}...")
        print(f"   Aspect Ratio: {asset['aspect_ratio']}")
        print(f"   References: {len(asset['references'])} images")
        
        try:
            # Build content with multiple reference images
            content = []
            for ref in asset['references']:
                content.append({
                    "type": "image_url",
                    "image_url": {"url": ref}
                })
            content.append({
                "type": "text",
                "text": asset['prompt']
            })
            
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
                "X-Title": "Nano Banana Assets Generator"
            }
            
            payload = {
                "model": "google/gemini-3-pro-image-preview",
                "messages": [{
                    "role": "user",
                    "content": content
                }],
                "modalities": ["image", "text"],
                "image_config": {"aspect_ratio": asset['aspect_ratio']},
                "temperature": 0.7,
                "max_tokens": 4096
            }
            
            import requests
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code != 200:
                raise Exception(f"API Error: {response.status_code} - {response.text}")
            
            saved_files = save_generated_images(response.json(), asset['name'], output_dir)
            all_generated_files.extend(saved_files)
            
            print(f"   ✅ Completed {asset['name']}\n")
            
        except Exception as e:
            print(f"   ❌ Error generating {asset['name']}: {str(e)}\n")
            continue
    
    print(f"\n{'='*70}")
    print(f"✅ Assets Generated Using Actual Reference Images!")
    print(f"{'='*70}")
    print(f"Total: {len(all_generated_files)} assets")
    print(f"\nMethod: Used actual OpenTransition website images as visual references")
    print(f"Result: Should match website style exactly (not interpreted)")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    regenerate_with_actual_references()
