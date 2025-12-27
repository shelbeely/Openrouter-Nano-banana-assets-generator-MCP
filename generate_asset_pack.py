#!/usr/bin/env python3
"""
Generate a comprehensive asset pack using the processed logo
"""
import os
import sys
import json
import base64
import requests
from pathlib import Path
from typing import List, Dict, Any

# Configuration
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"

def image_to_base64_url(image_path: str) -> str:
    """Convert image file to base64 data URL"""
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    # Determine mime type from extension
    ext = Path(image_path).suffix.lower()
    mime_type = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
    }.get(ext, 'image/png')
    
    return f"data:{mime_type};base64,{image_data}"

def call_openrouter(prompt: str, logo_base64: str, aspect_ratio: str = "1:1") -> Dict[str, Any]:
    """Call OpenRouter API to generate an asset"""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
        "X-Title": "Nano Banana Assets Generator"
    }
    
    # Build content with logo reference
    content = [
        {
            "type": "image_url",
            "image_url": {
                "url": logo_base64
            }
        },
        {
            "type": "text",
            "text": prompt
        }
    ]
    
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
    
    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    return response.json()

def save_generated_images(response: Dict[str, Any], asset_name: str, output_dir: Path) -> List[str]:
    """Extract and save generated images from API response"""
    saved_files = []
    
    message = response.get('choices', [{}])[0].get('message', {})
    images = message.get('images', [])
    
    if not images:
        print(f"⚠️  No images generated for {asset_name}")
        return saved_files
    
    for idx, img in enumerate(images):
        # Get the base64 data URL
        image_url = img.get('image_url', {}).get('url', '') or img.get('url', '')
        
        if not image_url or not image_url.startswith('data:'):
            continue
        
        # Extract base64 data
        base64_data = image_url.split(',', 1)[1]
        image_data = base64.b64decode(base64_data)
        
        # Save to file
        filename = f"{asset_name}_{idx + 1}.png"
        filepath = output_dir / filename
        
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        saved_files.append(str(filepath))
        print(f"   ✅ Saved: {filename}")
    
    return saved_files

def generate_asset_pack():
    """Generate a complete asset pack with the processed logo"""
    
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
    print(f"✅ Logo loaded: {logo_path}")
    
    # Define asset specifications for inclusive transgender transition tracking app
    assets = [
        {
            "name": "hero_banner",
            "aspect_ratio": "16:9",
            "prompt": """Generate a high-quality hero banner for an inclusive transgender transition tracking app website with the following specifications:

Subject: The provided transparent logo as the central focal point, surrounded by gentle flowing abstract elements (soft gradient waves, flowing connecting lines, uplifting particles) creating a supportive, empowering, and affirming atmosphere that celebrates personal journey and growth

Composition: Wide shot with logo prominently centered, flowing elements moving gracefully around it suggesting transformation and progress, negative space on sides for text overlay about empowerment and support, balanced and harmonious visual weight

Action: Gentle sense of transformation and personal growth with elements flowing upward and forward, suggesting positive journey, hope, progress, and self-discovery

Location: Warm, welcoming digital space with inclusive atmosphere, safe and affirming environment, modern supportive app context

Style: Modern inclusive design with warm, affirming aesthetic suitable for health/wellness app, gentle gradients representing transition and transformation, contemporary supportive design language, professional yet approachable and compassionate

Lighting: Soft warm welcoming lighting creating safe space, gentle highlights on logo conveying hope and affirmation, comforting glow suggesting support and community

Camera Details: Slightly elevated perspective suggesting empowerment and growth, gentle depth creating inclusive welcoming space
Materiality: Logo maintains clarity and warmth, gradient elements have soft caring quality, overall supportive and affirming aesthetic

Technical Specifications:
Aspect Ratio: 16:9
Resolution: 1920x1080
Color Palette: Use inclusive, affirming colors - transgender flag colors (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples (#A78BFA, #C084FC), warm compassionate tones, gentle rainbow pride accents

Requirements:
- Professional health/wellness app quality
- Logo must be clearly visible and prominent
- Warm, supportive, and inclusive design
- Affirming and empowering visual language
- Optimized for website hero section celebrating transgender individuals
- Creates sense of safety, support, and community
- Suitable for personal health tracking context

IMPORTANT: The reference image is the brand logo with transparent background. Integrate it prominently into a supportive, inclusive design that celebrates transgender identity and personal growth journey."""
        },
        {
            "name": "instagram_post",
            "aspect_ratio": "1:1",
            "prompt": """Generate a high-quality Instagram post for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo as the main element, complemented by supportive design elements (gentle flowing shapes, affirming patterns, uplifting elements) creating an empowering and inclusive social media presence

Composition: Centered logo with balanced supportive surrounding elements, Instagram-optimized square format, visually appealing and affirming, scroll-stopping yet compassionate

Action: Gentle presentation with uplifting visual interest suggesting support, community, and empowerment

Location: Warm inclusive social media environment, safe supportive digital community space

Style: Contemporary inclusive social aesthetic, supportive yet engaging, modern affirming brand presentation celebrating transgender community, warm and welcoming

Lighting: Soft warm inviting social media lighting, compassionate and eye-catching, supportive glow creating safe space

Camera Details: Direct frontal view optimized for mobile screens, clear focus on supportive brand identity
Materiality: Logo crisp and warm, background elements smooth and caring, inclusive social presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1080x1080
Color Palette: Inclusive transgender-affirming colors - trans flag colors (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples (#A78BFA, #C084FC), gentle pride rainbow accents, warm compassionate tones

Requirements:
- Instagram-ready quality for health/wellness app
- Logo clearly visible and prominent
- Affirming and empowering for transgender community
- Supportive and inclusive design language
- Optimized for mobile viewing
- Creates sense of community and validation

IMPORTANT: The reference image is the brand logo. Feature it prominently in an inclusive, affirming Instagram design celebrating transgender identity and personal journey."""
        },
        {
            "name": "instagram_story",
            "aspect_ratio": "9:16",
            "prompt": """Generate a high-quality Instagram story for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo prominently displayed with vertical-optimized supportive design elements creating an affirming mobile story experience celebrating personal journey

Composition: Vertical layout optimized for mobile stories, logo in upper-middle section, text-safe zones at top and bottom for empowering messages, flowing vertical composition suggesting growth and transformation

Action: Gentle uplifting elements suggesting personal progress, transformation journey, and community support

Location: Vertical mobile-first inclusive environment, supportive social story space, safe affirming context

Style: Modern inclusive Instagram story aesthetic, supportive mobile-first design, engaging and affirming, celebrates transgender identity with warmth and compassion

Lighting: Soft warm appealing mobile lighting, optimized for story viewing with supportive glow, compassionate presentation

Camera Details: Vertical mobile perspective, optimized for full-screen story viewing with welcoming feel
Materiality: Sharp caring logo, smooth supportive elements, inclusive mobile aesthetic

Technical Specifications:
Aspect Ratio: 9:16
Resolution: 1080x1920
Color Palette: Transgender-affirming colors - trans flag (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples, gentle pride accents, warm inclusive tones

Requirements:
- Instagram story-ready quality for health/wellness app
- Vertical mobile-optimized
- Logo clearly visible
- Warm, supportive, and inclusive
- Affirming for transgender community
- Engaging for story viewers celebrating their journey

IMPORTANT: The reference image is the brand logo. Design a supportive vertical story format celebrating transgender identity and personal growth."""
        },
        {
            "name": "facebook_cover",
            "aspect_ratio": "21:9",
            "prompt": """Generate a high-quality Facebook cover banner for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo integrated into a wide supportive cover design with gentle flowing elements celebrating transgender identity and personal journey

Composition: Ultra-wide horizontal layout, logo positioned strategically with supportive elements, profile picture safe zone on left considered, balanced wide composition suggesting transformation and growth

Action: Gentle flowing presentation conveying support, community, empowerment, and affirming transgender individuals' journeys

Location: Wide supportive Facebook cover environment, inclusive health/wellness social presence, safe affirming community space

Style: Inclusive Facebook-appropriate design, warm and supportive, wide-format optimized celebrating transgender identity with compassion and affirmation

Lighting: Warm supportive lighting across wide format, gentle affirming glow, compassionate presentation

Camera Details: Wide welcoming perspective, inclusive depth
Materiality: Logo clear and supportive, background elements flowing and caring, inclusive community aesthetic

Technical Specifications:
Aspect Ratio: 21:9 (ultra-wide for Facebook cover)
Resolution: High quality wide format
Color Palette: Transgender-affirming colors - trans flag (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples, gentle pride rainbow, warm inclusive palette

Requirements:
- Facebook cover-ready quality for health/wellness app
- Wide format optimized
- Logo prominently featured with warmth
- Supportive inclusive appearance celebrating transgender community
- Profile picture safe zone considered
- Creates safe, affirming community space

IMPORTANT: The reference image is the brand logo. Create a supportive wide Facebook cover celebrating transgender identity and personal transformation."""
        },
        {
            "name": "twitter_header",
            "aspect_ratio": "21:9",
            "prompt": """Generate a high-quality Twitter header banner for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo integrated into a supportive Twitter header with affirming design elements celebrating transgender community

Composition: Wide horizontal Twitter header format, logo prominently positioned, profile picture safe zone on left considered, inclusive supportive layout

Action: Uplifting presence conveying support, community, validation, and empowerment for transgender individuals

Location: Twitter header environment, inclusive health/wellness social media presence, affirming community space

Style: Modern Twitter-appropriate inclusive design, warm and supportive, celebrates transgender identity with compassion

Lighting: Warm supportive lighting optimized for Twitter display, gentle affirming glow

Camera Details: Wide welcoming header perspective, inclusive presentation
Materiality: Clear supportive logo, caring background, inclusive social presence

Technical Specifications:
Aspect Ratio: 3:1 (Twitter header format)
Resolution: High quality for Twitter display
Color Palette: Transgender-affirming colors - trans flag (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples, gentle pride accents

Requirements:
- Twitter header-ready quality for health/wellness app
- Wide format optimized
- Logo clearly visible with warmth
- Supportive affirming appearance for transgender community
- Profile picture safe zone considered
- Creates welcoming inclusive space

IMPORTANT: The reference image is the brand logo. Create a supportive Twitter header celebrating transgender identity and personal journey."""
        },
        {
            "name": "linkedin_banner",
            "aspect_ratio": "21:9",
            "prompt": """Generate a high-quality LinkedIn banner for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo integrated into a professional yet compassionate LinkedIn banner suitable for health-tech and inclusive healthcare presence

Composition: Wide professional LinkedIn banner format, logo strategically positioned, healthcare-appropriate layout, professional yet caring visual hierarchy

Action: Professional presentation conveying both credibility and compassion, supporting transgender health and wellness

Location: Professional LinkedIn environment, health-tech and inclusive healthcare B2B presence

Style: Professional healthcare-tech design with inclusive compassionate elements, appropriate for health/wellness industry, modern supportive aesthetic

Lighting: Professional warm lighting, trustworthy yet caring presentation, supportive glow

Camera Details: Wide professional banner perspective, healthcare industry depth
Materiality: Logo crisp and professional with warmth, background sophisticated yet supportive, health-tech appropriate

Technical Specifications:
Aspect Ratio: 4:1 (LinkedIn banner format)
Resolution: High quality for professional LinkedIn display
Color Palette: Professional health-tech colors with transgender-affirming accents - supportive purples (#A78BFA, #C084FC), trans flag accents (light blue #5BCEFA, pink #F5A9B8), clean professional palette

Requirements:
- LinkedIn banner-ready quality for health-tech industry
- Professional healthcare appearance with inclusive values
- Logo prominently featured
- Appropriate for B2B healthcare/wellness partnerships
- Conveys both credibility and compassion
- Suitable for inclusive health-tech context

IMPORTANT: The reference image is the brand logo. Create a professional health-tech LinkedIn banner that balances credibility with inclusive, supportive values for transgender healthcare."""
        },
        {
            "name": "profile_picture",
            "aspect_ratio": "1:1",
            "prompt": """Generate a high-quality profile picture for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo optimized for circular profile picture use, clean, warm, and immediately recognizable as supportive transgender health app

Composition: Perfectly centered for circular cropping, logo clearly visible at small sizes with supportive visual warmth, circular-safe inclusive design

Action: Welcoming iconic brand representation suggesting support and community

Location: Isolated warm background, inclusive profile picture environment

Style: Clean supportive profile picture aesthetic, optimized for recognition at small sizes, warm and affirming visual language

Lighting: Warm inviting lighting, ensuring visibility and warmth at all sizes, gentle supportive glow

Camera Details: Direct centered view, circular-crop optimized with caring presentation
Materiality: Logo sharp and warm, background clean and supportive, inclusive presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1024x1024 (high quality for profile use)
Color Palette: Transgender-affirming colors with warmth - trans flag accents (light blue #5BCEFA, pink #F5A9B8), supportive purples, gentle inclusive tones

Requirements:
- Profile picture-ready quality for health/wellness app
- Circular crop-safe design
- Logo clearly visible at small sizes (40px-200px)
- Warm supportive background
- Recognizable inclusive brand representation
- Conveys safety, support, and affirmation

IMPORTANT: The reference image is the brand logo. Optimize it for circular profile picture use celebrating transgender identity with warmth and support."""
        },
        {
            "name": "app_icon",
            "aspect_ratio": "1:1",
            "prompt": """Generate a high-quality mobile app icon for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo simplified and optimized for mobile app icon use, instantly recognizable as supportive transgender health app

Composition: Perfectly centered for square app icon, logo simplified for small sizes (especially 60x60 to 180x180), clear and recognizable, app icon-safe design

Action: Welcoming static representation inviting users to track their journey

Location: Isolated on warm supportive background or gradient, mobile home screen environment

Style: Modern mobile app icon aesthetic, warm and inviting, optimized for instant recognition on mobile devices, inclusive visual language

Lighting: Bright appealing app icon lighting, warm and inviting glow, optimized for home screen visibility

Camera Details: Direct centered app icon view, mobile-optimized
Materiality: Logo simplified but warm and clear, background vibrant yet supportive, premium app presence

Technical Specifications:
Aspect Ratio: 1:1
Resolution: 1024x1024 (iOS App Store standard)
Color Palette: Transgender-affirming warm colors - trans flag inspired (light blue #5BCEFA, pink #F5A9B8), supportive purples, gentle inclusive gradient

Requirements:
- iOS/Android app icon-ready quality
- Square format with rounded corner-safe design
- Logo simplified and clearly visible at tiny sizes (60px-180px)
- Warm inviting appearance
- Stands out on mobile home screen
- Instantly recognizable as supportive transgender health app
- Conveys safety, warmth, and empowerment

IMPORTANT: The reference image is the brand logo. Simplify and optimize it for mobile app icon celebrating transgender identity with immediate visual warmth."""
        },
        {
            "name": "app_splash_screen",
            "aspect_ratio": "9:16",
            "prompt": """Generate a high-quality mobile app splash screen for an inclusive transgender transition tracking app with the following specifications:

Subject: The provided brand logo as central welcoming element on app launch screen with gentle supportive visual elements creating first impression of safety and affirmation

Composition: Vertical mobile splash screen layout, logo centered with breathing room, supportive elements creating welcoming first experience, app launch-optimized

Action: Gentle welcoming presentation that immediately conveys support, safety, and empowerment to transgender users starting their app experience

Location: Mobile app splash screen environment, first-impression context, welcoming entry point

Style: Modern mobile app splash aesthetic, warm and immediately reassuring, creates safe affirming first impression celebrating transgender identity

Lighting: Soft warm welcoming lighting for app launch, gentle glow suggesting safe space and support

Camera Details: Vertical mobile full-screen perspective, welcoming presentation
Materiality: Logo clear and warm on launch, background gentle and supportive, premium app experience

Technical Specifications:
Aspect Ratio: 9:16
Resolution: 1080x1920 (mobile splash screen)
Color Palette: Transgender-affirming warm colors - trans flag (light blue #5BCEFA, pink #F5A9B8, white #FFFFFF), supportive purples, gentle gradient

Requirements:
- Mobile app splash screen-ready quality
- Vertical full-screen optimized
- Logo prominently centered and welcoming
- Creates immediate sense of safety and support
- Warm affirming first impression
- Celebrates transgender identity with compassion
- Loads quickly and sets supportive tone

IMPORTANT: The reference image is the brand logo. Create a warm, welcoming app splash screen that immediately makes transgender users feel safe, seen, and supported."""
        },
        {
            "name": "youtube_thumbnail",
            "aspect_ratio": "16:9",
            "prompt": """Generate a high-quality YouTube thumbnail with the following specifications:

Subject: The provided brand logo integrated into an eye-catching YouTube thumbnail design with engaging visual elements

Composition: YouTube thumbnail layout with logo visible, space for text overlay, attention-grabbing composition, platform-optimized

Action: Engaging presentation designed to attract clicks while maintaining professionalism

Location: YouTube thumbnail environment, video content context

Style: Professional yet engaging YouTube aesthetic, eye-catching while maintaining brand integrity, click-worthy design

Lighting: Bright appealing lighting optimized for thumbnail visibility, professional glow

Camera Details: Direct engaging perspective, thumbnail-optimized
Materiality: Logo clear and professional, background vibrant and appealing

Technical Specifications:
Aspect Ratio: 16:9
Resolution: 1280x720 (YouTube standard)
Color Palette: Professional brand colors with high contrast for visibility

Requirements:
- YouTube thumbnail-ready quality
- Eye-catching and professional
- Logo clearly visible
- Space for text overlay
- Optimized for small preview sizes
- Click-worthy while professional

IMPORTANT: The reference image is the brand logo. Create an engaging YouTube thumbnail that attracts viewers while maintaining professional brand identity."""
        }
    ]
    
    print(f"\n🚀 Generating {len(assets)} assets for inclusive transgender transition tracking app...\n")
    print("🏳️‍⚧️ Creating supportive, affirming asset pack celebrating transgender identity\n")
    
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
    print(f"✅ Asset Pack Generation Complete!")
    print(f"{'='*60}")
    print(f"Total assets generated: {len(all_generated_files)}")
    print(f"Output directory: {output_dir}")
    print(f"\nGenerated assets:")
    for file in all_generated_files:
        print(f"  - {Path(file).name}")
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    generate_asset_pack()
