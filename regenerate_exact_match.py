#!/usr/bin/env python3
"""
Regenerate assets matching EXACT OpenTransition website visuals:
- Organic flowing teardrop shapes (like section-background.png)
- Butterflies as transformation symbols  
- Sparkle/star elements
- Warm orange (#E68322) people/elements
- Soft peachy-cream gradients
- Flat illustration style
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, image_to_base64_url, call_openrouter, 
    save_generated_images, Path
)

def regenerate_matching_opentransition():
    """Regenerate to EXACTLY match OpenTransition website graphics"""
    
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
    
    # EXACT OpenTransition visual style
    visual_style = """
EXACT VISUAL STYLE FROM OPENTRANSITION WEBSITE:
- Organic flowing shapes: Large soft teardrop/water drop shapes with subtle white outlines, overlapping translucently
- Butterflies: Orange/peach butterflies (#E68322, #F9B21E) as transformation symbols scattered throughout
- Sparkles: Four-pointed star sparkles in warm yellow (#F9B21E)
- Flowing lines: Gentle curved paths connecting elements
- Flat illustration: Simple, friendly flat illustration style (NOT photorealistic)
- Colors: Cream backgrounds (#F5E8DA, #FFF8E7), warm orange (#E68322), golden yellow (#F9B21E), soft peach gradients
- NO traditional trans flag colors - use warm oranges and peachy creams only
- Soft, welcoming, organic aesthetic with transformation theme (butterflies)
"""
    
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo centered, surrounded by 3-4 large organic teardrop/water drop shapes (like section-background.png), 2-3 orange butterflies (#E68322), 5-6 sparkle stars (#F9B21E), gentle flowing curved lines

Composition: Wide format, logo prominent center, organic shapes flowing from left (cream/peach) to right (light orange), butterflies scattered in upper right and lower left, sparkles adding magic feel

Action: Butterflies appearing to flutter upward (transformation), gentle flow suggesting journey/progress

Location: Soft peachy-cream gradient background (#FFF8E7 to #F5E8DA), clean modern space

Style: FLAT ILLUSTRATION style exactly like OpenTransition og-image, warm friendly aesthetic, Material 3 rounded elements, organic flowing shapes with subtle white outlines

Lighting: Soft even lighting, no dramatic shadows, flat friendly illustration style

Technical:
- Aspect Ratio: 16:9  
- Resolution: 1920x1080
- Colors: Cream #F5E8DA, peach #FFEEDD, orange #E68322, yellow #F9B21E
- Elements: Organic teardrop shapes, butterflies, sparkles, curved lines, logo

CRITICAL: Match OpenTransition section-background.png organic shapes + og-image.png butterflies/sparkles EXACTLY. Flat illustration style, NOT photorealistic."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo centered, 2-3 organic teardrop shapes, 1-2 butterflies, 3-4 sparkles, flowing curved line

Composition: Square format, logo center, organic shapes balanced around it, butterfly upper right, sparkles corners

Action: Butterfly suggesting upward transformation

Location: Soft peachy gradient (#FFF8E7 to #F5E8DA)

Style: FLAT ILLUSTRATION matching OpenTransition exactly, warm friendly, Material 3 rounded

Technical:
- 1:1, 1080x1080
- Colors: Cream #F5E8DA, orange #E68322, yellow #F9B21E
- Elements: Organic shapes, butterflies, sparkles

CRITICAL: Flat illustration style like OpenTransition, organic teardrop shapes, butterflies."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo upper-middle, 2-3 vertical organic shapes, 2 butterflies, 4-5 sparkles, flowing vertical line

Composition: Vertical mobile, logo upper-middle, organic shapes flowing top to bottom, butterflies mid and lower

Action: Butterflies fluttering upward along flowing line

Location: Vertical peachy gradient

Style: FLAT ILLUSTRATION OpenTransition style, mobile-optimized

Technical:
- 9:16, 1080x1920
- OpenTransition colors and elements

CRITICAL: Match OpenTransition flat illustration exactly."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo right-center, 4-5 organic shapes flowing left to right, 3 butterflies, 6-7 sparkles, curved paths

Composition: Ultra-wide, logo positioned right, organic shapes flow from left (cream) to right (orange), butterflies scattered

Action: Butterflies suggesting journey across wide space

Location: Wide peachy gradient

Style: FLAT ILLUSTRATION OpenTransition style

Technical:
- 21:9 ultra-wide
- OpenTransition visual elements

CRITICAL: Organic shapes + butterflies + sparkles from OpenTransition."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo right-of-center, 3-4 organic shapes, 2-3 butterflies, 5 sparkles, flowing lines

Composition: Wide (crop to 3:1), logo right, organic flow left to right, butterflies scattered

Style: FLAT ILLUSTRATION OpenTransition style

Technical:
- 21:9 (crop to 3:1)
- OpenTransition elements

CRITICAL: Match OpenTransition flat style exactly."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo right, 3-4 subtle organic shapes, 1-2 butterflies, 4 sparkles, professional yet warm

Composition: Wide professional (crop to 4:1), logo right, subtle organic elements

Style: FLAT ILLUSTRATION OpenTransition style, slightly more professional

Technical:
- 21:9 (crop to 4:1)
- OpenTransition colors, subtle approach

CRITICAL: Professional but keep OpenTransition flat illustration style."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo centered, 1-2 small organic shapes as background, 1 butterfly, 2 sparkles

Composition: Circular-safe, logo center, simple organic background

Style: FLAT ILLUSTRATION OpenTransition style, circular-optimized

Technical:
- 1:1, 1024x1024
- Simple OpenTransition elements

CRITICAL: Clean flat style, circular-safe, warm peachy background."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo simplified center, 1 organic shape background, 1 small butterfly, 1 sparkle

Composition: App icon square, logo prominent, minimal elements

Style: FLAT ILLUSTRATION OpenTransition style, icon-optimized

Technical:
- 1:1, 1024x1024
- Simplified for small sizes
- OpenTransition warm colors

CRITICAL: Simple flat icon, logo clear at tiny sizes, warm peachy background."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo centered, 3-4 organic shapes, 2-3 butterflies, 5-6 sparkles, flowing paths

Composition: Vertical splash, logo center, organic shapes and butterflies creating welcoming atmosphere

Action: Butterflies fluttering upward, suggesting beginning of journey

Style: FLAT ILLUSTRATION OpenTransition style

Technical:
- 9:16, 1080x1920
- Full OpenTransition visual treatment

CRITICAL: Welcoming splash with all OpenTransition elements - organic shapes, butterflies, sparkles."""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate matching OpenTransition website EXACTLY:

{visual_style}

Subject: Logo present, 4-5 organic shapes, 3-4 butterflies, 7-8 sparkles, multiple flowing curved paths connecting across image suggesting community

Composition: Wide banner, logo visible, organic shapes and butterflies throughout, flowing lines suggesting connections and shared journey

Action: Multiple butterflies at different positions suggesting diverse journeys, curved paths connecting suggesting community support

Style: FLAT ILLUSTRATION OpenTransition style emphasizing community/connection

Technical:
- 16:9, 1920x1080
- Rich use of OpenTransition elements showing community

CRITICAL: Community theme - multiple butterflies, connecting paths, organic shapes suggesting diverse yet connected journeys."""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} to MATCH OpenTransition visuals EXACTLY...\n")
    print("🎨 Visual style: Organic teardrop shapes + Butterflies + Sparkles + Warm orange/peach\n")
    print("📊 Reference: OpenTransition website graphics analyzed\n")
    
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
    print(f"✅ Assets Regenerated Matching OpenTransition Website!")
    print(f"{'='*70}")
    print(f"Total: {len(all_generated_files)} assets")
    print(f"\nVisual Elements:")
    print(f"  ✓ Organic teardrop/water drop shapes (like section-background.png)")
    print(f"  ✓ Orange butterflies as transformation symbols (#E68322)")
    print(f"  ✓ Sparkle stars (#F9B21E)")
    print(f"  ✓ Flowing curved lines")
    print(f"  ✓ Flat illustration style (NOT photorealistic)")
    print(f"  ✓ Warm peachy-cream gradients")
    print(f"\nMatches: https://shelbeely.github.io/OpenTransition-website/")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    regenerate_matching_opentransition()
