# Regenerating OpenTransition Asset Pack with Transparency and Logo Consistency

This guide explains how to properly regenerate all 10 assets using the **nano-banana-assets skill** with:
- ✅ **Transparent backgrounds** (using chroma key + rembg)
- ✅ **Logo consistency** across all assets
- ✅ **OpenTransition website style matching**

## Prerequisites

```bash
# Install rembg for automatic background removal
pip install rembg

# Verify OPENROUTER_API_KEY is set
echo $OPENROUTER_API_KEY
```

## Method 1: Using the Batch Generator (Recommended)

The skill includes `batch_generate.py` which handles everything automatically.

### Step 1: Navigate to skill scripts directory

```bash
cd .github/skills/nano-banana-assets/scripts
```

### Step 2: Ensure reference images are in place

```bash
# Should have these files:
ls -l logo_transparent.png og-image.png section-background.png
```

### Step 3: Run batch generation with transparency

```bash
# Using the provided config (adjust paths to match your structure)
python batch_generate.py \
  --config ../../../../opentransition_asset_pack_config.json \
  --transparent \
  --output ../../../../assets/generated/asset_pack_transparent
```

This will:
1. ✅ Generate each asset with #00FF00 chroma key background
2. ✅ Automatically remove background using rembg (AI-powered)
3. ✅ Save transparent PNG files (RGBA format)
4. ✅ Save original with green background for reference
5. ✅ Use reference images (logo, og-image, section-background) for consistency

## Method 2: Generate Individual Assets

For more control, generate assets one at a time:

```bash
cd .github/skills/nano-banana-assets/scripts

# Hero Banner with transparency
python generate_with_transparency.py \
  "LOGO CONSISTENCY: Use exact butterfly circle logo from first reference. NO text in logo.

Create hero banner matching OpenTransition style:
- Warm orange butterflies (#E68322)
- Peachy cream gradients (#FFF8E7, #F5E8DA)
- Organic teardrop shapes
- Golden sparkles (#F9B21E)
- Logo centered (butterfly circle only)
- Text 'OpenTransition' SEPARATE from logo" \
  "16:9" \
  "1920x1080"

# Instagram Post with transparency
python generate_with_transparency.py \
  "LOGO CONSISTENCY: Exact logo - butterfly circle only.

Instagram post OpenTransition style:
- Orange butterflies
- Peachy backgrounds
- Logo centered" \
  "1:1" \
  "1080x1080"

# Continue for all 10 assets...
```

## Output Files

For each asset, you'll get:
- `{name}_1_transparent.png` - **Final transparent RGBA PNG** (use this!)
- `{name}_1_original_green.png` - Original with green background (reference)

## Ensuring Logo Consistency

The key to logo consistency is in the prompts. **Critical instructions:**

```
LOGO CONSISTENCY RULE:
- First reference image is the EXACT logo (butterfly in circle with sparkle)
- DO NOT add "OpenTransition" text to the logo
- DO NOT modify the logo in any way
- Use this EXACT logo design consistently
- Text "OpenTransition" should be SEPARATE from logo, not part of it
```

Every prompt should include these instructions to ensure the AI doesn't generate a different logo each time.

## Troubleshooting

### Issue: API Payment Required (402)
**Solution:** Ensure your OpenRouter API key has sufficient credits

### Issue: rembg not installed
**Solution:** `pip install rembg`

### Issue: Logo looks different in each asset
**Solution:** Make logo consistency instructions more explicit in prompts, and ensure logo reference image is first in the reference array

### Issue: Background not fully transparent
**Solution:** 
- Check the generated `_transparent.png` files (should be RGBA)
- If still has artifacts, the green background might not be uniform
- Can manually refine with: `convert image.png -fuzz 5% -transparent "#00FF00" output.png`

## Verifying Transparency

```bash
# Check if file has alpha channel (should show RGBA)
file asset_1_transparent.png

# Should output: PNG image data, ..., 8-bit/color RGBA, ...
```

## Complete Workflow Summary

```bash
# 1. Install dependencies
pip install rembg

# 2. Navigate to skill directory  
cd .github/skills/nano-banana-assets/scripts

# 3. Ensure reference images are present
ls logo_transparent.png og-image.png section-background.png

# 4. Run batch generation with transparency
python batch_generate.py \
  --config ../../../../opentransition_asset_pack_config.json \
  --transparent \
  --output ../../../../assets/generated/asset_pack_transparent

# 5. Check results
ls -lh ../../../../assets/generated/asset_pack_transparent/*_transparent.png

# 6. Verify transparency
file ../../../../assets/generated/asset_pack_transparent/*_transparent.png | head -3
```

## Why Use the Skill's Scripts?

The nano-banana-assets skill scripts provide:

1. **Proper chroma key workflow**: Uses #00FF00 background (not fake checkered patterns)
2. **Automatic rembg integration**: AI-powered background removal built-in
3. **Batch processing**: Generate all 10 assets efficiently
4. **Error handling**: Graceful fallback if rembg unavailable
5. **Consistent API calls**: Properly formatted requests to OpenRouter
6. **Reference image support**: Handles multiple reference images correctly

## Expected Results

All 10 assets with:
- ✅ Transparent RGBA PNG format
- ✅ Identical logo (butterfly in circle with sparkle) across all assets
- ✅ OpenTransition color scheme (warm orange #E68322, peachy creams)
- ✅ Orange/yellow butterflies (not rainbow)
- ✅ Professional quality ready for web use

Total size: ~10-15MB for all transparent assets
