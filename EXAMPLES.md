# Usage Examples

## Example 1: Generate a Hero Banner

```javascript
{
  "tool": "generate_asset",
  "arguments": {
    "prompt": "Create a modern hero banner for a SaaS platform. Include abstract tech elements, gradient background from blue to purple, with space for overlaying text. Professional and clean design.",
    "aspectRatio": "16:9",
    "resolution": "1920x1080",
    "colorPalette": ["#667EEA", "#764BA2", "#F093FB"]
  }
}
```

## Example 2: Generate Icons with Logo Reference

```javascript
{
  "tool": "generate_asset",
  "arguments": {
    "prompt": "Create a set of minimalist icons for a dashboard: home, settings, notifications, profile. Consistent style, rounded corners, 2px stroke weight.",
    "aspectRatio": "1:1",
    "resolution": "1080x1080",
    "logoFile": "data:image/png;base64,iVBORw0KGgoAAAANS...",
    "colorPalette": ["#667EEA", "#48494B"]
  }
}
```

## Example 3: Generate Social Media Asset Pack

```javascript
{
  "tool": "generate_asset_pack",
  "arguments": {
    "description": "Social media asset pack for an eco-friendly coffee brand launch",
    "assetTypes": [
      "instagram-post-square",
      "instagram-story",
      "facebook-cover",
      "twitter-header",
      "linkedin-banner"
    ],
    "brandGuidelines": "Natural, organic aesthetic. Use earth tones. Include coffee bean imagery. Minimalist and modern. Target audience: environmentally conscious millennials.",
    "colorPalette": ["#2ECC71", "#27AE60", "#8B4513", "#F1C40F", "#FFFFFF"],
    "logoFile": "https://example.com/logo.png",
    "resolution": "2K"
  }
}
```

## Example 4: Edit Existing Asset

```javascript
{
  "tool": "edit_asset",
  "arguments": {
    "sourceImage": "https://example.com/banner.png",
    "editInstructions": "Adjust the lighting to be warmer and more inviting. Increase contrast slightly. Soften the shadows. Make the background slightly blurred to emphasize the foreground subject.",
    "preserveElements": ["logo", "text", "call-to-action-button"],
    "resolution": "1920x1080"
  }
}
```

## Example 5: Create High-Resolution Product Visualization

```javascript
{
  "tool": "generate_asset",
  "arguments": {
    "prompt": "Product shot of a minimalist smartwatch on a clean white surface with soft studio lighting. Watch face shows 10:10. Subtle reflections on the surface. Professional e-commerce quality.",
    "aspectRatio": "4:3",
    "resolution": "4K",
    "referenceImages": [
      "https://example.com/watch-reference1.jpg",
      "https://example.com/lighting-reference.jpg"
    ],
    "colorPalette": ["#000000", "#FFFFFF", "#C0C0C0"]
  }
}
```

## Example 6: Generate UI Kit Components

```javascript
{
  "tool": "generate_asset_pack",
  "arguments": {
    "description": "Complete UI component kit for a modern web application",
    "assetTypes": [
      "button-set-primary-secondary-tertiary",
      "input-field-variations",
      "card-components",
      "navigation-elements",
      "icon-set-24px",
      "loading-states",
      "modal-templates"
    ],
    "brandGuidelines": "Modern, accessible design following WCAG 2.1 AA standards. Rounded corners (8px radius). Clear hierarchy. Support for light and dark modes.",
    "colorPalette": ["#667EEA", "#764BA2", "#48494B", "#E8E8E8", "#FFFFFF"],
    "aspectRatio": "16:9",
    "resolution": "1920x1080"
  }
}
```

## Example 7: Ensure Brand Consistency

```javascript
{
  "tool": "ensure_brand_consistency",
  "arguments": {
    "assets": [
      "https://example.com/asset1.png",
      "https://example.com/asset2.png",
      "https://example.com/asset3.png"
    ],
    "brandGuidelines": "Brand identity: Professional tech company. Primary color: #667EEA (blue). Secondary: #764BA2 (purple). Typography: Sans-serif, clean. Style: Modern, minimalist, trustworthy. Logo must always appear in top-left or center. Maintain 2:1 contrast ratio minimum.",
    "referenceImages": ["https://example.com/brand-guide.png"],
    "colorPalette": ["#667EEA", "#764BA2", "#FFFFFF", "#F8F9FA"],
    "logoFile": "https://example.com/official-logo.png"
  }
}
```

## Example 8: Edit with Aspect Ratio Change

```javascript
{
  "tool": "edit_asset",
  "arguments": {
    "sourceImage": "https://example.com/original-16-9.png",
    "editInstructions": "Crop to vertical format for mobile stories. Ensure the main subject remains centered and prominent. Adjust composition for vertical viewing.",
    "aspectRatio": "9:16",
    "preserveElements": ["logo", "main-product"],
    "resolution": "1080x1920"
  }
}
```

## Example 9: Generate Background Patterns

```javascript
{
  "tool": "generate_asset",
  "arguments": {
    "prompt": "Seamless repeating pattern with subtle geometric shapes. Modern, abstract, and professional. Suitable as a website background. Low contrast to not distract from content.",
    "aspectRatio": "1:1",
    "resolution": "2K",
    "colorPalette": ["#F8F9FA", "#E9ECEF", "#DEE2E6"]
  }
}
```

## Example 10: Multi-Reference Asset Generation

```javascript
{
  "tool": "generate_asset",
  "arguments": {
    "prompt": "Create a promotional banner combining elements from all reference images. Blend the style of the first image with the color treatment from the second, and incorporate the layout structure from the third. Add our logo and maintain brand consistency.",
    "aspectRatio": "21:9",
    "resolution": "3440x1440",
    "referenceImages": [
      "https://example.com/style-ref.jpg",
      "https://example.com/color-ref.jpg",
      "https://example.com/layout-ref.jpg"
    ],
    "logoFile": "https://example.com/logo.png",
    "colorPalette": ["#667EEA", "#764BA2", "#F093FB"]
  }
}
```

## Tips for Best Results

### Writing Effective Prompts

1. **Be Specific**: Include details about style, mood, elements, and composition
2. **Reference Context**: Mention the intended use (web banner, icon, social media, etc.)
3. **Describe Quality**: Use terms like "professional", "high-resolution", "production-ready"
4. **Specify Elements**: List what should be included or excluded
5. **Define Style**: Modern, minimalist, vibrant, corporate, playful, etc.

### Using Reference Images

- Provide up to 5 reference images for best results
- Use references to establish style, composition, or color treatment
- Mix reference types: some for style, some for composition, some for specific elements
- Ensure reference images are high quality and relevant

### Color Palettes

- Provide 3-5 key brand colors as hex codes
- Include primary, secondary, and accent colors
- Consider background/foreground relationships
- Specify usage context if needed (e.g., "primary for buttons")

### Brand Consistency

- Always include brand guidelines when generating multiple assets
- Use the same logo file across all generations
- Maintain consistent color palette
- Reference previous successful assets
- Use `ensure_brand_consistency` to validate before finalizing

### Resolution Selection

- **1080x1080**: Social media posts, profile images
- **1920x1080**: Web banners, video thumbnails, presentations
- **2K (2560x1440)**: High-quality web assets, retina displays
- **4K (3840x2160)**: Print materials, large displays, future-proofing
- **Custom**: Match specific platform requirements

### Aspect Ratios

- **1:1**: Instagram posts, profile pictures, icons
- **16:9**: YouTube thumbnails, web banners, presentations
- **9:16**: Instagram/TikTok stories, mobile-first designs
- **4:3**: Traditional displays, some social platforms
- **21:9**: Ultrawide banners, cinematic compositions

## Workflow Examples

### Complete Brand Launch

1. Generate logo variations with `generate_asset`
2. Create asset pack with `generate_asset_pack` for all platforms
3. Edit specific assets with `edit_asset` for fine-tuning
4. Validate consistency with `ensure_brand_consistency`
5. Iterate on any inconsistencies

### Website Redesign

1. Generate hero banner with brand colors
2. Create UI component set as asset pack
3. Generate icon set with consistent style
4. Generate background patterns and textures
5. Create call-to-action graphics
6. Ensure all assets work together cohesively

### Social Media Campaign

1. Define brand guidelines and color palette
2. Generate asset pack for all social platforms
3. Create variations for A/B testing
4. Edit best-performing assets for optimization
5. Maintain consistency across campaign duration
