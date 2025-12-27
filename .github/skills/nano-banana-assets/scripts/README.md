# Helper Scripts for Nano Banana Assets Skill

This directory contains utility scripts for generating and processing assets using OpenRouter's Nano Banana Pro model.

## Available Scripts

### 1. `generate_asset.py` - Basic Asset Generation

Generate a single asset with full control over parameters.

**Usage:**
```bash
python generate_asset.py "Modern hero banner" "16:9" "1920x1080"
```

**Features:**
- Single asset generation
- Asset pack generation
- Image editing capabilities
- Reference image support

---

### 2. `generate_asset.sh` - Bash Version

Lightweight bash script for quick asset generation.

**Usage:**
```bash
./generate_asset.sh "Icon design" "1:1" "512x512"
```

**Note:** Requires `jq` for JSON parsing.

---

### 3. `generate_with_transparency.py` ⭐ **NEW**

**Fully automated transparent asset generation!**

Automatically generates with chroma key background and removes it with rembg.

**Usage:**
```bash
python generate_with_transparency.py "Kawaii sticker" "1:1" "1024x1024"
```

**What it does:**
1. ✅ Generates with #00FF00 chroma key (no fake checkered patterns)
2. ✅ Removes background with rembg (AI-powered)
3. ✅ Outputs transparent RGBA PNG
4. ✅ Saves both transparent and original versions

**Requirements:**
```bash
pip install rembg requests
```

**Output:**
- `asset_1_transparent.png` - With alpha transparency
- `asset_1_original_green.png` - With green background (for reference)

---

### 4. `batch_generate.py` ⭐ **NEW**

Generate multiple assets at once from various sources.

**Usage:**
```bash
# From JSON config file
python batch_generate.py --config example_batch_config.json

# From command-line prompts
python batch_generate.py --prompts "Logo" "Banner" "Icon" --transparent

# From text file (one prompt per line)
python batch_generate.py --file prompts.txt --aspect-ratio 1:1

# With custom output and colors
python batch_generate.py --prompts "Icon 1" "Icon 2" -o icons --colors "#FF0000" "#00FF00"
```

**Features:**
- Batch generation from JSON, command-line, or text file
- Optional automatic transparency removal
- Progress tracking and error handling
- Organized output with custom naming
- Resume capability for interrupted batches

**Config file format** (`example_batch_config.json`):
```json
{
  "assets": [
    {
      "name": "hero_banner",
      "prompt": "Modern tech startup hero banner",
      "aspect_ratio": "16:9",
      "resolution": "1920x1080",
      "color_palette": ["#667EEA", "#764BA2"]
    }
  ]
}
```

---

### 5. `remove_backgrounds.py` ⭐ **NEW**

Post-process existing images to remove backgrounds.

**Usage:**
```bash
# Single file with rembg (AI-powered)
python remove_backgrounds.py my_image.png

# Multiple files
python remove_backgrounds.py img1.png img2.png img3.png

# All PNG files in directory
python remove_backgrounds.py --directory ./images/

# With chroma key removal (for #00FF00 green backgrounds)
python remove_backgrounds.py --chroma-key "#00FF00" image.png

# Recursive with custom output
python remove_backgrounds.py -d ./input/ -o ./output/ --recursive
```

**Features:**
- AI-powered background removal with rembg
- Chroma key color removal
- Batch directory processing
- Recursive directory support
- Custom output directory

**Requirements:**
```bash
pip install rembg Pillow
```

---

## Quick Start Examples

### Generate a Single Transparent Sticker
```bash
python generate_with_transparency.py "Cute cat sticker" "1:1" "1024x1024"
```

### Batch Generate Icon Set
```bash
python batch_generate.py --prompts \
  "Home icon" \
  "Settings icon" \
  "Profile icon" \
  "Search icon" \
  --transparent \
  --aspect-ratio 1:1 \
  --resolution 512x512 \
  --output icon_set
```

### Remove Backgrounds from Existing Images
```bash
python remove_backgrounds.py --directory ./generated_assets/
```

### Generate Asset Pack from Config
```bash
python batch_generate.py --config example_batch_config.json --transparent
```

---

## Environment Setup

### Install Required Dependencies
```bash
# For basic generation
pip install requests

# For transparent assets (recommended)
pip install rembg requests

# For chroma key removal
pip install Pillow

# All dependencies
pip install rembg requests Pillow
```

### Set API Key
```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

---

## Transparency Workflow

### Understanding the Process

The Gemini model does NOT support true alpha transparency. Our solution:

1. **Generate with chroma key background (#00FF00)**
   - Avoids fake checkered patterns
   - Clean, uniform color for easy removal

2. **Remove background with rembg (AI-powered)**
   - High-quality edge detection
   - Handles fine details (hair, fur, etc.)
   - Fully automated

### Automated Workflow (Recommended)
```bash
# One command for everything!
python generate_with_transparency.py "Your prompt" "1:1" "1024x1024"
```

### Manual Workflow
```bash
# Step 1: Generate with chroma key
python generate_asset.py "Your prompt with solid bright green (#00FF00) background"

# Step 2: Remove background
python remove_backgrounds.py generated_asset.png
```

---

## Tips & Best Practices

### For Best Results
- Be specific in prompts (use the Six-Element Framework)
- For transparency, always use the automated script or chroma key approach
- Use batch_generate.py for multiple similar assets
- Set appropriate resolution for your use case

### Common Resolutions
- **Icons**: 512x512, 1024x1024
- **Social Media Posts**: 1080x1080
- **Banners**: 1920x1080
- **Headers**: 1500x500

### Color Palettes
Always specify hex codes for consistent branding:
```bash
--colors "#667EEA" "#764BA2" "#F093FB"
```

---

## Troubleshooting

### "rembg not installed"
```bash
pip install rembg
```

### "OPENROUTER_API_KEY not found"
```bash
export OPENROUTER_API_KEY="your-key-here"
```

### "Image quality not good"
- Use higher resolution
- Be more specific in your prompt
- Use the Six-Element Framework (Subject, Composition, Action, Location, Style, Lighting)

### "Background not fully removed"
- The AI model works best with clean chroma key backgrounds
- Try adjusting chroma key tolerance in manual removal
- Use rembg for better edge detection

---

## Support

For more information, see:
- Main skill documentation: `../SKILL.md`
- API reference: `../references/api-reference.md`
- Prompt templates: `../references/prompt-templates.md`

---

**Generated assets are for testing and development. Review OpenRouter's usage terms for production use.**
