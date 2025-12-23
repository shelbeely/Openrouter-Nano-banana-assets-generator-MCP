---
name: nano-banana-assets
description: Generate professional web assets, icons, banners, backgrounds, and UI elements using OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview). Use when the user needs to create or edit images, graphics, or visual assets for web development, social media, branding, or design projects.
license: MIT
metadata:
  author: shelbeely
  version: "1.0.0"
  category: design-and-media
  keywords: image-generation, assets, web-design, branding, openrouter, gemini
compatibility: Requires internet access and OpenRouter API key. Works with any agent that can make HTTP API calls.
allowed-tools: fetch http-client curl
---

# Nano Banana Assets Generator Skill

This skill enables AI agents to generate high-quality web assets using OpenRouter's Nano Banana Pro model (Google Gemini 3 Pro Image Preview). It provides professional asset generation, editing, and brand consistency management.

## About Nano Banana Pro

Nano Banana Pro is Google's most advanced image-generation and editing model, built on Gemini 3 Pro. It extends the original Nano Banana with significantly improved multimodal reasoning, real-world grounding, and high-fidelity visual synthesis.

**Key Features:**
- **Identity Preservation**: Maintains consistency across up to 5 subjects/reference images
- **Multi-Image Blending**: Consistent style across multiple generations
- **Text Rendering**: Industry-leading text placement in images with multilingual layouts
- **Fine-Grained Controls**: Localized edits, lighting adjustments, focus control, camera transformations
- **Flexible Outputs**: Support for 2K/4K outputs and multiple aspect ratios
- **Context-Rich Graphics**: From infographics and diagrams to cinematic composites

**Important**: For generating more than 5 images with consistent style, this skill uses a **sliding window technique** (detailed in section 5 below) to work around the 5-image reference limit while maintaining visual consistency across larger series.

## Core Capabilities

1. **Generate Single Assets**: Create icons, banners, backgrounds, UI elements, and more
2. **Generate Asset Packs**: Create cohesive sets of related assets with consistent branding
3. **Edit Existing Assets**: Apply fine-grained edits to existing images
4. **Ensure Brand Consistency**: Analyze and maintain visual identity across multiple assets
5. **Generate Consistent Series (6+ Images)**: Create large image series maintaining consistency using the sliding window technique

## Prerequisites

Before using this skill, ensure you have:

- OpenRouter API key (get one from https://openrouter.ai/)
- The API key should be stored as `OPENROUTER_API_KEY` environment variable
- Internet access to call the OpenRouter API

## API Configuration

### Base URL
```
https://openrouter.ai/api/v1/chat/completions
```

### Model
```
google/gemini-3-pro-image-preview
```

### Authentication
```
Authorization: Bearer <OPENROUTER_API_KEY>
```

## Core Operations

### 1. Generate a Single Asset

Use this when the user needs one specific asset (icon, banner, background, etc.).

**When to use:**
- User asks for "create an icon"
- User wants "generate a banner"
- User needs "make a background image"
- User requests any single graphic asset

**Steps:**
1. Collect requirements:
   - What type of asset (icon, banner, background, UI element, etc.)
   - Description/prompt (be detailed and specific)
   - Aspect ratio (1:1, 16:9, 9:16, 4:3, 21:9, etc.)
   - Resolution (1080x1080, 1920x1080, 2K, 4K)
   - Color palette (hex codes)
   - Any reference images or logos

2. Build the prompt:
   ```
   Generate a high-quality [asset type] with the following specifications:
   
   Description: [detailed description]
   Aspect Ratio: [ratio]
   Resolution: [resolution]
   Color Palette: [colors]
   
   Requirements:
   - Professional, web-ready quality
   - Modern and visually appealing design
   - Optimized for digital use
   - Clean and polished appearance
   ```

3. Make the API call (see API Call Format section below)

4. Extract generated images from response.choices[0].message.images array

5. Present the images to the user

**Example prompt:**
```
Generate a high-quality hero banner with the following specifications:

Description: Modern tech startup hero banner with gradient background from blue (#667EEA) to purple (#764BA2), abstract geometric elements, and space for overlaying text. Clean, professional, and eye-catching design.
Aspect Ratio: 16:9
Resolution: 1920x1080
Color Palette: #667EEA, #764BA2, #F093FB

Requirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance
```

### 2. Generate Asset Pack

Use this when the user needs multiple related assets maintaining brand consistency.

**When to use:**
- User asks for "social media kit"
- User wants "complete branding package"
- User needs "set of icons" or "icon set"
- User requests multiple related assets

**Steps:**
1. Collect requirements:
   - Overall purpose/description
   - List of asset types needed (e.g., "instagram-post", "facebook-cover", "icon-set")
   - Brand guidelines (style, tone, values)
   - Color palette
   - Logo file (if any)
   - Default aspect ratio and resolution

2. Build the prompt:
   ```
   Generate a complete, brand-consistent asset pack for web development:
   
   Project Description: [description]
   
   Asset Types to Generate:
   1. [asset type 1]
   2. [asset type 2]
   3. [asset type 3]
   ...
   
   Brand Guidelines:
   [guidelines]
   
   Brand Color Palette: [colors]
   Default Aspect Ratio: [ratio]
   Default Resolution: [resolution]
   
   Requirements:
   - All assets must maintain visual consistency
   - Follow the brand guidelines strictly
   - Use the provided color palette throughout
   - Professional, production-ready quality
   - Each asset should be optimized for its specific use case
   - Cohesive design language across all assets
   ```

3. Make the API call with reference images if provided

4. Extract all generated images from the response

5. Present each asset with its type/purpose labeled

**Example prompt:**
```
Generate a complete, brand-consistent asset pack for web development:

Project Description: Social media kit for an eco-friendly coffee brand targeting young professionals

Asset Types to Generate:
1. Instagram post (square, 1:1)
2. Instagram story (vertical, 9:16)
3. Facebook cover (wide banner)
4. Twitter header (wide banner)
5. App icon (square, simple)

Brand Guidelines:
Minimalist, nature-inspired, earthy aesthetics. Focus on sustainability, organic elements, and natural textures. Warm and inviting tone. Use coffee-related imagery with environmental themes.

Brand Color Palette: #2ECC71, #27AE60, #8B4513, #F5F5DC
Default Aspect Ratio: 1:1
Default Resolution: 1080x1080

Requirements:
- All assets must maintain visual consistency
- Follow the brand guidelines strictly
- Use the provided color palette throughout
- Professional, production-ready quality
- Each asset should be optimized for its specific use case
- Cohesive design language across all assets
```

### 3. Edit Existing Asset

Use this when the user wants to modify an existing image.

**When to use:**
- User says "edit this image"
- User wants "adjust the lighting"
- User needs "change the colors"
- User requests any modification to an existing asset

**Steps:**
1. Get the source image (URL or base64 data)

2. Collect edit requirements:
   - Specific edit instructions (be precise)
   - Elements to preserve (logo, text, specific objects)
   - Target aspect ratio (if changing)
   - Target resolution (if changing)

3. Build the prompt:
   ```
   Edit the provided image with the following instructions:
   
   Edit Instructions: [specific edits]
   
   Preserve These Elements: [elements to keep]
   Target Aspect Ratio: [ratio]
   Target Resolution: [resolution]
   
   Editing Requirements:
   - Apply edits precisely as instructed
   - Maintain image quality and professional appearance
   - Preserve specified elements without alteration
   - Ensure smooth transitions and natural-looking results
   - Output should be web-ready and optimized
   ```

4. Make the API call with the source image included in the content array

5. Extract edited image from the response

6. Present the edited image to the user

**Example prompt with image:**
```
Edit the provided image with the following instructions:

Edit Instructions: Adjust lighting to be warmer with golden hour tones, increase contrast by 20%, soften shadows, and add a subtle vignette effect around the edges. Make the overall mood more inviting and cozy.

Preserve These Elements: logo in top-left corner, main product in center, text overlay at bottom

Editing Requirements:
- Apply edits precisely as instructed
- Maintain image quality and professional appearance
- Preserve specified elements without alteration
- Ensure smooth transitions and natural-looking results
- Output should be web-ready and optimized
```

### 4. Ensure Brand Consistency

Use this when the user wants to check if multiple assets follow brand guidelines.

**When to use:**
- User says "check these assets for consistency"
- User wants "review brand compliance"
- User needs "validate branding"
- User asks if assets "match the guidelines"

**Steps:**
1. Collect all assets to analyze (URLs or base64 data)

2. Get brand guidelines:
   - Detailed style requirements
   - Color palette (official brand colors)
   - Reference images showing desired style
   - Logo file
   - Typography preferences
   - Tone and values

3. Build the prompt:
   ```
   Analyze the following assets for brand consistency and provide recommendations:
   
   Brand Guidelines:
   [detailed guidelines]
   
   Brand Colors: [hex codes]
   
   Analysis Requirements:
   - Check adherence to brand guidelines
   - Verify consistent use of colors, typography, and style
   - Identify inconsistencies across assets
   - Provide specific recommendations for improvements
   - Suggest refinements to maintain brand identity
   - Ensure logo usage is consistent and appropriate
   - Verify visual cohesion across all assets
   
   I have [N] assets to analyze. Please review them for consistency.
   ```

4. Make the API call with all assets and reference images

5. Extract analysis text and any corrected images

6. Present the analysis with specific recommendations

**Example prompt:**
```
Analyze the following assets for brand consistency and provide recommendations:

Brand Guidelines:
- Style: Modern, minimalist, professional
- Tone: Trustworthy, innovative, forward-thinking
- Colors must be limited to the brand palette
- Logo must always be visible and properly sized
- Typography: Clean, sans-serif, high readability
- Imagery: High-tech, futuristic, abstract geometric patterns preferred

Brand Colors: #667EEA, #764BA2, #FFFFFF, #2D3748

Analysis Requirements:
- Check adherence to brand guidelines
- Verify consistent use of colors, typography, and style
- Identify inconsistencies across assets
- Provide specific recommendations for improvements
- Suggest refinements to maintain brand identity
- Ensure logo usage is consistent and appropriate
- Verify visual cohesion across all assets

I have 4 assets to analyze. Please review them for consistency.
```

### 5. Generate Consistent Series (More than 5 Images)

Use this when the user needs to generate **more than 5 images** that must maintain consistency across the entire series.

**Background**: Nano Banana Pro supports accurate identity preservation across up to 5 subjects/reference images. For series larger than 5 images, use a **sliding window approach** where you use the last 5 generated images as references for each new image.

**When to use:**
- User asks for "10 icons in the same style"
- User wants "a storyboard with 8 frames"
- User needs "12 social media posts with consistent branding"
- User requests any image series with more than 5 items

**Steps:**

1. **Initial Setup**:
   - Collect series requirements:
     - Overall series description
     - Individual descriptions for each image
     - Brand guidelines and style requirements
     - Color palette
     - Aspect ratio and resolution
     - Any initial reference images or logo

2. **Generate First Image**:
   - Use any initial reference images provided
   - Include brand guidelines and color palette
   - This establishes the baseline style

3. **Generate Subsequent Images (Sliding Window)**:
   - For images 2-5: Use ALL previously generated images as references
   - For image 6 onwards: Use only the LAST 5 generated images as references
   - This maintains consistency while respecting the model's 5-image limit

4. **Workflow Pattern**:

   **For each image in the series:**
   
   a. Build the prompt:
   ```
   Generate image [N] of [TOTAL] for this series:
   
   Series Context: [overall description]
   
   This Image: [specific description for this image]
   
   Brand Guidelines:
   [guidelines]
   
   Color Palette: [colors]
   Aspect Ratio: [ratio]
   Resolution: [resolution]
   
   Consistency Requirements:
   - Maintain the same visual style as the reference images
   - Use consistent design language, color treatment, and composition
   - Ensure this image feels like part of the same cohesive series
   - Professional, web-ready quality
   - Modern and polished appearance
   
   IMPORTANT: The reference images show the previously generated images in this series. Match their style, tone, and visual identity exactly while creating this new variation.
   ```
   
   b. Prepare reference images:
   ```
   reference_images = []
   
   # Add logo if provided
   if logo_file:
       reference_images.append(logo_file)
   
   # Add initial references only for first image
   if current_image == 1 and initial_references:
       reference_images.extend(initial_references)
   
   # Add previously generated images (sliding window)
   if generated_images:
       # Take last 5 images
       start_index = max(0, len(generated_images) - 5)
       reference_images.extend(generated_images[start_index:])
   ```
   
   c. Make API call with reference images
   
   d. Store the generated image for use in next iteration
   
   e. Repeat for next image

5. **Present results with clear tracking**:
   - Show each image with its number and description
   - Indicate which images were used as references
   - Confirm consistency across the series

**Example workflow for 8-icon series:**

```
User Request: "Create 8 minimalist icons for a productivity app: home, calendar, tasks, notes, settings, profile, notifications, help"

Your Workflow:

Step 1: Generate Icon 1 (Home)
---
Prompt: "Generate icon 1 of 8 for this series:

Series Context: Minimalist icon set for productivity app. Clean lines, modern design, consistent stroke weight, monochrome style suitable for both light and dark interfaces.

This Image: Home icon - house symbol representing the main dashboard

Brand Guidelines: Minimalist, professional, 2px stroke weight, rounded line caps, #2D3748 color on transparent background

Aspect Ratio: 1:1
Resolution: 512x512

Consistency Requirements:
- Professional, web-ready quality
- Modern and polished appearance
- Clean, simple design with consistent visual language"

References: [initial reference images if any, logo if any]
[Make API call]
[Store generated icon 1]

Step 2: Generate Icon 2 (Calendar)
---
Prompt: "Generate icon 2 of 8 for this series:

Series Context: Minimalist icon set for productivity app. Clean lines, modern design, consistent stroke weight, monochrome style.

This Image: Calendar icon - calendar grid representing scheduling

Brand Guidelines: Minimalist, professional, 2px stroke weight, rounded line caps, #2D3748 color on transparent background

Consistency Requirements:
- Maintain the same visual style as the reference images
- Use consistent design language, color treatment, and composition
- Ensure this icon feels like part of the same cohesive series

IMPORTANT: The reference images show the previously generated icons in this series. Match their style, tone, and visual identity exactly while creating this new variation."

References: [logo if any, icon 1]
[Make API call]
[Store generated icon 2]

Step 3-5: Generate Icons 3, 4, 5
---
Same process, using all previously generated icons as references
References for icon 3: [logo, icon 1, icon 2]
References for icon 4: [logo, icon 1, icon 2, icon 3]
References for icon 5: [logo, icon 1, icon 2, icon 3, icon 4]

Step 6: Generate Icon 6 (Profile) - SLIDING WINDOW STARTS
---
Prompt: [same structure as above]

References: [logo, icon 2, icon 3, icon 4, icon 5] ← Only last 5 (or 4 + logo)
[Make API call]
[Store generated icon 6]

Step 7: Generate Icon 7 (Notifications)
---
References: [logo, icon 3, icon 4, icon 5, icon 6] ← Sliding window
[Make API call]
[Store generated icon 7]

Step 8: Generate Icon 8 (Help)
---
References: [logo, icon 4, icon 5, icon 6, icon 7] ← Sliding window
[Make API call]
[Store generated icon 8]

Final Response:
"✅ Generated 8 consistent icons for your productivity app!

Icons created with sliding window consistency:
1. Home - baseline style established
2. Calendar - matched icon 1
3. Tasks - matched icons 1-2
4. Notes - matched icons 1-3
5. Settings - matched icons 1-4
6. Profile - matched icons 2-5 (sliding window)
7. Notifications - matched icons 3-6 (sliding window)
8. Help - matched icons 4-7 (sliding window)

All icons maintain consistent style, stroke weight, and visual language throughout the series."

[Present all 8 icons]
```

**Key Points:**

- **Sliding window**: Use last 5 images as references when you have more than 5
- **Explicit instructions**: Tell the model the reference images are from the same series
- **Consistency emphasis**: Emphasize matching style, tone, and identity
- **Series context**: Always include the overall series description
- **Track progress**: Keep track of which images are used as references
- **Quality control**: After generation, visually verify consistency

**Common Use Cases:**
- Large icon sets (10+, 20+, 50+ icons)
- Storyboards with many frames (8-16 frames)
- Social media calendar (30 days of posts)
- Product catalog (multiple product variations)
- UI component libraries (many components)
- Brand asset collections (extensive asset sets)

## API Call Format

### Basic Request Structure

```json
{
  "model": "google/gemini-3-pro-image-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "YOUR PROMPT HERE"
        }
      ]
    }
  ],
  "modalities": ["image", "text"],
  "temperature": 0.7,
  "max_tokens": 4096
}
```

### With Image Input (for editing or reference)

```json
{
  "model": "google/gemini-3-pro-image-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/image.png"
          }
        },
        {
          "type": "text",
          "text": "YOUR PROMPT HERE"
        }
      ]
    }
  ],
  "modalities": ["image", "text"],
  "temperature": 0.7,
  "max_tokens": 4096
}
```

### With Aspect Ratio Control

```json
{
  "model": "google/gemini-3-pro-image-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "YOUR PROMPT HERE"
        }
      ]
    }
  ],
  "modalities": ["image", "text"],
  "image_config": {
    "aspect_ratio": "16:9"
  },
  "temperature": 0.7,
  "max_tokens": 4096
}
```

### Required Headers

```
Authorization: Bearer YOUR_OPENROUTER_API_KEY
Content-Type: application/json
HTTP-Referer: https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP
X-Title: Nano Banana Assets Generator
```

### Response Format

```json
{
  "choices": [
    {
      "message": {
        "content": "Description of generated assets...",
        "images": [
          {
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANS..."
            }
          }
        ]
      }
    }
  ]
}
```

## Supported Aspect Ratios

- `1:1` - Square (Instagram posts, icons, profile pictures)
- `16:9` - Widescreen (YouTube thumbnails, web banners, hero sections)
- `9:16` - Vertical (Instagram/Facebook stories, mobile screens)
- `4:3` - Traditional (presentations, older displays)
- `3:4` - Vertical traditional
- `21:9` - Ultra-wide (cinematic, wide banners)
- `9:21` - Ultra-tall
- `2:3` - Portrait
- `3:2` - Landscape

## Supported Resolutions

- `1080x1080` - Standard square (1:1)
- `1920x1080` - Full HD (16:9)
- `1080x1920` - Full HD vertical (9:16)
- `2K` (2560x1440) - High quality
- `4K` (3840x2160) - Ultra high quality
- `3840x2160` - 4K explicit
- `2560x1440` - 2K explicit
- `1280x720` - HD ready

## Best Practices

### Writing Effective Prompts

1. **Be Specific and Detailed**
   - ❌ "Make a banner"
   - ✅ "Create a modern tech startup hero banner with gradient background from blue to purple, abstract geometric elements, and space for overlaying text"

2. **Include Context**
   - Mention where the asset will be used (website, social media, email, app)
   - Specify the target audience
   - Describe the desired mood/emotion

3. **Define Style Clearly**
   - Use descriptive terms: minimalist, vibrant, elegant, playful, professional
   - Reference art styles: flat design, material design, glassmorphism, etc.
   - Mention specific elements: gradients, shadows, textures, patterns

4. **Specify Technical Requirements**
   - Always include aspect ratio for the intended use case
   - Mention resolution if quality is critical
   - List any technical constraints

### Color Guidance

1. **Provide Hex Codes**
   - ✅ Use: "#667EEA", "#764BA2"
   - ❌ Avoid: "blue", "purple"

2. **Include 3-5 Brand Colors**
   - Primary color
   - Secondary color
   - Accent color(s)
   - Background color (if applicable)

3. **Consider Color Harmony**
   - Complementary colors for contrast
   - Analogous colors for harmony
   - Triadic colors for vibrancy

### Reference Images

1. **Use Up to 5 Reference Images**
   - Style references (overall look)
   - Composition references (layout)
   - Color treatment references (mood)
   - Technical references (quality level)

2. **Provide Context for References**
   - Explain what aspect to emulate
   - Clarify what to avoid from the reference
   - Specify if it's for style, composition, or color only

### Brand Consistency

1. **Establish Guidelines First**
   - Define style clearly
   - Document color usage rules
   - Specify typography preferences
   - Outline logo usage rules

2. **Use Identity Preservation**
   - Include brand reference images
   - Provide logo in all requests
   - Maintain color palette strictly

3. **Iterate and Refine**
   - Generate initial assets
   - Check consistency
   - Refine as needed
   - Validate final outputs

## Common Use Cases

### Website Assets
- Hero banners (16:9, 21:9)
- Section backgrounds (16:9, various)
- Icon sets (1:1, small resolution)
- Call-to-action buttons (custom sizes)
- Feature images (4:3, 16:9)

### Social Media
- Instagram posts (1:1, 1080x1080)
- Instagram stories (9:16, 1080x1920)
- Facebook covers (wide, custom)
- Twitter headers (3:1, custom)
- LinkedIn banners (4:1, custom)
- YouTube thumbnails (16:9, 1280x720)

### Branding
- Logo variations (1:1, vector-style)
- Brand patterns (tileable, various)
- Color palette visualizations
- Style guide assets
- Presentation templates

### UI/UX Design
- App icons (1:1, multiple sizes)
- Splash screens (9:16, device-specific)
- Empty states (custom)
- Error states (custom)
- Loading animations (conceptual)

## Error Handling

### Common Issues

1. **Missing API Key**
   - Check that OPENROUTER_API_KEY is set
   - Verify the key is valid
   - Ensure the key has sufficient credits

2. **API Errors**
   - 401: Invalid API key
   - 402: Insufficient credits
   - 429: Rate limit exceeded
   - 500: Server error (retry)

3. **Invalid Parameters**
   - Check aspect ratio format (use colons, not "x")
   - Verify resolution is supported
   - Ensure image URLs are accessible
   - Validate hex color codes start with #

4. **Quality Issues**
   - Provide more detailed prompts
   - Add reference images
   - Specify style more clearly
   - Include brand guidelines
   - Try multiple iterations

### Troubleshooting Steps

1. Verify API key is set correctly
2. Check internet connectivity
3. Validate request format
4. Review prompt quality
5. Check for model availability
6. Retry with exponential backoff for transient errors

## Examples

### Example 1: Simple Icon

**User Request:** "Create a home icon for my website"

**Your Response:**
```
I'll generate a home icon for your website. Let me create a clean, professional icon.

API Request:
- Prompt: "Generate a minimalist home icon for a website. Simple, clean lines, modern design. Suitable for use as a navigation icon. White icon on transparent background."
- Aspect Ratio: 1:1
- Resolution: 512x512
- Style: Minimalist, professional

[Make API call with these parameters]

Generated icon:
[Present the generated image]
```

### Example 2: Social Media Kit

**User Request:** "I need a social media kit for my coffee shop"

**Your Response:**
```
I'll create a comprehensive social media kit for your coffee shop. What's your coffee shop's style and brand colors?

[After getting details:]

I'll generate 4 assets for your coffee shop:
1. Instagram post (square)
2. Instagram story (vertical)
3. Facebook cover
4. Profile picture

API Request:
- Description: Social media kit for artisan coffee shop
- Assets: instagram-post, instagram-story, facebook-cover, profile-picture
- Brand: Cozy, artisan, warm atmosphere
- Colors: #6F4E37, #DEB887, #FFFDD0
- Style: Warm, inviting, crafted aesthetic

[Make API call]

Generated assets:
[Present all generated images labeled by type]
```

### Example 3: Edit Existing Asset

**User Request:** "Make this image warmer and brighter" [provides image]

**Your Response:**
```
I'll adjust the image to be warmer and brighter.

API Request:
- Operation: Edit existing image
- Instructions: Adjust color temperature to be warmer (add golden/yellow tones), increase overall brightness by 20%, maintain contrast
- Preserve: Original composition, main subjects, any text

[Make API call with the provided image]

Edited image:
[Present the edited result]

Changes applied:
- Added warm golden tones
- Increased brightness by 20%
- Maintained original composition
```

### Example 4: Consistent Series (10 Icons)

**User Request:** "Create 10 weather icons in a consistent style: sunny, cloudy, rainy, stormy, snowy, windy, foggy, partly cloudy, thunderstorm, and hail"

**Your Response:**
```
I'll create a consistent set of 10 weather icons. Since this is more than 5 images, I'll use the sliding window technique to maintain consistency throughout.

First, let me establish the base style...

[Icon 1 - Sunny]
API Request:
- Prompt: "Generate icon 1 of 10 for weather icon series:
  
  Series Context: Weather icon set with consistent minimalist style, 2px stroke weight, rounded line caps, monochrome design, clean and modern.
  
  This Image: Sunny weather icon - sun with rays
  
  Aspect Ratio: 1:1
  Resolution: 512x512
  Color: #2D3748 on transparent background
  
  Professional, web-ready quality with clean, simple design"
  
- References: None (establishing baseline)

[Generate and store Icon 1]

[Icon 2 - Cloudy]
API Request:
- Prompt: "Generate icon 2 of 10 for weather icon series:
  
  Series Context: Weather icon set with consistent minimalist style, matching the previous icon's stroke weight and design language.
  
  This Image: Cloudy weather icon - cloud shape
  
  Consistency Requirements:
  - Match the visual style of the reference image exactly
  - Same stroke weight, line caps, and design approach
  - Ensure this feels like part of the same icon family
  
  IMPORTANT: The reference image shows the previously generated icon. Match its style exactly."
  
- References: [Icon 1]

[Generate and store Icon 2]

[Icons 3-5]
Continue same pattern, adding all previous icons as references
- Icon 3 references: [Icon 1, Icon 2]
- Icon 4 references: [Icon 1, Icon 2, Icon 3]
- Icon 5 references: [Icon 1, Icon 2, Icon 3, Icon 4]

[Icon 6 - Windy] ← Sliding window begins
API Request:
- Same prompt structure
- References: [Icon 2, Icon 3, Icon 4, Icon 5] ← Only last 4 icons (staying under 5 limit)

[Icons 7-10]
Continue with sliding window:
- Icon 7 references: [Icon 3, Icon 4, Icon 5, Icon 6]
- Icon 8 references: [Icon 4, Icon 5, Icon 6, Icon 7]
- Icon 9 references: [Icon 5, Icon 6, Icon 7, Icon 8]
- Icon 10 references: [Icon 6, Icon 7, Icon 8, Icon 9]

✅ Complete! Generated 10 weather icons with consistent style throughout.

Consistency strategy:
- Icons 1-5: Each new icon referenced all previous ones
- Icons 6-10: Sliding window of last 4 icons maintained consistency

All icons share the same stroke weight, style, and visual language!

[Present all 10 icons]
```

## Integration Tips

### With Code Editors
- Agents can directly generate assets during development
- Assets can be saved to project directories
- Quick iteration on UI components

### With Design Tools
- Export generated assets for further refinement
- Use as starting points for complex designs
- Maintain consistency across design systems

### With Workflow Automation
- Batch generate assets for multiple projects
- Automate social media content creation
- Generate variations for A/B testing

## Security Considerations

1. **API Key Management**
   - Never hardcode API keys
   - Use environment variables
   - Rotate keys regularly
   - Monitor usage

2. **Input Validation**
   - Validate user inputs
   - Sanitize prompts
   - Check image URLs for security
   - Limit request sizes

3. **Rate Limiting**
   - Implement request throttling
   - Handle rate limit errors gracefully
   - Cache results when appropriate
   - Monitor API usage

## Performance Tips

1. **Optimize Requests**
   - Batch related assets when possible
   - Use appropriate resolutions (don't request 4K unless needed)
   - Cache frequently used assets
   - Reuse similar prompts

2. **Manage Costs**
   - Monitor API usage
   - Use appropriate model parameters
   - Avoid unnecessary regenerations
   - Implement result caching

3. **Quality vs Speed**
   - Lower resolution for drafts/previews
   - Higher resolution for final outputs
   - Use reference images to improve first-try success
   - Iterate on prompts to reduce regenerations

## Version History

- **1.0.0** (2024): Initial release
  - Basic asset generation
  - Asset pack creation
  - Image editing capabilities
  - Brand consistency checking

## Support and Resources

- **OpenRouter Documentation**: https://openrouter.ai/docs
- **Model Information**: https://openrouter.ai/models
- **GitHub Repository**: https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP
- **MCP Server**: Available as a full MCP server implementation in this repository

## Related Skills

- Image optimization and compression
- Color palette generation
- Typography pairing
- Layout generation
- Brand identity creation

---

**Remember**: This skill uses OpenRouter's API which requires credits. Monitor your usage and implement appropriate rate limiting and error handling in production environments.
