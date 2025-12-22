# Quick Start Guide

## Installation & Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Build the Project

```bash
npm run build
```

### 3. Set Your API Key

Get your API key from [OpenRouter](https://openrouter.ai/):

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

### 4. Validate Installation

```bash
./validate.sh
```

## Using with Claude Desktop

### Configure Claude Desktop

Edit your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

Add this configuration:

```json
{
  "mcpServers": {
    "nano-banana-assets": {
      "command": "node",
      "args": [
        "/absolute/path/to/openrouter-nano-banana-mcp/dist/index.js"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-your-key-here"
      }
    }
  }
}
```

Replace `/absolute/path/to/` with the actual path to this repository.

### Restart Claude Desktop

After saving the configuration, restart Claude Desktop for the changes to take effect.

## Quick Examples

Once configured, you can use these tools in Claude:

### Example 1: Generate a Simple Icon

```
Can you generate a minimalist home icon for my website? 
Use color #667EEA and make it 1:1 aspect ratio.
```

### Example 2: Create a Hero Banner

```
Generate a modern hero banner for a tech startup website. 
Use these colors: #667EEA, #764BA2, #F093FB
Aspect ratio: 16:9
Resolution: 1920x1080
```

### Example 3: Generate a Social Media Kit

```
Create a social media asset pack for an eco-friendly coffee brand with:
- Instagram post (square)
- Instagram story (vertical)
- Facebook cover
- Twitter header

Use natural, earthy colors: #2ECC71, #27AE60, #8B4513
```

### Example 4: Edit an Existing Asset

```
I have this image [provide URL or upload]. 
Can you adjust the lighting to be warmer and increase the contrast?
Keep the logo untouched.
```

### Example 5: Check Brand Consistency

```
I have these three assets [provide URLs or upload].
Can you check if they follow my brand guidelines?

Brand colors: #667EEA, #764BA2
Style: Modern, minimalist, professional
```

## Available Tools

The MCP server provides 4 main tools:

1. **`generate_asset`** - Generate single assets (icons, banners, backgrounds, etc.)
2. **`generate_asset_pack`** - Generate multiple related assets maintaining consistency
3. **`edit_asset`** - Edit existing assets with fine-grained controls
4. **`ensure_brand_consistency`** - Analyze assets for brand consistency

## Understanding Tool Parameters

### Aspect Ratios
- `1:1` - Square (Instagram posts, icons)
- `16:9` - Widescreen (YouTube, web banners)
- `9:16` - Vertical (Stories, mobile)
- `4:3`, `3:4` - Traditional formats
- `21:9`, `9:21` - Ultra-wide formats

### Resolutions
- `1080x1080` - Standard square
- `1920x1080` - Full HD
- `2K` (2560x1440) - High quality
- `4K` (3840x2160) - Ultra high quality

### Reference Images
- Provide up to 5 reference images
- Can be URLs or base64-encoded data
- Used for style guidance and consistency

### Color Palettes
- Provide as hex codes (e.g., `#667EEA`)
- Include 3-5 brand colors
- Used to maintain brand identity

## Tips for Best Results

### 1. Be Specific in Prompts
❌ "Make me a banner"  
✅ "Create a modern tech startup hero banner with gradient background from blue to purple, abstract geometric elements, and space for overlaying text"

### 2. Use Reference Images
Provide examples of the style you want:
- Style references
- Composition examples
- Color treatment examples

### 3. Specify the Use Case
Mention where the asset will be used:
- Website hero banner
- Social media post
- Email header
- UI component

### 4. Include Brand Elements
Always include:
- Logo (if applicable)
- Brand colors
- Style guidelines
- Tone (professional, playful, minimalist, etc.)

### 5. Iterate
- Start with a simple generation
- Review the result
- Use `edit_asset` to refine
- Use `ensure_brand_consistency` to validate

## Troubleshooting

### Server Not Showing in Claude

1. Check the config file path is correct
2. Ensure the JSON is valid (no trailing commas)
3. Verify the absolute path to `dist/index.js`
4. Restart Claude Desktop
5. Check Claude Desktop's developer console for errors

### API Key Errors

1. Verify your key starts with `sk-or-v1-`
2. Check the key is set in the config
3. Ensure you have credits on OpenRouter
4. Test the key at [OpenRouter Playground](https://openrouter.ai/playground)

### Generation Quality Issues

1. Provide more detailed prompts
2. Add reference images
3. Specify resolution and aspect ratio
4. Include brand guidelines
5. Try iterating with `edit_asset`

### Build Errors

```bash
# Clean and rebuild
rm -rf dist node_modules
npm install
npm run build
```

## Advanced Usage

### Multiple Configurations

You can set up multiple instances for different projects:

```json
{
  "mcpServers": {
    "nano-banana-project-a": {
      "command": "node",
      "args": ["/path/to/instance-a/dist/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "key-for-project-a"
      }
    },
    "nano-banana-project-b": {
      "command": "node",
      "args": ["/path/to/instance-b/dist/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "key-for-project-b"
      }
    }
  }
}
```

### Using with Other MCP Clients

The server follows the standard MCP protocol and works with any MCP-compatible client:

```bash
# Run directly
export OPENROUTER_API_KEY="your-key"
node dist/index.js
```

## Resources

- **Full Documentation:** [README.md](./README.md)
- **Examples:** [EXAMPLES.md](./EXAMPLES.md)
- **Configuration:** [CONFIG.md](./CONFIG.md)
- **OpenRouter Docs:** https://openrouter.ai/docs
- **MCP Protocol:** https://modelcontextprotocol.io

## Support

If you encounter issues:

1. Run `./validate.sh` to check your setup
2. Review the documentation files
3. Check OpenRouter status
4. Open an issue on GitHub

## Next Steps

1. ✅ Install and validate setup
2. ✅ Configure Claude Desktop
3. ✅ Try the quick examples above
4. 📖 Read [EXAMPLES.md](./EXAMPLES.md) for more use cases
5. 🎨 Start generating your own assets!

---

**Happy creating! 🎨**
