#!/usr/bin/env python3
"""
Regenerate assets with CONSISTENT LOGO across all images
The logo is ONLY the butterfly in circle - no text is part of the logo
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

def regenerate_with_consistent_logo():
    """Regenerate with EXACT same logo across all assets"""
    
    if not OPENROUTER_API_KEY:
        print("❌ ERROR: OPENROUTER_API_KEY environment variable not set")
        sys.exit(1)
    
    repo_root = Path(__file__).parent
    logo_path = repo_root / "assets/generated/logo_transparent.png"
    output_dir = repo_root / "assets/generated/asset_pack"
    output_dir.mkdir(exist_ok=True)
    
    # Load reference images
    ref_dir = repo_root / "opentransition_references"
    og_image = ref_dir / "og-image.png"
    section_bg = ref_dir / "section-background.png"
    
    print("📦 Loading reference images...")
    logo_base64 = image_to_base64_url(str(logo_path))
    og_image_base64 = image_to_base64_url(str(og_image))
    section_bg_base64 = image_to_base64_url(str(section_bg))
    print(f"✅ Loaded references\n")
    
    # Critical instruction about logo
    logo_instruction = """
CRITICAL LOGO REQUIREMENT:
The first reference image is the EXACT logo. It is ONLY a butterfly in a circle with a sparkle.
- DO NOT add "OpenTransition" text to the logo
- DO NOT modify the logo in any way
- Use this EXACT logo design consistently across ALL assets
- The logo must look IDENTICAL in every asset
- Text "OpenTransition" should be SEPARATE from the logo, not part of it
- Keep the butterfly, circle, and sparkle exactly as shown in the reference
"""
    
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create hero banner (1920x1080) matching OpenTransition website style:

Logo Placement:
- Place the EXACT logo (butterfly in circle with sparkle) from first reference
- Position it prominently - do NOT modify it or add text to it
- The text "OpenTransition" should be SEPARATE, next to the logo (not part of the logo itself)
- Logo must be IDENTICAL to the reference image

Style from references:
- Warm orange (#E68322) color scheme
- Orange/yellow butterflies (NOT rainbow)  
- Peachy cream gradients
- Organic teardrop shapes (from section-background.png)
- Golden yellow sparkles
- Flat illustration style (from og-image.png)

REMEMBER: Logo stays exactly as provided - just butterfly circle with sparkle. No modifications."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create Instagram post (1080x1080) with CONSISTENT logo:

Logo: Use EXACT logo from first reference (butterfly in circle) - do NOT modify
Style: Match og-image.png colors (warm orange, peachy backgrounds)
Elements: Orange butterflies, peachy teardrops, golden sparkles

Text "OpenTransition" separate from logo, not part of it."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create Instagram story (1080x1920) with CONSISTENT logo:

Logo: EXACT butterfly circle from reference - unchanged
Style: OpenTransition warm orange/peachy aesthetic
Layout: Vertical format

Logo must be IDENTICAL to reference image."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create Facebook cover with CONSISTENT logo:

Logo: EXACT butterfly circle with sparkle - no modifications
Style: OpenTransition colors and elements
Format: Ultra-wide

Logo consistency is critical."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64],
            "prompt": f"""{logo_instruction}

Create Twitter header with CONSISTENT logo:

Logo: Use EXACT butterfly circle from reference
Style: OpenTransition warm aesthetic
Position: Logo right-of-center

Same logo as all other assets."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "references": [logo_base64, og_image_base64],
            "prompt": f"""{logo_instruction}

Create LinkedIn banner with CONSISTENT logo:

Logo: EXACT butterfly circle - no text added
Style: Professional OpenTransition aesthetic
Position: Logo positioned right

Logo must match all other assets exactly."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "references": [logo_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create profile picture (1024x1024) with CONSISTENT logo:

Logo: EXACT butterfly circle from reference - centered
Background: Peachy cream from section-background.png
Design: Circular-safe

Logo is just butterfly circle with sparkle - nothing added."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "references": [logo_base64, og_image_base64],
            "prompt": f"""{logo_instruction}

Create app icon (1024x1024) with CONSISTENT logo:

Logo: EXACT butterfly circle from reference - simplified if needed but same design
Background: Warm peachy gradient
Size: Clear at small sizes

Logo must be recognizably the SAME across all assets."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create app splash (1080x1920) with CONSISTENT logo:

Logo: EXACT butterfly circle - centered
Style: OpenTransition warm welcoming aesthetic
Elements: Orange butterflies, peachy shapes, golden sparkles

Logo consistency critical - same design as all assets."""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "references": [logo_base64, og_image_base64, section_bg_base64],
            "prompt": f"""{logo_instruction}

Create community banner (1920x1080) with CONSISTENT logo:

Logo: EXACT butterfly circle from reference
Style: Rich OpenTransition elements
Community: Multiple orange butterflies, connecting elements

Logo must be IDENTICAL across all 10 assets - just butterfly circle with sparkle."""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} with CONSISTENT LOGO...\n")
    print("🦋 Logo Consistency Rule:\n")
    print("  ✓ Logo is ONLY butterfly in circle with sparkle")
    print("  ✓ NO text 'OpenTransition' added to logo")
    print("  ✓ Logo stays IDENTICAL across all assets")
    print("  ✓ Text is SEPARATE from logo\n")
    
    all_generated_files = []
    
    for idx, asset in enumerate(assets, 1):
        print(f"[{idx}/{len(assets)}] Generating {asset['name']}...")
        print(f"   Ensuring logo consistency...")
        
        try:
            # Build content with references
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
            
            print(f"   ✅ {asset['name']} generated\n")
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}\n")
            continue
    
    print(f"\n{'='*70}")
    print(f"✅ Assets Regenerated with Consistent Logo!")
    print(f"{'='*70}")
    print(f"Total: {len(all_generated_files)} assets")
    print(f"\nLogo Consistency:")
    print(f"  🦋 Same butterfly circle with sparkle across ALL assets")
    print(f"  📝 'OpenTransition' text separate from logo")
    print(f"  ✓ Logo identical in every image")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    regenerate_with_consistent_logo()
