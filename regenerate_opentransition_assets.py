#!/usr/bin/env python3
"""
Regenerate asset pack to match OpenTransition website Material 3 theme
"""
import sys
import os

# Add parent directory to path to import from generate_asset_pack
sys.path.insert(0, os.path.dirname(__file__))

from generate_asset_pack import (
    OPENROUTER_API_KEY, image_to_base64_url, call_openrouter, 
    save_generated_images, Path
)

def regenerate_opentransition_assets():
    """Regenerate all assets to match OpenTransition website Material 3 theme"""
    
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
    
    # OpenTransition website Material 3 color scheme
    color_scheme = {
        "primary": "#E68322",  # Warm orange
        "primary_dark": "#BC5A1E",  # Dark orange/brown
        "secondary": "#F9B21E",  # Accent orange
        "tertiary": "#EFBF84",  # Light peach
        "background_light": "#FFF8E7",  # Cream
        "background_peach": "#FFEEDD",  # Light peach
        "surface": "#FCF4ED",  # Light surface
        "surface_variant": "#F5E6D3",  # Beige surface
        "text_primary": "#3B3B3B",  # Dark grey
        "text_secondary": "#5C5C5C"  # Medium grey
    }
    
    # Define assets with OpenTransition Material 3 theme
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate a high-quality hero banner matching OpenTransition website's Material 3 design:

Subject: The provided transparent logo as the central focal point, surrounded by soft flowing wave elements and gentle geometric shapes creating a warm, supportive atmosphere

Composition: Wide shot with logo prominently centered, flowing elements in warm peachy tones moving gracefully around it, negative space on sides for text overlay, balanced composition with modern Material 3 aesthetics

Action: Gentle flowing movement with soft waves suggesting transformation and personal journey, warm uplifting energy

Location: Clean modern Material 3 digital space with warm peachy gradient background, supportive environment

Style: Material 3 design language with rounded corners (1.5rem-2rem), soft gradients from cream to peach, modern card-based aesthetic, warm and inviting, professional health-wellness app design

Lighting: Soft warm lighting with peachy glow, gentle shadows for depth following Material 3 elevation principles, warm inviting atmosphere

Camera Details: Slightly elevated perspective for modern feel, subtle depth with Material 3 layering
Materiality: Smooth gradients with cream-to-peach transitions, logo crisp and warm, overall welcoming Material 3 aesthetic

Technical Specifications:
Aspect Ratio: 16:9
Resolution: 1920x1080
Color Palette: PRIMARY {color_scheme['primary']} (warm orange), GRADIENTS from {color_scheme['background_light']} (cream) through {color_scheme['background_peach']} (light peach) to {color_scheme['surface']} (peachy cream), accent {color_scheme['secondary']} (golden orange)

Requirements:
- Material 3 design language throughout
- Soft peachy gradient backgrounds
- Rounded corners and soft shadows
- Logo clearly visible and prominent
- Warm, supportive, inclusive design
- Modern health-tech aesthetic
- Matches OpenTransition website exactly

IMPORTANT: The reference image is the brand logo. Use the EXACT color scheme from OpenTransition website - warm oranges and peachy creams, NOT traditional trans flag colors."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate a high-quality Instagram post matching OpenTransition website's Material 3 design:

Subject: The provided brand logo as main element, complemented by soft flowing elements in warm peachy tones creating engaging social presence

Composition: Centered logo with balanced surrounding elements using Material 3 principles, Instagram square format, warm gradient background

Action: Gentle presentation with soft flowing elements suggesting support and warmth

Location: Warm Material 3 social media environment with peachy gradient

Style: Material 3 design with rounded corners, soft peachy gradients matching OpenTransition website, modern supportive aesthetic

Lighting: Soft warm peachy lighting, inviting and eye-catching Material 3 glow

Camera Details: Direct frontal view optimized for mobile, clear Material 3 presentation
Materiality: Smooth peachy gradients, logo crisp and warm, premium Material 3 social presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1080x1080
Color Palette: PRIMARY {color_scheme['primary']}, gradients {color_scheme['background_light']} to {color_scheme['surface']}, accent {color_scheme['secondary']}

Requirements:
- Material 3 design language
- Warm peachy gradient backgrounds
- Rounded corners (1.5rem radius)
- Soft shadows
- Logo clearly visible
- OpenTransition website color scheme

IMPORTANT: Use OpenTransition colors - warm oranges ({color_scheme['primary']}) and peachy creams, NOT trans flag colors."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate a high-quality Instagram story matching OpenTransition website's Material 3 design:

Subject: The provided brand logo prominently displayed with vertical-optimized flowing elements in warm peachy tones

Composition: Vertical layout with logo in upper-middle, text-safe zones, flowing peachy gradient background using Material 3 principles

Action: Gentle uplifting elements in warm peachy tones suggesting support

Location: Vertical mobile Material 3 environment with warm gradient

Style: Material 3 mobile-first design, warm peachy aesthetics matching OpenTransition, modern supportive feel

Lighting: Soft warm peachy lighting optimized for mobile viewing, supportive Material 3 glow

Camera Details: Vertical mobile perspective, Material 3 optimized
Materiality: Smooth peachy gradient, logo warm and clear, Material 3 mobile aesthetic

Technical Specifications:
Aspect Ratio: 9:16
Resolution: 1080x1920
Color Palette: PRIMARY {color_scheme['primary']}, peachy gradients {color_scheme['background_light']} to {color_scheme['background_peach']}, accent {color_scheme['secondary']}

Requirements:
- Material 3 mobile design
- Warm peachy gradients
- Rounded Material 3 elements
- Logo visible
- OpenTransition color scheme

IMPORTANT: Use warm oranges and peachy creams from OpenTransition website."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate a high-quality Facebook cover matching OpenTransition website's Material 3 design:

Subject: The provided brand logo integrated into wide Material 3 cover with flowing peachy elements

Composition: Ultra-wide layout with logo positioned strategically, Material 3 flowing elements, profile picture safe zone

Action: Gentle flowing presentation with warm peachy waves suggesting transformation

Location: Wide Material 3 Facebook environment with peachy gradient

Style: Material 3 wide-format design, warm peachy aesthetics from OpenTransition website, modern supportive feel

Lighting: Warm peachy lighting across wide format, Material 3 elevation

Camera Details: Wide Material 3 perspective
Materiality: Smooth peachy gradients, logo warm and prominent, Material 3 aesthetic

Technical Specifications:
Aspect Ratio: 21:9
Color Palette: PRIMARY {color_scheme['primary']}, gradients {color_scheme['background_light']} through {color_scheme['background_peach']} to {color_scheme['surface']}

Requirements:
- Material 3 design
- Warm peachy gradients
- Rounded corners
- Logo prominently featured
- OpenTransition color scheme

IMPORTANT: Match OpenTransition website - warm oranges and peachy creams."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate a high-quality Twitter header matching OpenTransition website's Material 3 design:

Subject: The provided brand logo integrated into Material 3 Twitter header with peachy flowing elements

Composition: Ultra-wide layout (for 3:1 cropping), logo right-of-center, Material 3 flowing elements, profile safe zone left

Action: Uplifting warm peachy elements suggesting support

Location: Material 3 Twitter environment with peachy gradient

Style: Material 3 Twitter design, warm peachy OpenTransition aesthetics, modern supportive

Lighting: Warm peachy Material 3 lighting

Camera Details: Wide Material 3 header perspective
Materiality: Smooth peachy gradients, warm logo, Material 3 social presence

Technical Specifications:
Aspect Ratio: 21:9 (will be cropped to 3:1)
Color Palette: PRIMARY {color_scheme['primary']}, peachy gradients {color_scheme['background_light']} to {color_scheme['surface']}

Requirements:
- Material 3 design
- Warm peachy gradients
- Logo visible with warmth
- OpenTransition color scheme

NOTE: Will be center-cropped to Twitter 3:1

IMPORTANT: Use OpenTransition colors - warm oranges and peachy creams."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": f"""Generate a high-quality LinkedIn banner matching OpenTransition website's Material 3 design:

Subject: The provided brand logo in professional Material 3 LinkedIn banner with peachy elements

Composition: Ultra-wide professional layout (for 4:1 cropping), logo right side, Material 3 aesthetics, professional yet warm

Action: Professional presentation with subtle warm peachy elements

Location: Material 3 LinkedIn environment with subtle peachy gradient

Style: Professional Material 3 health-tech design, warm peachy accents from OpenTransition, modern supportive

Lighting: Professional warm Material 3 lighting with peachy undertones

Camera Details: Wide professional Material 3 perspective
Materiality: Subtle peachy gradients, professional warm logo, Material 3 health-tech

Technical Specifications:
Aspect Ratio: 21:9 (will be cropped to 4:1)
Color Palette: PRIMARY {color_scheme['primary']}, subtle gradients {color_scheme['background_light']} to {color_scheme['surface']}, professional warmth

Requirements:
- Professional Material 3 design
- Subtle warm peachy tones
- Logo prominently featured
- Health-tech credibility with warmth
- OpenTransition color scheme

NOTE: Will be center-cropped to LinkedIn 4:1

IMPORTANT: Professional but use OpenTransition warm oranges and peachy tones."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate a high-quality profile picture matching OpenTransition website's Material 3 design:

Subject: The provided brand logo optimized for circular profile use, warm peachy Material 3 background

Composition: Perfectly centered for circular cropping, Material 3 circular-safe design with warm background

Action: Welcoming warm presentation

Location: Circular Material 3 profile environment with peachy background

Style: Clean Material 3 profile aesthetic with warm peachy tones from OpenTransition

Lighting: Warm peachy Material 3 lighting ensuring visibility

Camera Details: Centered circular-crop optimized Material 3 view
Materiality: Warm peachy background, logo sharp and warm, Material 3 profile presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1024x1024
Color Palette: Warm background gradient {color_scheme['background_light']} to {color_scheme['background_peach']}, logo warm

Requirements:
- Material 3 circular-safe design
- Warm peachy background
- Logo clear at small sizes
- OpenTransition color scheme

IMPORTANT: Warm peachy background matching OpenTransition website."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "prompt": f"""Generate a high-quality mobile app icon matching OpenTransition website's Material 3 design:

Subject: The provided brand logo simplified for app icon, warm peachy Material 3 background

Composition: Centered for square app icon, logo simplified for tiny sizes, Material 3 rounded-safe design

Action: Welcoming warm static presentation

Location: Mobile app icon environment with warm peachy Material 3 gradient

Style: Modern Material 3 app icon aesthetic with warm peachy tones from OpenTransition website

Lighting: Bright appealing Material 3 lighting with warm peachy glow

Camera Details: Direct centered Material 3 app icon view
Materiality: Warm peachy gradient background, logo simplified but clear, premium Material 3 app presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1024x1024 (iOS standard)
Color Palette: Warm gradient {color_scheme['background_light']} through {color_scheme['background_peach']} to {color_scheme['surface']}, primary {color_scheme['primary']}

Requirements:
- Material 3 app icon design
- Warm peachy gradient background
- Logo simplified and clear at tiny sizes
- Rounded corner-safe
- OpenTransition color scheme

IMPORTANT: Warm peachy Material 3 app icon matching OpenTransition website exactly."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "prompt": f"""Generate a high-quality app splash screen matching OpenTransition website's Material 3 design:

Subject: The provided brand logo as welcoming element on Material 3 splash screen with flowing peachy waves

Composition: Vertical mobile splash layout, logo centered, Material 3 flowing peachy elements creating welcoming atmosphere

Action: Gentle flowing peachy waves suggesting safe welcoming space

Location: Mobile Material 3 splash environment with warm peachy gradient

Style: Modern Material 3 splash aesthetic with warm peachy gradients from OpenTransition website, welcoming first impression

Lighting: Soft warm peachy Material 3 lighting for app launch, welcoming glow

Camera Details: Vertical mobile Material 3 full-screen perspective
Materiality: Smooth peachy gradients, logo warm and welcoming, Material 3 premium app experience

Technical Specifications:
Aspect Ratio: 9:16
Resolution: 1080x1920
Color Palette: Warm gradient {color_scheme['background_light']} through {color_scheme['background_peach']} to {color_scheme['surface']}, primary {color_scheme['primary']}

Requirements:
- Material 3 splash design
- Warm peachy flowing gradients
- Logo centered and welcoming
- Creates warm first impression
- OpenTransition color scheme

IMPORTANT: Match OpenTransition website splash with warm peachy Material 3 gradients."""
        },
        {
            "name": "community_banner",
            "aspect_ratio": "16:9",
            "prompt": f"""Generate a high-quality community banner matching OpenTransition website's Material 3 design:

Subject: The provided brand logo with Material 3 community elements suggesting connection, flowing peachy waves representing unity

Composition: Wide community-focused layout with logo and abstract connection elements, Material 3 peachy flowing design

Action: Flowing peachy waves suggesting community connection and mutual support

Location: Material 3 community section with warm peachy gradient background

Style: Warm Material 3 community aesthetic with peachy flowing gradients from OpenTransition website, modern supportive feel

Lighting: Warm peachy Material 3 lighting creating sense of community togetherness

Camera Details: Wide Material 3 community perspective
Materiality: Flowing peachy gradients, logo warm and prominent, Material 3 community aesthetic

Technical Specifications:
Aspect Ratio: 16:9
Resolution: 1920x1080
Color Palette: PRIMARY {color_scheme['primary']}, flowing gradients {color_scheme['background_light']} through {color_scheme['background_peach']} to {color_scheme['surface']}, accent {color_scheme['secondary']}

Requirements:
- Material 3 community design
- Warm flowing peachy gradients
- Suggests connection and community
- Logo prominently featured
- OpenTransition color scheme

IMPORTANT: Use OpenTransition warm oranges and peachy gradients for community feeling."""
        }
    ]
    
    print(f"🚀 Regenerating {len(assets)} assets with OpenTransition Material 3 theme...\n")
    print("🎨 Using warm orange & peachy cream color scheme\n")
    print("Color scheme:")
    for key, value in color_scheme.items():
        print(f"  {key}: {value}")
    print()
    
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
    
    print(f"\n{'='*60}")
    print(f"✅ OpenTransition Material 3 Assets Complete!")
    print(f"{'='*60}")
    print(f"Total assets regenerated: {len(all_generated_files)}")
    print(f"\nColor scheme: Warm orange (#E68322) with peachy cream gradients")
    print(f"Style: Material 3 with rounded corners, soft shadows, flowing gradients")
    print(f"Matches: OpenTransition website https://shelbeely.github.io/OpenTransition-website/")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    regenerate_opentransition_assets()
