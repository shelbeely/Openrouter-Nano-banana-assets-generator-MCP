# OpenRouter Nano Banana Pro Assets Generator

A powerful asset generation solution that leverages OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview) for professional web asset generation and editing.

Available as both a **Model Context Protocol (MCP) server** and a **GitHub Copilot Agent Skill** (following the official GitHub specification).

## Overview

This project enables AI assistants to generate high-quality web assets, asset packs, and perform advanced image editing while maintaining brand consistency. It uses **Nano Banana Pro**, Google's most advanced image-generation and editing model built on Gemini 3 Pro.

### Two Ways to Use

1. **GitHub Copilot Agent Skill** - Official GitHub Copilot agent skill that loads automatically when you need asset generation
2. **MCP Server** - A full Model Context Protocol server for MCP-compatible clients

### Key Features

- 🎨 **Professional Asset Generation**: Create icons, banners, backgrounds, UI elements, and more
- 📦 **Asset Pack Creation**: Generate cohesive sets of related assets with consistent branding
- ✏️ **Advanced Image Editing**: Fine-grained controls for lighting, focus, localized edits, and transformations
- 🎯 **Brand Consistency**: Maintain visual identity across multiple assets with identity preservation
- 🖼️ **Multi-Modal Input**: Support for reference images, color palettes, and logo files
- 📐 **Flexible Formats**: Multiple aspect ratios (1:1, 16:9, 9:16, 21:9, etc.) and resolutions (up to 4K)
- 🌐 **Web-Optimized**: Assets designed specifically for web development workflows

## Quick Start

Choose your preferred method:

### Option 1: GitHub Copilot Agent Skill (Recommended)

The **GitHub Copilot Agent Skill** is automatically loaded by GitHub Copilot when you need asset generation.

1. **Set your API key** (one-time setup):
   ```bash
   # Run the interactive setup script
   ./setup-api-key.sh
   
   # Or manually set it
   export OPENROUTER_API_KEY="your-api-key-here"
   ```
   
   📖 **[Detailed API Key Setup Guide →](./OPENROUTER_API_KEY_SETUP.md)**

2. **Use with GitHub Copilot**:
   
   Just ask naturally in VS Code, CLI, or coding agent:
   ```
   "Generate a modern home icon for my website"
   "Create a hero banner with blue and purple gradient"
   "I need a social media kit for my brand"
   ```
   
   GitHub Copilot automatically uses the skill in `.github/skills/nano-banana-assets/`!

3. **Verify it works**:
   ```bash
   # Test the skill directly
   cd .github/skills/nano-banana-assets/scripts
   python generate_asset.py "Test icon" "1:1" "512x512"
   ```

📖 **[Full Agent Skill Documentation →](./.github/skills/README.md)**  
📖 **[Copilot Usage Guide →](./COPILOT_AGENT_USAGE.md)**

### Option 2: MCP Server

The **MCP Server** provides dedicated tools for MCP-compatible clients like Claude Desktop.

1. **Set your API key**:
   ```bash
   export OPENROUTER_API_KEY="your-api-key-here"
   ```

2. **Install dependencies**:
   ```bash
   npm install
   npm run build
   ```

2. **Set your API key**:
   ```bash
   export OPENROUTER_API_KEY="your-api-key-here"
   ```

3. **Configure MCP client** (e.g., Claude Desktop):

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

Get your API key from [OpenRouter](https://openrouter.ai/).

## Comparison: Agent Skill vs MCP Server

| Feature | Agent Skill | MCP Server |
|---------|-------------|------------|
| **Installation** | Copy directory | npm install + build |
| **Configuration** | Environment variable | MCP client config |
| **Platform Support** | All Agent Skills-compatible platforms | MCP-compatible clients |
| **Portability** | Highly portable | Requires Node.js |
| **Usage** | Natural language | Tool calls |
| **Maintenance** | Minimal | Standard npm package |

**Use Agent Skill when:**
- You want maximum portability
- You're using multiple AI platforms
- You prefer minimal setup

**Use MCP Server when:**
- You're already using MCP clients
- You want structured tool calls
- You prefer the MCP ecosystem

Both provide the same capabilities and quality!

## Available Capabilities

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

Nano Banana Pro (via OpenRouter) offers:

- **Advanced Multimodal Reasoning**: Understands context from reference images, logos, and descriptions
- **High-Fidelity Visual Synthesis**: Professional-quality outputs suitable for production
- **Text Rendering**: Industry-leading text placement in images with multilingual support
- **Identity Preservation**: Consistent styling across multiple assets (up to 5 subject references)
- **Fine-Grained Controls**: Localized edits, lighting adjustments, focus control, camera transformations
- **Flexible Output**: Support for multiple aspect ratios (1:1, 16:9, 9:16, 21:9, etc.)
- **Search Grounding**: Real-time information integration for context-rich graphics
- **Base64 Image Output**: Generated images are returned as base64-encoded data URLs

## How It Works

The server uses OpenRouter's image generation API with the following key features:

1. **Modalities**: Requests specify `["image", "text"]` to enable image generation
2. **Image Configuration**: Aspect ratios are passed via `image_config.aspect_ratio`
3. **Reference Images**: Input images are provided as URLs or base64 data for style guidance
4. **Response Format**: Generated images are returned in the `message.images` array as base64 data URLs
5. **Multiple Outputs**: The model can generate multiple variations or asset types in a single request

## Use Cases

- **Web Development**: Generate UI components, icons, backgrounds, and layouts
- **Brand Identity**: Create consistent asset packs for marketing materials
- **Product Design**: Visualize products and create mockups
- **Content Creation**: Social media graphics, blog headers, and promotional materials
- **Prototyping**: Quick generation of design concepts and variations
- **Asset Management**: Edit and refine existing assets while maintaining brand consistency

## Technical Details

### MCP Server
- **Model**: `google/gemini-3-pro-image-preview` via OpenRouter
- **API Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Protocol**: Model Context Protocol (MCP)
- **Transport**: stdio
- **Runtime**: Node.js with TypeScript
- **Image Format**: Base64-encoded data URLs (PNG)
- **Modalities**: `["image", "text"]` for image generation capabilities

### Agent Skill
- **Standard**: [Agent Skills](https://agentskills.io) specification v1.0
- **Format**: SKILL.md with YAML frontmatter + Markdown instructions
- **Compatibility**: All Agent Skills-compatible platforms
- **Scripts**: Bash and Python helper scripts included
- **Documentation**: Comprehensive references and templates
- **Requirements**: OpenRouter API key, internet access

### API Implementation

The server implements OpenRouter's multimodal image generation API:

```typescript
{
  model: "google/gemini-3-pro-image-preview",
  messages: [{ role: "user", content: [...] }],
  modalities: ["image", "text"],
  image_config: {
    aspect_ratio: "16:9"  // Configurable
  }
}
```

Response format:
```typescript
{
  choices: [{
    message: {
      content: "...",  // Text description
      images: [{       // Generated images
        image_url: { url: "data:image/png;base64,..." }
      }]
    }
  }]
}
```

## Development

### MCP Server Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Watch mode for development
npm run watch

# Test
npm run test
```

### Agent Skill Development

The Agent Skill is ready to use - no build step required! To modify:

1. Edit `nano-banana-assets-skill/SKILL.md` for instructions
2. Update scripts in `nano-banana-assets-skill/scripts/` as needed
3. Add reference materials to `nano-banana-assets-skill/references/`
4. Test with a compatible AI agent

## Project Structure

```
.
├── src/                           # MCP server source code
│   └── index.ts                   # Main server implementation
├── dist/                          # Built MCP server
│   └── index.js                   # Compiled server
├── nano-banana-assets-skill/      # Agent Skill (portable)
│   ├── SKILL.md                   # Main skill definition
│   ├── README.md                  # Skill documentation
│   ├── scripts/                   # Helper scripts
│   │   ├── generate_asset.sh      # Bash helper
│   │   └── generate_asset.py      # Python helper
│   ├── references/                # Reference docs
│   │   ├── api-reference.md       # API documentation
│   │   └── prompt-templates.md    # Prompt examples
│   └── assets/                    # Example assets
├── README.md                      # This file
├── EXAMPLES.md                    # Usage examples
├── CONFIG.md                      # Configuration guide
├── QUICKSTART.md                  # Quick start guide
└── package.json                   # npm package config
```

## Requirements

### For MCP Server
- Node.js 18 or higher
- OpenRouter API key
- MCP-compatible client (e.g., Claude Desktop)

### For Agent Skill
- OpenRouter API key
- Agent Skills-compatible AI platform
- Internet access
- (Optional) Python 3.10+ for Python scripts

## Documentation

- **[Agent Skill Documentation](./nano-banana-assets-skill/README.md)** - Complete guide to using the Agent Skill
- **[Quick Start Guide](./QUICKSTART.md)** - Get started quickly with MCP server
- **[Examples](./EXAMPLES.md)** - Detailed usage examples
- **[Configuration](./CONFIG.md)** - Configuration options
- **[API Reference](./API.md)** - API documentation

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- Built with [Model Context Protocol SDK](https://github.com/modelcontextprotocol)
- Follows [Agent Skills](https://agentskills.io) specification
- Powered by [OpenRouter](https://openrouter.ai/)
- Uses Google's Nano Banana Pro (Gemini 3 Pro Image Preview)