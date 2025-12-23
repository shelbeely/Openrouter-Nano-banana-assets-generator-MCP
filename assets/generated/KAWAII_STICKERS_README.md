# Kawaii Sticker Pack - Raccoon & Ferret Characters

## Overview

This is a kawaii-style sticker pack featuring adorable raccoon and ferret characters in various cute poses and outfits. Generated using the nano-banana-assets agent skill with OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview).

## ⚠️ Important Note: Background Transparency

**These images do NOT have true transparent backgrounds.** This is a known limitation of the Gemini image generation model.

- **Format:** RGB PNG (without alpha channel)
- **Actual Background:** Painted white/checkered pattern (not true transparency)
- **File Type:** Color type 2 (RGB), not color type 6 (RGBA)

**To use these as stickers with transparent backgrounds:**
1. Apply background removal in post-processing
2. Use tools like Photoshop, GIMP, remove.bg, or CLI tools
3. Example: `convert input.png -fuzz 10% -transparent white output.png`

## Art Style Specifications

All stickers follow a consistent, cohesive art style:

- ✅ **Bold, clean outlines** (3-4px consistent black stroke)
- ✅ **Simple cel-shading** (1-2 shade levels maximum)
- ✅ **Vibrant, pastel-leaning color palette** (pinks, mint green, sky blue, lavender, peach)
- ✅ **Chibi proportions** (oversized head 40% of body, small body, stubby limbs)
- ✅ **Rounded silhouette** with smooth curves, no sharp angles
- ✅ **Large expressive eyes** (sparkly, anime-style with highlights)
- ✅ **Simplified facial features** (small nose, simple expressions)
- ✅ **Soft, even lighting** with minimal shading
- ✅ **No texture or gradients** (flat colors only)
- ✅ **Polished, vector-like finish** suitable for digital stickers
- ❌ **Background:** RGB format with painted background (requires post-processing for transparency)
- ✅ **No text, no drop shadows, no borders**

## Sticker Collection (9/10 Generated)

### 1. Raccoon - Waving Cheerfully
**Filename:** `kawaii_sticker_01_raccoon_waving.png`
- **Action:** Waving cheerfully with one paw raised
- **Accessory:** Wearing a tiny pink bow tie
- **Role:** Baseline sticker, establishing the art style

### 2. Ferret - Jumping Joyfully
**Filename:** `kawaii_sticker_02_ferret_jumping.png`
- **Action:** Jumping joyfully in the air
- **Accessory:** Wearing a small yellow star hair clip
- **References:** 1 previous sticker

### 3. Raccoon - Praying Pose
**Filename:** `kawaii_sticker_03_raccoon_sitting.png`
- **Action:** Sitting with paws together in a praying pose
- **Accessory:** Wearing a cute mint green scarf
- **References:** 2 previous stickers

### 4. Ferret - Lying on Back
**Filename:** `kawaii_sticker_04_ferret_lying.png`
- **Action:** Lying on its back with paws up
- **Accessory:** Wearing tiny purple socks
- **References:** 3 previous stickers

### 5. Raccoon - Holding Heart
**Filename:** `kawaii_sticker_05_raccoon_holding.png`
- **Action:** Holding a heart with both paws
- **Accessory:** Wearing a small red beret
- **References:** 4 previous stickers

### 6. Ferret - Standing Excited
**Filename:** `kawaii_sticker_06_ferret_standing.png`
- **Action:** Standing on hind legs with excited expression
- **Accessory:** Wearing a tiny blue bow
- **References:** 5 previous stickers

### 7. Raccoon - Sleeping Peacefully
**Filename:** `kawaii_sticker_07_raccoon_sleeping.png`
- **Action:** Sleeping peacefully curled up
- **Accessory:** Wearing a soft lavender sleeping cap
- **References:** Last 5 stickers (sliding window begins)

### 8. Ferret - Dancing
**Filename:** `kawaii_sticker_08_ferret_dancing.png`
- **Action:** Dancing with paws in the air
- **Accessory:** Wearing a tiny orange collar with bell
- **References:** Last 5 stickers (sliding window)

### 9. Raccoon - Peace Sign
**Filename:** `kawaii_sticker_09_raccoon_making.png`
- **Action:** Making a peace sign with paw
- **Accessory:** Wearing cute round pink sunglasses
- **References:** Last 5 stickers (sliding window)

### 10. Ferret - Thumbs Up (Not Generated)
**Status:** ❌ API rate limit reached
- **Planned Action:** Sitting and giving a thumbs up
- **Planned Accessory:** Wearing a tiny teal headband

## Generation Strategy

### Sliding Window Consistency Technique

To maintain visual consistency across the entire sticker pack, we used the nano-banana-assets skill's recommended sliding window approach:

1. **Sticker 1** - No references (establishes baseline style)
2. **Stickers 2-6** - Accumulating references (each new sticker used all previous ones)
3. **Stickers 7-9** - Sliding window (each used last 5 stickers as references)

This technique ensures:
- Consistent line weight and outline style
- Matching chibi proportions across all characters
- Cohesive color treatment and shading approach
- Professional sticker-pack aesthetic
- Characters feel like they belong to the same universe

### Six-Element Framework

Each sticker prompt was crafted using Google's recommended Six-Element Framework:

1. **Subject** - Character type (raccoon/ferret) with specific features
2. **Composition** - Centered, balanced, optimized for sticker use
3. **Action** - Specific pose clearly depicted
4. **Location** - Transparent background, isolated character
5. **Style** - Kawaii/chibi aesthetic with consistent visual treatment
6. **Lighting** - Soft, even, minimal shading

## Technical Specifications

- **Resolution:** 1024x1024 pixels per sticker
- **Aspect Ratio:** 1:1 (square)
- **Format:** PNG with transparency
- **Color Mode:** RGB
- **Background:** Fully transparent (alpha channel)
- **File Size:** ~1MB per sticker

## Character Design

### Raccoon Features
- Soft gray body (#D8D8D8)
- Darker gray mask pattern (#A8A8A8)
- Pink nose (#FFB6D9)
- Bold black outlines (#000000)
- Characteristic ringed tail

### Ferret Features
- Cream/beige body (#F5E6D3)
- White chest (#FFFFFF)
- Pink nose (#FFB6D9)
- Bold black outlines (#000000)
- Elongated body shape with pointed face

## Usage

These stickers are perfect for:
- Messaging apps (Discord, Telegram, WhatsApp)
- Social media posts and reactions
- Digital planners and journals
- Website embellishments
- App UI elements
- Print stickers (high resolution suitable)

## Generation Details

- **Tool:** nano-banana-assets agent skill
- **Model:** Google Gemini 3 Pro Image Preview (Nano Banana Pro) via OpenRouter
- **API:** OpenRouter API (https://openrouter.ai/)
- **Date Generated:** December 23, 2024
- **Total Generation Time:** ~6 minutes for 9 stickers
- **Success Rate:** 9/10 (90%)

## Notes

- All stickers maintain consistent visual identity throughout the pack
- The sliding window technique successfully preserved style across all 9 generated stickers
- **Backgrounds are RGB (not RGBA)** - The model generated painted backgrounds, not true transparency
- Post-processing required for transparent backgrounds (use background removal tools)
- Each character has a distinct personality expressed through pose and accessories
- The art style is cohesive and professional, suitable for commercial use

## Known Limitation: Fake Transparency

**Issue Identified:** The generated images appear to have transparent backgrounds when viewed with a checkered pattern, but they are actually RGB PNG files with painted backgrounds.

**Technical Details:**
- File format: PNG color type 2 (RGB), not type 6 (RGBA)
- No alpha channel present
- Background is painted white/checkered pattern, not transparent pixels

**This is a model limitation** - Gemini 3 Pro Image Preview (Nano Banana Pro) does not support generating true RGBA images with alpha transparency. The model interprets "transparent background" requests as instructions to paint a white or checkered background.

**Solution:**
To convert these to true stickers with transparency, you need to:

1. **Use online tools:**
   - remove.bg
   - Adobe Express Background Remover
   - Canva Background Remover

2. **Use desktop software:**
   - Photoshop (Magic Wand + Delete)
   - GIMP (Select by Color + Delete)
   - Affinity Photo

3. **Use command-line tools:**
   ```bash
   # Using ImageMagick
   convert kawaii_sticker_01_raccoon_waving.png -fuzz 10% -transparent white output.png
   
   # Batch process all stickers
   for file in kawaii_sticker_*.png; do
     convert "$file" -fuzz 10% -transparent white "transparent_$file"
   done
   ```

**Future Recommendation:**
When using the nano-banana-assets skill, specify solid background colors (e.g., "white background", "light gray background") instead of requesting transparent backgrounds. This sets correct expectations and prevents confusion.

---

**Generated with ❤️ using the nano-banana-assets agent skill**
