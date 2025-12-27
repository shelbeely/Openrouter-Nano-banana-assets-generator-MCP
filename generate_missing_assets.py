#!/usr/bin/env python3
"""
Generate the two missing assets (Twitter header and LinkedIn banner)
"""
import sys
import os

# Add parent directory to path to import from generate_asset_pack
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, image_to_base64_url, call_openrouter, 
    save_generated_images, Path
)

def generate_missing_assets():
    """Generate Twitter header and LinkedIn banner"""
    
    if not OPENROUTER_API_KEY:
        print("❌ ERROR: OPENROUTER_API_KEY environment variable not set")
        sys.exit(1)
    
    # Paths
    repo_root = Path(__file__).parent
    logo_path = repo_root / "assets/generated/logo_transparent.png"
    output_dir = repo_root / "assets/generated/asset_pack"
    output_dir.mkdir(exist_ok=True)
    
    # Convert logo to base64
    print("📦 Preparing logo...")
    logo_base64 = image_to_base64_url(str(logo_path))
    print(f"✅ Logo loaded\n")
    
    # Define the two missing assets with supported aspect ratio
    assets = [
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": """Generate a high-quality Twitter header banner for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo integrated into a supportive Twitter header with affirming design elements celebrating transgender community

Composition: Ultra-wide horizontal layout (will be cropped to Twitter header), logo prominently positioned on right side to avoid profile picture, supportive layout with breathing room

Action: Uplifting presence conveying support, community, validation, and empowerment for transgender individuals

Location: Twitter header environment, inclusive health/wellness social media presence, affirming community space

Style: Modern Twitter-appropriate inclusive design, warm and supportive, celebrates transgender identity with compassion

Lighting: Warm supportive lighting optimized for Twitter display, gentle affirming glow

Camera Details: Wide welcoming header perspective, inclusive presentation
Materiality: Clear supportive logo, caring background, inclusive social presence

Technical Specifications:
Aspect Ratio: 21:9 (will be center-cropped for Twitter)
Resolution: High quality for Twitter display
Color Palette: Transgender-affirming colors - trans flag (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples, gentle pride accents

Requirements:
- Wide format with center focus for cropping
- Logo clearly visible with warmth, positioned right-of-center
- Supportive affirming appearance for transgender community
- Left side safe zone for profile picture
- Creates welcoming inclusive space

NOTE: This will be center-cropped to fit Twitter's 3:1 header requirement

IMPORTANT: The reference image is the brand logo. Create a supportive extra-wide banner celebrating transgender identity - it will be cropped to Twitter header proportions."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": """Generate a high-quality LinkedIn banner for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo integrated into a professional yet compassionate LinkedIn banner suitable for health-tech and inclusive healthcare presence

Composition: Ultra-wide professional LinkedIn banner format (will be cropped to LinkedIn proportions), logo strategically positioned on right, healthcare-appropriate layout, professional yet caring visual hierarchy

Action: Professional presentation conveying both credibility and compassion, supporting transgender health and wellness

Location: Professional LinkedIn environment, health-tech and inclusive healthcare B2B presence

Style: Professional healthcare-tech design with inclusive compassionate elements, appropriate for health/wellness industry, modern supportive aesthetic

Lighting: Professional warm lighting, trustworthy yet caring presentation, supportive glow

Camera Details: Wide professional banner perspective, healthcare industry depth
Materiality: Logo crisp and professional with warmth, background sophisticated yet supportive, health-tech appropriate

Technical Specifications:
Aspect Ratio: 21:9 (will be center-cropped for LinkedIn)
Resolution: High quality for professional LinkedIn display
Color Palette: Professional health-tech colors with transgender-affirming accents - supportive purples (#A78BFA, #C084FC), trans flag accents (light blue #5BCEFA, pink #F5A9B8), clean professional palette

Requirements:
- Wide format with center focus for cropping to 4:1
- Professional healthcare appearance with inclusive values
- Logo prominently featured on right side
- Appropriate for B2B healthcare/wellness partnerships
- Conveys both credibility and compassion
- Left side safe for profile picture

NOTE: This will be center-cropped to fit LinkedIn's 4:1 banner requirement

IMPORTANT: The reference image is the brand logo. Create a professional health-tech extra-wide banner that balances credibility with inclusive, supportive values for transgender healthcare - will be cropped to LinkedIn proportions."""
        }
    ]
    
    print(f"🚀 Generating 2 missing assets (Twitter header & LinkedIn banner)...\n")
    print("🏳️‍⚧️ Using 21:9 aspect ratio (will need cropping for final use)\n")
    
    all_generated_files = []
    
    for idx, asset in enumerate(assets, 1):
        print(f"[{idx}/2] Generating {asset['name']}...")
        print(f"   Aspect Ratio: {asset['aspect_ratio']}")
        
        try:
            response = call_openrouter(
                prompt=asset['prompt'],
                logo_base64=logo_base64,
                aspect_ratio=asset['aspect_ratio']
            )
            
            saved_files = save_generated_images(response, asset['name'], output_dir)
            all_generated_files.extend(saved_files)
            
            print(f"   ✅ Completed {asset['name']}\n")
            
        except Exception as e:
            print(f"   ❌ Error generating {asset['name']}: {str(e)}\n")
            continue
    
    print(f"\n{'='*60}")
    print(f"✅ Missing Assets Generated!")
    print(f"{'='*60}")
    print(f"Total assets generated: {len(all_generated_files)}")
    print(f"\nNote: These assets are in 21:9 format and will need to be")
    print(f"center-cropped to fit Twitter (3:1) and LinkedIn (4:1) requirements.")
    print(f"The logo has been positioned to accommodate this cropping.")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    generate_missing_assets()
