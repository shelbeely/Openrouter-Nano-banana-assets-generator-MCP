# Nano Banana Assets Skill - Usage Demonstration

This document demonstrates how to use the **nano-banana-assets** skill to generate professional web assets using AI.

## Overview

The nano-banana-assets skill is available at `.github/skills/nano-banana-assets/` and enables AI agents (like GitHub Copilot) to generate high-quality images, icons, banners, and other visual assets using OpenRouter's Nano Banana Pro model.

## How It Works

When you're working with GitHub Copilot and need to generate visual assets, you can use natural language to request them. The skill automatically:

1. Loads when asset generation is needed
2. Uses your `OPENROUTER_API_KEY` from the environment
3. Calls the OpenRouter API with the appropriate model
4. Returns generated images as base64-encoded PNG/JPEG files

## Example Usage Scenarios

### Scenario 1: Generate a Simple Icon

**User Request:**
```
"Generate a modern home icon for my website navigation"
```

**What the Skill Does:**
1. Interprets your request
2. Builds an appropriate prompt with specifications
3. Calls OpenRouter API with aspect ratio 1:1
4. Returns a 512x512 professional icon
5. Saves it to your project

**Expected Result:**
- Clean, modern home icon
- Suitable for web navigation
- Professional quality
- Properly sized and formatted

### Scenario 2: Create a Social Media Kit

**User Request:**
```
"I need a social media kit for my eco-friendly coffee brand. Include Instagram post, story, and Facebook cover. Use green and brown colors."
```

**What the Skill Does:**
1. Recognizes this as an asset pack request
2. Generates multiple assets with consistent branding:
   - Instagram post (1:1, 1080x1080)
   - Instagram story (9:16, 1080x1920)
   - Facebook cover (wide banner)
3. Maintains visual consistency across all assets
4. Uses the specified color palette (#2ECC71, #8B4513, etc.)

**Expected Result:**
- 3 professionally designed assets
- Consistent branding and style
- Proper dimensions for each platform
- Color-coordinated with brand guidelines

### Scenario 3: Edit an Existing Image

**User Request:**
```
"Make this banner warmer and add a subtle gradient overlay"
[Provides image file]
```

**What the Skill Does:**
1. Accepts the source image
2. Applies editing instructions:
   - Adjusts color temperature (warmer tones)
   - Adds gradient overlay
3. Preserves original composition
4. Returns edited high-quality result

**Expected Result:**
- Image with warmer color tones
- Subtle gradient overlay applied
- Original subjects and layout preserved
- Professional editing quality

### Scenario 4: Generate a Hero Banner

**User Request:**
```
"Create a hero banner for a tech startup with blue and purple gradient, 16:9 aspect ratio, modern and professional"
```

**What the Skill Does:**
1. Builds detailed prompt with specifications
2. Sets aspect ratio to 16:9
3. Sets resolution to 1920x1080
4. Includes color palette (#667EEA, #764BA2)
5. Generates modern, professional design

**Expected Result:**
- Widescreen banner (1920x1080)
- Blue to purple gradient background
- Modern, professional appearance
- Ready for website hero section

## Skill Features

### 1. **Single Asset Generation**
- Icons (1:1, various sizes)
- Banners (16:9, 21:9, custom)
- Backgrounds (any aspect ratio)
- UI elements
- Custom graphics

### 2. **Asset Pack Creation**
- Social media kits
- Brand identity packages
- Icon sets
- Complete marketing materials
- Consistent multi-asset generation

### 3. **Image Editing**
- Color adjustments
- Lighting and contrast
- Adding effects
- Composition changes
- Quality enhancements

### 4. **Brand Consistency**
- Multi-asset analysis
- Brand guideline compliance
- Color palette validation
- Style consistency checking
- Recommendations for improvements

## API Configuration

The skill uses the following API setup:

```json
{
  "endpoint": "https://openrouter.ai/api/v1/chat/completions",
  "model": "google/gemini-3-pro-image-preview",
  "auth": "Bearer OPENROUTER_API_KEY",
  "modalities": ["image", "text"]
}
```

### Required Environment Variable

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

Get your API key from: https://openrouter.ai/

## Supported Specifications

### Aspect Ratios
- `1:1` - Square (icons, Instagram posts)
- `16:9` - Widescreen (banners, YouTube)
- `9:16` - Vertical (stories, mobile)
- `4:3` - Traditional
- `21:9` - Ultra-wide
- Custom ratios supported

### Resolutions
- `512x512` - Small icons
- `1080x1080` - Standard square
- `1920x1080` - Full HD
- `2K` (2560x1440)
- `4K` (3840x2160)
- Custom resolutions supported

### Output Formats
- PNG (default, lossless)
- JPEG (when specified)
- Base64-encoded data URLs
- Direct file saves

## Testing the Skill Locally

### Prerequisites
1. OpenRouter API key
2. Python 3.10+ (optional, for Python scripts)
3. Internet connection

### Quick Test

```bash
# Set your API key
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Navigate to skill scripts
cd .github/skills/nano-banana-assets/scripts

# Run Python helper
python3 generate_asset.py "Modern home icon" "1:1" "512x512"

# Or use bash helper
bash generate_asset.sh "Modern home icon" "1:1" "512x512"
```

### Using the Demo Script

```bash
# Run the comprehensive demo
./demo-agent-skill.sh

# This will:
# 1. Check prerequisites
# 2. Verify API key
# 3. Run example generations
# 4. Show results
```

## Integration with GitHub Copilot

When using GitHub Copilot coding agent:

1. **Automatic Loading**: The skill loads automatically when you need asset generation
2. **Natural Language**: Just ask naturally for what you need
3. **Context-Aware**: Copilot understands your project context
4. **File Management**: Generated assets are saved to appropriate directories

### Example Interactions

```
You: "I need a logo for my app"
Copilot: *loads nano-banana-assets skill*
Copilot: *generates professional logo*
Copilot: "I've created a modern logo. Would you like any adjustments?"

You: "Create social media banners for our product launch"
Copilot: *generates complete social media kit*
Copilot: "I've created Instagram, Facebook, and Twitter banners with consistent branding."

You: "Make the hero image brighter"
Copilot: *edits existing image*
Copilot: "I've increased the brightness and enhanced the colors."
```

## Best Practices

### 1. Be Specific
- ❌ "Make an icon"
- ✅ "Create a minimalist home icon in blue (#667EEA) for website navigation, 512x512"

### 2. Provide Context
- Mention where it will be used
- Specify the target audience
- Describe desired mood/style

### 3. Use Brand Guidelines
- Provide hex color codes
- Reference existing assets
- Specify style requirements

### 4. Iterate
- Start with a base design
- Refine based on results
- Test variations

## Troubleshooting

### Issue: "API key not found"
**Solution:** Set the OPENROUTER_API_KEY environment variable

### Issue: "No images in response"
**Solution:** Check that modalities includes "image" and model supports image generation

### Issue: "Rate limit exceeded"
**Solution:** Wait and retry, or check your OpenRouter usage limits

### Issue: "Low quality output"
**Solution:** Provide more detailed prompts, add reference images, or increase resolution

## Cost Considerations

- Each API call consumes OpenRouter credits
- Cost varies by resolution and complexity
- Monitor usage at: https://openrouter.ai/activity
- Use appropriate resolutions (don't request 4K for thumbnails)

## Additional Resources

- **Skill Documentation**: `.github/skills/nano-banana-assets/README.md`
- **API Reference**: `.github/skills/nano-banana-assets/references/api-reference.md`
- **Prompt Templates**: `.github/skills/nano-banana-assets/references/prompt-templates.md`
- **OpenRouter Docs**: https://openrouter.ai/docs
- **Main README**: `README.md`

## Summary

The nano-banana-assets skill provides professional asset generation capabilities through a simple, natural language interface. It's designed to work seamlessly with GitHub Copilot and other AI agents, making high-quality visual content creation as easy as asking for it.

Just request what you need, and the skill handles the technical details of prompt engineering, API calls, and file management automatically.
