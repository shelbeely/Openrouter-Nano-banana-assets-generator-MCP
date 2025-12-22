# OpenRouter Nano Banana Pro Assets Generator MCP

A powerful Model Context Protocol (MCP) server that leverages OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview) for professional web asset generation and editing.

## Overview

This MCP server enables AI assistants to generate high-quality web assets, asset packs, and perform advanced image editing while maintaining brand consistency. It uses **Nano Banana Pro**, Google's most advanced image-generation and editing model built on Gemini 3 Pro.

### Key Features

- 🎨 **Professional Asset Generation**: Create icons, banners, backgrounds, UI elements, and more
- 📦 **Asset Pack Creation**: Generate cohesive sets of related assets with consistent branding
- ✏️ **Advanced Image Editing**: Fine-grained controls for lighting, focus, localized edits, and transformations
- 🎯 **Brand Consistency**: Maintain visual identity across multiple assets with identity preservation
- 🖼️ **Multi-Modal Input**: Support for reference images, color palettes, and logo files
- 📐 **Flexible Formats**: Multiple aspect ratios (1:1, 16:9, 9:16, 21:9, etc.) and resolutions (up to 4K)
- 🌐 **Web-Optimized**: Assets designed specifically for web development workflows

## Installation

```bash
npm install
npm run build
```

## Configuration

Set your OpenRouter API key as an environment variable:

```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

You can obtain an API key from [OpenRouter](https://openrouter.ai/).

## Usage

### With Claude Desktop

Add this configuration to your Claude Desktop config file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "nano-banana-assets": {
      "command": "node",
      "args": ["/absolute/path/to/openrouter-nano-banana-mcp/dist/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### Standalone Usage

```bash
# Set your API key
export OPENROUTER_API_KEY="your-api-key-here"

# Run the server
node dist/index.js
```

## Available Tools

### 1. `generate_asset`

Generate a single web asset with full control over style, format, and branding.

**Parameters:**
- `prompt` (required): Detailed description of the asset
- `aspectRatio`: "1:1", "16:9", "9:16", "4:3", "21:9", etc.
- `resolution`: "1920x1080", "2K", "4K", etc.
- `referenceImages`: Array of image URLs for style guidance (max 5)
- `colorPalette`: Array of hex color codes
- `logoFile`: Logo URL or base64 data
- `editInstructions`: Optional editing instructions

**Example:**
```
Generate a hero banner with:
- Prompt: "Modern tech startup hero banner with gradient background"
- Aspect Ratio: 16:9
- Resolution: 1920x1080
- Color Palette: ["#667EEA", "#764BA2"]
```

### 2. `generate_asset_pack`

Create a complete set of related assets with consistent branding.

**Parameters:**
- `description` (required): Overall purpose of the asset pack
- `assetTypes` (required): Array of asset types to generate
- `brandGuidelines`: Brand style requirements
- `referenceImages`: Reference images for visual style
- `colorPalette`: Brand color palette
- `logoFile`: Brand logo
- `aspectRatio`: Default aspect ratio
- `resolution`: Default resolution

**Example:**
```
Generate an asset pack with:
- Description: "Social media kit for eco-friendly brand"
- Asset Types: ["instagram-post", "facebook-cover", "twitter-header", "icon-set"]
- Brand Guidelines: "Minimalist, nature-inspired, clean aesthetics"
- Color Palette: ["#2ECC71", "#27AE60", "#F1C40F"]
```

### 3. `edit_asset`

Edit existing assets with advanced controls.

**Parameters:**
- `sourceImage` (required): Image URL or base64 data
- `editInstructions` (required): Detailed editing instructions
- `preserveElements`: Elements to keep unchanged
- `aspectRatio`: Target aspect ratio
- `resolution`: Target resolution

**Example:**
```
Edit an asset with:
- Source Image: [URL or base64]
- Edit Instructions: "Adjust lighting to be warmer, increase contrast, soften shadows"
- Preserve Elements: ["logo", "text"]
```

### 4. `ensure_brand_consistency`

Analyze assets for brand consistency and get recommendations.

**Parameters:**
- `assets` (required): Array of asset URLs to analyze
- `brandGuidelines` (required): Brand guidelines
- `referenceImages`: Brand reference images
- `colorPalette`: Official brand colors
- `logoFile`: Official logo

**Example:**
```
Check consistency of:
- Assets: [multiple URLs]
- Brand Guidelines: "Modern, professional, use primary blue #667EEA"
- Color Palette: ["#667EEA", "#764BA2", "#FFFFFF"]
```

## Model Capabilities

Nano Banana Pro offers:

- **Advanced Multimodal Reasoning**: Understands context from reference images, logos, and descriptions
- **High-Fidelity Visual Synthesis**: Professional-quality outputs suitable for production
- **Text Rendering**: Industry-leading text placement in images with multilingual support
- **Identity Preservation**: Consistent styling across multiple assets (up to 5 subject references)
- **Fine-Grained Controls**: Localized edits, lighting adjustments, focus control, camera transformations
- **Flexible Output**: 2K/4K support, multiple aspect ratios, web-optimized formats
- **Search Grounding**: Real-time information integration for context-rich graphics

## Use Cases

- **Web Development**: Generate UI components, icons, backgrounds, and layouts
- **Brand Identity**: Create consistent asset packs for marketing materials
- **Product Design**: Visualize products and create mockups
- **Content Creation**: Social media graphics, blog headers, and promotional materials
- **Prototyping**: Quick generation of design concepts and variations
- **Asset Management**: Edit and refine existing assets while maintaining brand consistency

## Technical Details

- **Model**: `google/gemini-3-pro-image-preview` via OpenRouter
- **Protocol**: Model Context Protocol (MCP)
- **Transport**: stdio
- **Runtime**: Node.js with TypeScript

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Watch mode for development
npm run watch
```

## Requirements

- Node.js 18 or higher
- OpenRouter API key
- MCP-compatible client (e.g., Claude Desktop)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- Built with [Model Context Protocol SDK](https://github.com/modelcontextprotocol)
- Powered by [OpenRouter](https://openrouter.ai/)
- Uses Google's Nano Banana Pro (Gemini 3 Pro Image Preview)