# API Reference

## OpenRouter Integration

This MCP server integrates with OpenRouter's API to access Google's Nano Banana Pro (Gemini 3 Pro Image Preview) model.

### Authentication

Set your OpenRouter API key as an environment variable:

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

### Model Details

- **Model ID**: `google/gemini-3-pro-image-preview`
- **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Capabilities**: Image generation, image editing, multimodal understanding

## Request Format

### Image Generation Request

```typescript
{
  model: "google/gemini-3-pro-image-preview",
  messages: [
    {
      role: "user",
      content: [
        // Optional: Reference images for style/context
        {
          type: "image_url",
          image_url: { url: "https://example.com/ref.jpg" }
        },
        // Required: Text prompt
        {
          type: "text",
          text: "Generate a modern hero banner..."
        }
      ]
    }
  ],
  modalities: ["image", "text"],  // Enables image generation
  image_config: {
    aspect_ratio: "16:9"  // Optional: Default is 1:1
  },
  temperature: 0.7,
  max_tokens: 4096
}
```

### Response Format

```typescript
{
  id: "gen-...",
  choices: [
    {
      message: {
        role: "assistant",
        content: "I've created a modern hero banner...",
        images: [
          {
            image_url: {
              url: "data:image/png;base64,iVBORw0KG..."
            }
          }
        ]
      }
    }
  ],
  usage: { ... }
}
```

## MCP Tools

### 1. generate_asset

Generate a single web asset with full customization.

#### Input Schema

```typescript
{
  prompt: string;              // Required: Asset description
  aspectRatio?: string;        // "1:1" | "16:9" | "9:16" | "4:3" | etc.
  resolution?: string;         // "1080x1080" | "1920x1080" | "2K" | "4K" | etc.
  referenceImages?: string[];  // URLs or base64 data (max 5)
  colorPalette?: string[];     // Hex codes: ["#667EEA", "#764BA2"]
  logoFile?: string;           // URL or base64 data
  editInstructions?: string;   // Optional editing guidance
}
```

#### Output Format

```typescript
{
  content: [
    {
      type: "text",
      text: "Asset Generation Complete!..."
    },
    {
      type: "image",
      data: "data:image/png;base64,...",
      mimeType: "image/png"
    }
  ]
}
```

#### Example Usage

```javascript
// Via MCP
{
  tool: "generate_asset",
  arguments: {
    prompt: "Modern tech startup hero banner",
    aspectRatio: "16:9",
    colorPalette: ["#667EEA", "#764BA2"]
  }
}
```

### 2. generate_asset_pack

Generate multiple related assets maintaining brand consistency.

#### Input Schema

```typescript
{
  description: string;         // Required: Pack purpose
  assetTypes: string[];        // Required: Types to generate
  brandGuidelines?: string;    // Brand style requirements
  referenceImages?: string[];  // Style references
  colorPalette?: string[];     // Brand colors
  logoFile?: string;           // Brand logo
  aspectRatio?: string;        // Default aspect ratio
  resolution?: string;         // Default resolution
}
```

#### Output Format

```typescript
{
  content: [
    {
      type: "text",
      text: "Asset Pack Generation Complete!..."
    },
    {
      type: "image",
      data: "data:image/png;base64,...",
      mimeType: "image/png"
    },
    // ... more images
  ]
}
```

#### Example Usage

```javascript
{
  tool: "generate_asset_pack",
  arguments: {
    description: "Social media kit for eco brand",
    assetTypes: ["instagram-post", "facebook-cover", "twitter-header"],
    colorPalette: ["#2ECC71", "#27AE60"]
  }
}
```

### 3. edit_asset

Edit existing assets with fine-grained controls.

#### Input Schema

```typescript
{
  sourceImage: string;         // Required: Image to edit
  editInstructions: string;    // Required: Edit instructions
  preserveElements?: string[]; // Elements to keep unchanged
  aspectRatio?: string;        // Target aspect ratio
  resolution?: string;         // Target resolution
}
```

#### Output Format

```typescript
{
  content: [
    {
      type: "text",
      text: "Asset Editing Complete!..."
    },
    {
      type: "image",
      data: "data:image/png;base64,...",
      mimeType: "image/png"
    }
  ]
}
```

#### Example Usage

```javascript
{
  tool: "edit_asset",
  arguments: {
    sourceImage: "https://example.com/original.png",
    editInstructions: "Adjust lighting, increase contrast",
    preserveElements: ["logo", "text"]
  }
}
```

### 4. ensure_brand_consistency

Analyze assets for brand consistency and get recommendations.

#### Input Schema

```typescript
{
  assets: string[];            // Required: Assets to analyze
  brandGuidelines: string;     // Required: Brand guidelines
  referenceImages?: string[];  // Brand references
  colorPalette?: string[];     // Brand colors
  logoFile?: string;           // Official logo
}
```

#### Output Format

```typescript
{
  content: [
    {
      type: "text",
      text: "Brand Consistency Analysis Complete!..."
    },
    // Optionally includes refined/corrected images
    {
      type: "image",
      data: "data:image/png;base64,...",
      mimeType: "image/png"
    }
  ]
}
```

#### Example Usage

```javascript
{
  tool: "ensure_brand_consistency",
  arguments: {
    assets: ["url1", "url2", "url3"],
    brandGuidelines: "Modern, professional, blue/purple theme",
    colorPalette: ["#667EEA", "#764BA2"]
  }
}
```

## Aspect Ratios

Supported aspect ratios:

| Ratio | Description | Common Uses |
|-------|-------------|-------------|
| `1:1` | Square | Instagram posts, icons, avatars |
| `16:9` | Widescreen | YouTube, web banners, presentations |
| `9:16` | Vertical | Stories, mobile content |
| `4:3` | Traditional | Classic displays, some platforms |
| `3:4` | Portrait | Mobile-first designs |
| `21:9` | Ultra-wide | Cinematic banners, headers |
| `9:21` | Ultra-tall | Vertical scrolling content |
| `2:3` | Portrait | Photography, posters |
| `3:2` | Landscape | Photography, print |

## Resolutions

Supported resolutions:

| Resolution | Pixels | Use Case |
|------------|--------|----------|
| `1080x1080` | 1K square | Social media, icons |
| `1920x1080` | Full HD | Standard web, video |
| `2K` | 2560x1440 | High-quality web, retina |
| `4K` | 3840x2160 | Ultra-high quality, print |
| `3840x2160` | 4K explicit | Professional work |
| `2560x1440` | QHD | High-res displays |
| `1280x720` | HD | Optimized web assets |

## Image Input Formats

Reference images and logos can be provided as:

### 1. HTTPS URLs

```javascript
referenceImages: [
  "https://example.com/image1.jpg",
  "https://example.com/image2.png"
]
```

### 2. Data URLs (Base64)

```javascript
referenceImages: [
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUg..."
]
```

### 3. Mixed Formats

```javascript
referenceImages: [
  "https://example.com/image.jpg",
  "data:image/png;base64,iVBORw0KG..."
]
```

## Image Output Format

All generated images are returned as:

- **Format**: Base64-encoded data URLs
- **Type**: PNG (`image/png`)
- **Encoding**: UTF-8 base64 string
- **Structure**: `data:image/png;base64,<encoded-data>`

### Using Generated Images

#### In HTML

```html
<img src="data:image/png;base64,iVBORw0KG..." alt="Generated asset">
```

#### Saving to File (Node.js)

```javascript
const base64Data = imageUrl.replace(/^data:image\/png;base64,/, "");
const buffer = Buffer.from(base64Data, 'base64');
fs.writeFileSync('output.png', buffer);
```

#### Saving to File (Browser)

```javascript
const link = document.createElement('a');
link.href = imageDataUrl;
link.download = 'asset.png';
link.click();
```

## Error Handling

### Common Errors

#### 1. Missing API Key

```
Error: OPENROUTER_API_KEY environment variable is required
```

**Solution**: Set the environment variable

#### 2. Invalid Aspect Ratio

```
Error: Invalid aspect ratio specified
```

**Solution**: Use one of the supported ratios

#### 3. API Rate Limit

```
Error: OpenRouter API error: 429 - Rate limit exceeded
```

**Solution**: Wait and retry, or upgrade your OpenRouter plan

#### 4. Insufficient Credits

```
Error: OpenRouter API error: 402 - Insufficient credits
```

**Solution**: Add credits to your OpenRouter account

### Error Response Format

```typescript
{
  content: [
    {
      type: "text",
      text: "Error: <error message>"
    }
  ],
  isError: true
}
```

## Rate Limits

OpenRouter rate limits depend on your account tier:

- **Free Tier**: Limited requests per day
- **Paid Tier**: Higher limits based on plan

Check your usage at: https://openrouter.ai/dashboard

## Best Practices

### 1. Optimize Reference Images

- Compress images before sending
- Use appropriate resolutions (don't send 8K refs for 1K output)
- Limit to 5 reference images maximum

### 2. Efficient Prompting

- Be specific and detailed
- Include all requirements upfront
- Avoid multiple iterations when possible

### 3. Batch Operations

- Use `generate_asset_pack` instead of multiple `generate_asset` calls
- Reduces API calls and maintains consistency

### 4. Cache Results

- Store generated assets
- Reuse across projects when appropriate
- Reduces unnecessary regeneration

### 5. Error Recovery

- Implement retry logic with exponential backoff
- Handle rate limits gracefully
- Validate inputs before API calls

## Advanced Features

### Multi-Image Input

Provide multiple reference images for:
- Style fusion
- Composition guidance
- Color extraction
- Identity preservation

```javascript
referenceImages: [
  "style-reference.jpg",      // Overall style
  "color-palette.png",        // Color scheme
  "composition-guide.jpg",    // Layout structure
  "detail-example.jpg"        // Specific details
]
```

### Custom Resolution with Aspect Ratio

Specify both for precise control:

```javascript
{
  aspectRatio: "16:9",
  resolution: "3840x2160"  // 4K widescreen
}
```

### Brand Consistency Workflow

1. Generate initial asset
2. Create variations with `generate_asset_pack`
3. Validate with `ensure_brand_consistency`
4. Refine with `edit_asset` if needed
5. Final validation

## Support Resources

- **OpenRouter Docs**: https://openrouter.ai/docs
- **Model Page**: https://openrouter.ai/google/gemini-3-pro-image-preview
- **API Status**: https://status.openrouter.ai
- **GitHub Issues**: [Repository issues page]
- **MCP Protocol**: https://modelcontextprotocol.io

## Version History

- **1.0.0**: Initial release with image generation, editing, and brand consistency tools
