# Nano Banana Assets - Agent Skill

An Agent Skill for generating professional web assets using OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview).

## Overview

This is an **Agent Skill** following the [agentskills.io](https://agentskills.io) standard. It enables AI agents to generate high-quality web assets, icons, banners, backgrounds, and more using OpenRouter's API.

## What is an Agent Skill?

Agent Skills are a standardized way to package instructions, scripts, and resources that teach AI agents how to perform specialized tasks. This skill teaches agents how to:

- Generate single web assets (icons, banners, backgrounds, etc.)
- Create cohesive asset packs with consistent branding
- Edit existing images with fine-grained controls
- Ensure brand consistency across multiple assets

## Skill Structure

```
nano-banana-assets-skill/
├── SKILL.md              # Main skill definition (START HERE)
├── README.md             # This file
├── scripts/              # Helper scripts
│   ├── generate_asset.sh # Bash script for asset generation
│   └── generate_asset.py # Python script for asset generation
├── references/           # Reference documentation
│   ├── api-reference.md  # OpenRouter API documentation
│   └── prompt-templates.md # Prompt templates and examples
└── assets/              # (Empty) Example assets would go here
```

## For AI Agents

**If you are an AI agent**, read the `SKILL.md` file. It contains:

- Complete instructions for generating assets
- API call formats and examples
- Prompt engineering best practices
- Error handling guidelines
- Supported parameters and options

## For Humans

### Using This Skill

#### With Compatible AI Assistants

This skill works with any AI agent that supports the Agent Skills standard, including:

- **Claude Desktop** (via agent skills)
- **GitHub Copilot** (via skills)
- **VS Code Copilot** (via skills)
- **Cursor** (via skills)
- Other compatible platforms

#### Installation

1. **Copy this directory** to your agent's skills directory:
   - Claude Desktop: `~/.config/Claude/skills/` (Linux/Mac)
   - VS Code: Follow VS Code agent skills documentation
   - Other: Check your platform's documentation

2. **Set environment variable**:
   ```bash
   export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
   ```

3. **Restart your agent** to load the new skill

#### Testing the Skill

Once installed, try asking your AI assistant:

```
"Can you use the nano-banana-assets skill to generate a modern hero banner?"
```

or

```
"Generate an icon set using the asset generation skill"
```

### Prerequisites

- **OpenRouter API Key**: Get one from [OpenRouter](https://openrouter.ai/)
- **Internet Access**: Required for API calls
- **Credits**: OpenRouter uses a credit-based system

### Manual Usage

You can also use the helper scripts directly:

#### Bash Script

```bash
cd nano-banana-assets-skill/scripts
export OPENROUTER_API_KEY="your-key"
./generate_asset.sh "Modern tech startup hero banner" "16:9" "1920x1080"
```

#### Python Script

```bash
cd nano-banana-assets-skill/scripts
export OPENROUTER_API_KEY="your-key"
python generate_asset.py "Modern tech startup hero banner" "16:9" "1920x1080"
```

The Python script provides more functionality:

```python
from generate_asset import AssetGenerator

generator = AssetGenerator()

# Generate single asset
response = generator.generate_asset(
    prompt="Modern hero banner",
    aspect_ratio="16:9",
    resolution="1920x1080",
    color_palette=["#667EEA", "#764BA2"]
)

# Generate asset pack
response = generator.generate_asset_pack(
    description="Social media kit",
    asset_types=["instagram-post", "facebook-cover"],
    brand_guidelines="Modern, minimalist, professional"
)

# Edit existing asset
response = generator.edit_asset(
    source_image="https://example.com/image.png",
    edit_instructions="Make warmer and brighter"
)

# Save images
generator.save_images_from_response(response, "my-asset")
```

## Capabilities

### 1. Generate Single Assets
- Icons (all styles and sizes)
- Banners (hero, header, footer)
- Backgrounds (patterns, gradients, scenes)
- UI elements (buttons, cards, badges)
- Social media graphics
- And more...

### 2. Generate Asset Packs
- Social media kits
- Brand identity packs
- Icon sets
- UI component libraries
- Marketing materials
- Consistent multi-asset sets

### 3. Edit Existing Assets
- Lighting adjustments
- Color corrections
- Element additions/removals
- Style transformations
- Resolution changes
- Aspect ratio changes

### 4. Brand Consistency
- Analyze multiple assets
- Check brand guideline compliance
- Identify inconsistencies
- Suggest improvements
- Generate corrected versions

## Supported Formats

### Aspect Ratios
- `1:1` - Square (Instagram, icons)
- `16:9` - Widescreen (YouTube, banners)
- `9:16` - Vertical (Stories)
- `4:3`, `3:4` - Traditional
- `21:9`, `9:21` - Ultra-wide
- `2:3`, `3:2` - Photography

### Resolutions
- `1080x1080` - Standard square
- `1920x1080` - Full HD
- `2K` (2560x1440) - High quality
- `4K` (3840x2160) - Ultra quality
- Custom sizes supported

### Output Format
- PNG (base64-encoded data URLs)
- High quality
- Web-optimized

## Documentation

- **[SKILL.md](./SKILL.md)** - Complete skill definition and instructions
- **[api-reference.md](./references/api-reference.md)** - OpenRouter API details
- **[prompt-templates.md](./references/prompt-templates.md)** - Tested prompt templates

## Examples

### Example 1: Generate an Icon

```
Agent, use the nano-banana-assets skill to generate a minimalist home icon
with color #667EEA, square aspect ratio, 512x512 resolution.
```

### Example 2: Create Social Media Kit

```
I need a social media kit for an eco-friendly brand. Use the asset generation
skill to create:
- Instagram post (square)
- Instagram story (vertical)
- Facebook cover
- Twitter header

Use colors: #2ECC71, #27AE60
Style: Natural, organic, minimalist
```

### Example 3: Edit an Image

```
Using the nano-banana-assets skill, edit this image [URL] to make it warmer
and brighter. Preserve the logo in the corner.
```

## Comparison with MCP Server

This repository also includes a full **Model Context Protocol (MCP) server** that provides the same functionality. The differences:

| Feature | Agent Skill | MCP Server |
|---------|-------------|------------|
| Format | Agent Skills standard | MCP protocol |
| Installation | Copy to skills directory | Configure in MCP client |
| Usage | Natural language commands | Tool calls |
| Platform | Skills-compatible agents | MCP-compatible clients |
| Integration | Lightweight, portable | Full server/client protocol |

**When to use each:**

- **Agent Skill**: You want AI agents to learn how to generate assets as part of their capabilities
- **MCP Server**: You want a dedicated server providing asset generation tools to MCP clients

Both approaches use the same underlying OpenRouter API and produce the same quality results.

## Development

### Testing Changes

After modifying the skill:

1. Update `SKILL.md` with changes
2. Test with compatible agent
3. Verify all examples still work
4. Update version in metadata

### Contributing

Contributions are welcome! To contribute:

1. Test your changes thoroughly
2. Update documentation
3. Follow the Agent Skills specification
4. Submit a pull request

## Troubleshooting

### Skill Not Loading

1. Check file structure matches specification
2. Verify `SKILL.md` has valid YAML frontmatter
3. Restart your agent
4. Check agent's skills directory path

### API Errors

1. Verify `OPENROUTER_API_KEY` is set correctly
2. Check you have credits on OpenRouter
3. Ensure internet connectivity
4. Review error messages in agent output

### Poor Quality Results

1. Use more detailed prompts
2. Add reference images when possible
3. Specify colors with hex codes
4. Include style and mood descriptors
5. Review prompt templates for examples

## Resources

- **Agent Skills Specification**: https://agentskills.io
- **OpenRouter Platform**: https://openrouter.ai
- **GitHub Repository**: https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP
- **Model Documentation**: OpenRouter Nano Banana Pro

## License

MIT License - See the repository LICENSE file for details.

## Support

For issues or questions:

1. Check the documentation in this skill
2. Review the [prompt templates](./references/prompt-templates.md)
3. Consult the [API reference](./references/api-reference.md)
4. Open an issue on GitHub
5. Contact OpenRouter support for API-related issues

## Version

Current version: **1.0.0**

See `SKILL.md` metadata for version information.

---

**Happy asset generating! 🎨**
