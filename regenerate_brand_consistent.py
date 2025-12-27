#!/usr/bin/env python3
"""
Regenerate assets EXACTLY matching OpenTransition website with subtle queer enhancement

OpenTransition website actual style:
- Warm orange (#E68322) butterflies (NOT rainbow)
- Peachy cream backgrounds (#FFF8E7, #F5E8DA, #FFEEDD)
- Organic teardrop shapes in warm tones
- Flat illustration style
- Yellow sparkles (#F9B21E)

"A bit more queer" means:
- Trans flag colors (light blue, pink) integrated within existing palette
- Keep warm orange base consistent with OpenTransition branding
- Subtle trans pride WITHOUT changing the brand
- NO full rainbow - maintain OpenTransition's cohesive color scheme
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, image_to_base64_url, call_openrouter, 
    save_generated_images, Path
)

def regenerate_brand_consistent():
    """Regenerate matching OpenTransition EXACTLY + subtle trans pride"""
    
    if not OPENROUTER_API_KEY:
        print("❌ ERROR: OPENROUTER_API_KEY environment variable not set")
        sys.exit(1)
    
    repo_root = Path(__file__).parent
    logo_path = repo_root / "assets/generated/logo_transparent.png"
    output_dir = repo_root / "assets/generated/asset_pack"
    output_dir.mkdir(exist_ok=True)
    
    print("📦 Preparing logo...")
    logo_base64 = image_to_base64_url(str(logo_path))
    print(f"✅ Logo loaded\n")
    
    visual_style = """
EXACT OPENTRANSITION BRANDING (MUST MATCH):

FROM WEBSITE ANALYSIS:
- PRIMARY COLOR: Warm orange #E68322 (NOT rainbow)
- SECONDARY: Golden yellow #F9B21E
- BACKGROUNDS: Peachy cream #FFF8E7, #F5E8DA, #FFEEDD, #FCF4ED
- BUTTERFLIES: Orange and yellow (like og-image.png) - NOT rainbow
- ORGANIC SHAPES: Soft teardrop shapes in peachy/cream tones (section-background.png)
- SPARKLES: Four-pointed stars in golden yellow
- FLAT ILLUSTRATION: Warm, friendly style from og-image.png
- FLOWING LINES: Gentle curved paths in warm tones

BRAND CONSISTENCY CRITICAL:
✓ Keep warm orange as primary color throughout
✓ Peachy cream gradients only
✓ Orange/yellow butterflies (NOT rainbow)
✓ Golden yellow sparkles
✓ Maintain OpenTransition cohesive warm aesthetic

"A BIT MORE QUEER" (SUBTLE ENHANCEMENTS):
- Trans flag colors integrated WITHIN warm palette:
  * Use light blue #5BCEFA alongside cream backgrounds (subtle accent)
  * Use pink #F5A9B8 alongside peachy tones (already similar!)
  * Mix trans colors subtly into organic shapes
- Some butterflies with trans flag wings (blue/pink) ALONGSIDE orange ones
- Trans flag as subtle accent, NOT dominant
- Maintain warm orange base - just add trans pride touches

RESULT: OpenTransition branding preserved + subtle trans pride visibility
"""
    
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate hero banner EXACTLY matching OpenTransition website with subtle trans pride:

{visual_style}

Subject: Logo centered, 4-5 large organic teardrop shapes (peachy cream tones with SUBTLE trans flag blue/pink accents), 3-4 butterflies (MOSTLY warm orange #E68322, 1-2 with trans flag blue/pink wings as subtle accent), 6-7 sparkles (golden yellow #F9B21E with few trans colored)

Composition: Wide hero, logo prominent center, organic shapes flowing in OpenTransition's peachy aesthetic, butterflies scattered (primarily orange, some with subtle trans colors), warm welcoming composition

Action: Butterflies fluttering upward (transformation), warm orange primary with subtle trans pride accents

Location: Peachy cream gradient background (#FFF8E7 to #F5E8DA) with VERY SUBTLE trans blue/pink accents

Style: FLAT ILLUSTRATION exactly like OpenTransition og-image.png - warm orange primary, peachy backgrounds, friendly illustration style. Trans colors as SUBTLE accent only.

Lighting: Soft warm lighting matching OpenTransition, gentle peachy glow

Technical:
- 16:9, 1920x1080
- PRIMARY: Warm orange #E68322, golden yellow #F9B21E
- BACKGROUNDS: Peachy cream #FFF8E7, #F5E8DA, #FFEEDD
- TRANS ACCENT: Light blue #5BCEFA, pink #F5A9B8 (SUBTLE, not dominant)
- Elements: Organic shapes, mostly orange butterflies, golden sparkles, logo

CRITICAL: Match OpenTransition branding EXACTLY. Warm orange primary. Peachy backgrounds. Trans colors as SUBTLE accent only. Brand consistency is paramount."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate Instagram post EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo centered, 2-3 organic shapes (peachy with subtle trans accents), 2 butterflies (orange + 1 trans flag accent), 4 sparkles (golden yellow)

Composition: Square, logo center, OpenTransition warm aesthetic, subtle trans pride

Action: Warm orange butterflies with subtle trans accent

Location: Peachy gradient OpenTransition style

Style: FLAT ILLUSTRATION OpenTransition, warm orange primary, subtle trans touches

Technical:
- 1:1, 1080x1080
- Warm orange primary + peachy backgrounds + subtle trans accents

CRITICAL: OpenTransition branding first, trans pride subtle."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate Instagram story EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo upper-middle, 2-3 vertical organic shapes (peachy with subtle trans tints), 2-3 butterflies (primarily orange, 1 trans flag wings), 5 sparkles (golden)

Composition: Vertical mobile, OpenTransition warm aesthetic maintained

Action: Orange butterflies ascending, subtle trans pride accent

Style: FLAT ILLUSTRATION OpenTransition style, warm primary

Technical:
- 9:16, 1080x1920
- Warm orange + peachy + subtle trans accents

CRITICAL: OpenTransition brand consistency, subtle trans touches."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate Facebook cover EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo right-center, 4-5 organic shapes (peachy with subtle trans tints), 3 butterflies (mostly orange, 1 trans wings), 6 sparkles (golden)

Composition: Wide, OpenTransition warm flowing aesthetic

Action: Warm orange butterflies, subtle trans accent

Style: FLAT ILLUSTRATION OpenTransition, warm brand colors

Technical:
- 21:9
- Warm orange primary + subtle trans

CRITICAL: OpenTransition branding maintained."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate Twitter header EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo right, 3-4 organic shapes (peachy with subtle trans), 2-3 butterflies (orange primary, subtle trans accent), 5 sparkles (golden)

Style: FLAT ILLUSTRATION OpenTransition brand style

Technical:
- 21:9 (crop to 3:1)
- Warm orange + subtle trans

CRITICAL: OpenTransition brand colors maintained."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate LinkedIn banner EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo right, 3-4 subtle organic shapes (peachy with very subtle trans tints), 2 butterflies (orange, 1 subtle trans wings), 4 sparkles (golden)

Style: FLAT ILLUSTRATION OpenTransition, professional warm aesthetic

Technical:
- 21:9 (crop to 4:1)
- Warm orange primary + very subtle trans

CRITICAL: Professional OpenTransition branding."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate profile picture EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo centered, 1-2 organic shapes (peachy background with subtle trans tint), 1 butterfly (orange or subtle trans), 2 sparkles (golden)

Style: FLAT ILLUSTRATION OpenTransition, circular-safe

Technical:
- 1:1, 1024x1024
- Warm peachy background + subtle trans accent

CRITICAL: OpenTransition warm brand, simple clean design."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate app icon EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo simplified center, 1 organic shape (peachy with subtle trans tint), 1 small butterfly (orange or subtle trans wings), 1 sparkle (golden)

Style: FLAT ILLUSTRATION OpenTransition, icon-optimized

Technical:
- 1:1, 1024x1024
- Warm peachy + subtle trans
- Clear at small sizes

CRITICAL: OpenTransition warm branding, simple icon."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate app splash EXACTLY matching OpenTransition with subtle trans pride:

{visual_style}

Subject: Logo centered, 3-4 organic shapes (peachy with subtle trans tints), 2-3 butterflies (mostly orange, 1 trans accent), 5-6 sparkles (golden)

Style: FLAT ILLUSTRATION OpenTransition welcoming style

Technical:
- 9:16, 1080x1920
- Warm orange primary + peachy + subtle trans accents

CRITICAL: OpenTransition warm welcoming brand."""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate community banner EXACTLY matching OpenTransition with trans pride visible:

{visual_style}

Subject: Logo visible, 4-5 organic shapes (peachy with trans blue/pink mixed in), 3-4 butterflies (mix of orange and trans flag wings - about 50/50), 7-8 sparkles (golden with some trans colored)

Composition: Community focused, OpenTransition warm style, trans pride MORE visible here (community banner can be more explicit)

Action: Mix of orange and trans butterflies (community diversity), warm base maintained

Style: FLAT ILLUSTRATION OpenTransition, community celebration

Technical:
- 16:9, 1920x1080
- Warm orange maintained as base + trans colors MORE prominent for community
- Still cohesive with OpenTransition brand

CRITICAL: Community banner can show more trans pride while keeping OpenTransition warm orange base. Balance warm branding with trans community celebration."""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} with EXACT OpenTransition branding + subtle trans pride...\n")
    print("🎨 Brand-Consistent Design:\n")
    print("  ✓ Warm orange #E68322 as PRIMARY (like OpenTransition)")
    print("  ✓ Peachy cream backgrounds (matching website)")
    print("  ✓ Golden yellow sparkles")
    print("  ✓ MOSTLY orange butterflies")
    print("  ✓ Trans flag colors as SUBTLE accent")
    print("  ✓ Brand consistency maintained")
    print("  ✓ Flat illustration style from OpenTransition\n")
    
    all_generated_files = []
    
    for idx, asset in enumerate(assets, 1):
        print(f"[{idx}/{len(assets)}] Generating {asset['name']}...")
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
    
    print(f"\n{'='*70}")
    print(f"✅ Brand-Consistent Assets with Subtle Trans Pride!")
    print(f"{'='*70}")
    print(f"Total: {len(all_generated_files)} assets")
    print(f"\nBrand Consistency:")
    print(f"  🧡 Warm orange primary (OpenTransition brand)")
    print(f"  🍑 Peachy cream backgrounds (matches website)")
    print(f"  🦋 Mostly orange butterflies (brand consistent)")
    print(f"  ✨ Golden yellow sparkles (brand consistent)")
    print(f"  🏳️‍⚧️ Trans flag colors as subtle accent (not overwhelming)")
    print(f"  🎨 Flat illustration style (OpenTransition aesthetic)")
    print(f"\nResult: Cohesive OpenTransition branding + subtle trans pride visibility")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    regenerate_brand_consistent()
