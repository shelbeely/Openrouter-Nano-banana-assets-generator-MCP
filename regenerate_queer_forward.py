#!/usr/bin/env python3
"""
Final regeneration matching ALL OpenTransition website images with QUEER-FORWARD design

Analyzed images:
1. og-image.png - Diverse people, butterflies, sparkles, flowing paths
2. section-background.png - Organic teardrop shapes with subtle outlines
3. logo.png - Butterfly/transformation symbol in circle
4. decorative-pattern.png - Additional decorative elements

QUEER-FORWARD additions:
- Rainbow pride elements subtly integrated
- Diverse representation emphasized
- Transformation theme (butterflies) connected to queer identity
- Inclusive visual language celebrating LGBTQ+ community
- Trans flag colors INCLUDED alongside warm oranges
- Pride rainbow accents throughout
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, image_to_base64_url, call_openrouter, 
    save_generated_images, Path
)

def regenerate_queer_forward_assets():
    """Regenerate ALL assets matching OpenTransition + QUEER-FORWARD design"""
    
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
EXACT OPENTRANSITION VISUAL STYLE + QUEER-FORWARD:

FROM OPENTRANSITION WEBSITE:
- Organic teardrop/water drop shapes (section-background.png): Large soft overlapping shapes with subtle white outlines
- Butterflies: Orange/peach butterflies as transformation symbols (og-image.png)
- Sparkles: Four-pointed stars
- Flowing curved paths: Connecting elements, representing journey
- Flat illustration style: Friendly, warm, welcoming (NOT photorealistic)
- Diverse people: Various skin tones, body types, ages (og-image.png shows this)

BASE COLORS FROM SITE:
- Warm oranges: #E68322, #F9B21E
- Peachy creams: #FFF8E7, #F5E8DA, #FFEEDD
- Soft gradients from cream to peach to orange

QUEER-FORWARD ADDITIONS (CRITICAL):
- Trans flag colors integrated: Light blue #5BCEFA, Pink #F5A9B8, White #FFFFFF
- Rainbow pride gradient: Subtly woven through flowing paths and organic shapes
- Pride flag spectrum: Red #E40303, Orange #FF8C00, Yellow #FFED00, Green #008026, Blue #24408E, Purple #732982
- Multiple butterflies in rainbow colors (not just orange)
- Sparkles in pride rainbow colors
- Organic shapes with pride gradient fills
- Celebrate LGBTQ+ identity explicitly
- Transformation theme = queer journey/transition
- Inclusive, diverse, celebratory aesthetic

VISUAL ELEMENTS:
✓ Organic teardrop shapes (some with pride gradients)
✓ Rainbow butterflies (trans flag colors + full pride spectrum)
✓ Rainbow sparkles
✓ Flowing rainbow paths
✓ Trans flag colors prominent
✓ Warm orange base + queer pride colors
✓ Flat illustration style
✓ Celebratory, affirming, proud aesthetic
"""
    
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate QUEER-FORWARD hero banner matching OpenTransition style:

{visual_style}

Subject: Logo centered, 4-5 large organic teardrop shapes (some with trans flag gradient #5BCEFA to #F5A9B8, some with warm orange #E68322), 4-5 butterflies in RAINBOW PRIDE COLORS (trans blue, trans pink, pride rainbow spectrum), 7-8 sparkles in rainbow colors, flowing curved rainbow gradient paths

Composition: Wide hero format, logo prominent center, organic shapes flowing elegantly, butterflies in pride colors scattered throughout suggesting transformation and queer journey, rainbow paths connecting elements, trans flag colors prominent alongside warm oranges

Action: Rainbow butterflies fluttering upward (queer liberation, transformation), flowing pride paths suggesting journey and community connection

Location: Soft gradient background blending peachy cream (#FFF8E7) with subtle trans flag colors, welcoming queer-affirming space

Style: FLAT ILLUSTRATION exactly like OpenTransition og-image.png BUT with explicit QUEER pride elements - rainbow butterflies, trans flag colors, pride gradients, celebratory LGBTQ+ aesthetic

Lighting: Soft warm lighting celebrating queer identity, rainbow highlights, affirming glow

Technical:
- 16:9, 1920x1080
- Colors: Trans flag (#5BCEFA, #F5A9B8, #FFF), warm oranges (#E68322, #F9B21E), peachy creams (#FFF8E7, #F5E8DA), FULL PRIDE RAINBOW spectrum
- Elements: Organic shapes with pride gradients, rainbow butterflies (NOT just orange), rainbow sparkles, rainbow flowing paths, logo

CRITICAL: OpenTransition flat illustration style + EXPLICITLY QUEER-FORWARD. Rainbow pride butterflies, trans flag colors prominent, celebratory LGBTQ+ aesthetic. NOT subtle - PROUD and VISIBLE queer representation."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate QUEER-FORWARD Instagram post matching OpenTransition:

{visual_style}

Subject: Logo centered, 2-3 organic shapes (with pride gradients), 2-3 rainbow pride butterflies, 4-5 rainbow sparkles, flowing pride path

Composition: Square social format, logo center, organic shapes with trans flag and pride rainbow gradients, butterflies in queer pride colors

Action: Rainbow butterflies celebrating queer identity and transformation

Location: Peachy gradient with trans flag color accents

Style: FLAT ILLUSTRATION OpenTransition style + QUEER-FORWARD pride elements

Technical:
- 1:1, 1080x1080
- Trans flag + pride rainbow + warm oranges
- Rainbow butterflies, pride sparkles

CRITICAL: Explicitly queer Instagram post - rainbow pride butterflies, trans colors, celebrating LGBTQ+ community."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate QUEER-FORWARD Instagram story matching OpenTransition:

{visual_style}

Subject: Logo upper-middle, 2-3 vertical organic shapes (with pride gradients), 3 rainbow butterflies vertically arranged, 5-6 rainbow sparkles, vertical pride rainbow path

Composition: Vertical mobile story, logo visible, organic shapes flowing top to bottom with trans and pride colors, rainbow butterflies ascending

Action: Rainbow pride butterflies fluttering upward along rainbow path (queer liberation journey)

Location: Vertical peachy gradient with trans flag accents

Style: FLAT ILLUSTRATION OpenTransition + QUEER pride

Technical:
- 9:16, 1080x1920
- Trans flag + pride rainbow + warm base
- Vertical rainbow flow

CRITICAL: Mobile story celebrating queer identity - rainbow butterflies ascending, pride path, trans colors."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate QUEER-FORWARD Facebook cover matching OpenTransition:

{visual_style}

Subject: Logo right-center, 5-6 organic shapes (pride gradients), 4 rainbow butterflies, 7-8 rainbow sparkles, flowing rainbow paths left to right

Composition: Ultra-wide cover, logo positioned right, organic shapes flow with pride gradients, rainbow butterflies scattered, pride paths connecting

Action: Rainbow butterflies suggesting queer journey across wide space

Location: Wide peachy gradient with trans flag and pride accents

Style: FLAT ILLUSTRATION OpenTransition + QUEER-FORWARD

Technical:
- 21:9 ultra-wide
- Trans + pride + warm oranges
- Rainbow elements throughout

CRITICAL: Wide Facebook cover celebrating LGBTQ+ community - prominent rainbow butterflies, pride gradients."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate QUEER-FORWARD Twitter header matching OpenTransition:

{visual_style}

Subject: Logo right-of-center, 3-4 organic shapes (pride gradients), 3 rainbow butterflies, 6 rainbow sparkles, pride flowing lines

Composition: Wide header (crop to 3:1), logo right, organic shapes with queer pride gradients, rainbow butterflies

Action: Pride butterflies celebrating queer identity

Style: FLAT ILLUSTRATION OpenTransition + QUEER pride

Technical:
- 21:9 (crop to 3:1)
- Trans + pride rainbow + warm base

CRITICAL: Twitter header with explicit queer pride - rainbow butterflies, trans colors, LGBTQ+ celebration."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate QUEER-FORWARD professional LinkedIn banner matching OpenTransition:

{visual_style}

Subject: Logo right, 3-4 subtle organic shapes (with tasteful pride gradient accents), 2 rainbow butterflies (elegant), 5 sparkles (pride colors), professional yet proudly queer

Composition: Wide professional (crop to 4:1), logo right, elegant organic elements with subtle but visible pride colors

Action: Elegant rainbow butterflies (professional but proudly LGBTQ+)

Style: FLAT ILLUSTRATION OpenTransition, professional BUT visibly queer-affirming

Technical:
- 21:9 (crop to 4:1)
- Trans flag + subtle pride accents + warm professional base

CRITICAL: Professional LinkedIn BUT openly queer - tasteful rainbow elements, trans colors present, professional pride visibility."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate QUEER-FORWARD profile picture matching OpenTransition:

{visual_style}

Subject: Logo centered, 1-2 organic shapes (pride gradient background), 1 rainbow butterfly, 2-3 rainbow sparkles

Composition: Circular-safe profile, logo center, simple pride background, rainbow butterfly accent

Style: FLAT ILLUSTRATION OpenTransition + visible queer pride

Technical:
- 1:1, 1024x1024, circular-safe
- Trans flag + pride rainbow background
- Rainbow butterfly

CRITICAL: Profile picture with visible queer pride - rainbow butterfly, pride gradient background, trans colors."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate QUEER-FORWARD app icon matching OpenTransition:

{visual_style}

Subject: Logo simplified center, 1 organic shape (pride gradient), 1 small rainbow butterfly, 1 rainbow sparkle

Composition: App icon square, logo prominent, pride gradient background, rainbow butterfly accent

Style: FLAT ILLUSTRATION OpenTransition + queer pride, icon-optimized

Technical:
- 1:1, 1024x1024
- Simplified for app icon
- Trans flag + pride gradient
- Rainbow butterfly visible even at small size

CRITICAL: App icon with proud queer identity - pride gradient, rainbow butterfly, immediately recognizable as LGBTQ+ affirming."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate QUEER-FORWARD app splash screen matching OpenTransition:

{visual_style}

Subject: Logo centered, 3-4 organic shapes (pride gradients), 3-4 rainbow butterflies, 6-7 rainbow sparkles, flowing rainbow paths

Composition: Vertical mobile splash, logo center, organic shapes with trans and pride gradients creating welcoming queer-affirming atmosphere, rainbow butterflies celebrating identity

Action: Rainbow pride butterflies fluttering upward (queer journey beginning), rainbow paths suggesting community connection and support

Location: Vertical gradient blending peachy cream with trans flag colors

Style: FLAT ILLUSTRATION OpenTransition + celebratory QUEER pride

Technical:
- 9:16, 1080x1920
- Trans flag + full pride rainbow + warm base
- Welcoming queer-forward splash

CRITICAL: App splash celebrating LGBTQ+ users - rainbow butterflies, trans colors prominent, pride gradients, immediate queer affirmation."""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate QUEER-FORWARD community banner matching OpenTransition:

{visual_style}

Subject: Logo visible, 5-6 organic shapes (rainbow pride gradients), 5-6 rainbow butterflies, 9-10 rainbow sparkles, multiple flowing rainbow paths connecting across image

Composition: Wide community banner, logo present, abundant organic shapes with full pride spectrum gradients, many rainbow butterflies at different positions, flowing rainbow paths suggesting LGBTQ+ community connections and shared queer journey

Action: Multiple rainbow pride butterflies fluttering together (queer community solidarity), rainbow paths connecting (mutual support), transformation and liberation theme

Location: Peachy base with prominent trans flag colors and full pride rainbow

Style: FLAT ILLUSTRATION OpenTransition + EXPLICITLY QUEER community celebration

Technical:
- 16:9, 1920x1080
- Trans flag + FULL pride rainbow spectrum + warm base
- Rich queer community imagery

CRITICAL: Community banner celebrating LGBTQ+ solidarity - many rainbow butterflies (diverse queer identities), connecting rainbow paths (community support), trans flag colors prominent, full pride spectrum, explicitly queer-forward and celebratory. Most visibly queer asset of all."""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} QUEER-FORWARD assets matching OpenTransition...\n")
    print("🏳️‍🌈 QUEER-FORWARD Design:\n")
    print("  ✓ Rainbow pride butterflies (not just orange)")
    print("  ✓ Trans flag colors prominent (#5BCEFA, #F5A9B8, #FFF)")
    print("  ✓ Pride rainbow spectrum throughout")
    print("  ✓ Organic shapes with pride gradients")
    print("  ✓ Rainbow sparkles and flowing paths")
    print("  ✓ Celebrating LGBTQ+ identity explicitly")
    print("  ✓ Transformation theme = queer journey")
    print("  ✓ OpenTransition flat illustration style")
    print("  ✓ Warm orange base + queer pride colors\n")
    
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
    print(f"🏳️‍🌈 QUEER-FORWARD Assets Complete! 🏳️‍⚧️")
    print(f"{'='*70}")
    print(f"Total: {len(all_generated_files)} assets")
    print(f"\nQueer-Forward Elements:")
    print(f"  🦋 Rainbow pride butterflies (trans blue, pink, full pride spectrum)")
    print(f"  🏳️‍⚧️ Trans flag colors prominent (#5BCEFA, #F5A9B8, #FFF)")
    print(f"  🌈 Pride rainbow gradients in organic shapes")
    print(f"  ✨ Rainbow sparkles throughout")
    print(f"  🛤️ Flowing rainbow paths (community connection)")
    print(f"  💕 Celebrating LGBTQ+ identity explicitly")
    print(f"  🎨 OpenTransition flat illustration style + queer pride")
    print(f"\nBase: OpenTransition website + Explicit Queer Celebration")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    regenerate_queer_forward_assets()
