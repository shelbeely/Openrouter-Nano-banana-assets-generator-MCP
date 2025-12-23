# Using the Nano Banana Assets Skill with GitHub Copilot

This guide explains how to use the nano-banana-assets skill within the GitHub Copilot coding agent environment.

## Overview

The `nano-banana-assets` is an **official GitHub Copilot Agent Skill** that follows the [GitHub Agent Skills specification](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills). GitHub Copilot agents can use this skill to generate professional web assets, icons, banners, backgrounds, and more using OpenRouter's Nano Banana Pro model.

## What is a GitHub Copilot Agent Skill?

According to GitHub's documentation, Agent Skills are special folders containing instructions, scripts, and resources that GitHub Copilot agents can load to perform specialized, repeatable tasks. These skills:

- Expand Copilot's capabilities beyond code completion
- Are automatically loaded when relevant to your prompt or coding context
- Are portable across Copilot CLI, Copilot coding agent, and VS Code
- Allow domain-specific best practices and workflows

The nano-banana-assets skill teaches agents to:

1. **Generate single web assets** - Icons, banners, backgrounds, UI elements
2. **Create asset packs** - Multiple related assets with consistent branding
3. **Edit existing images** - Fine-grained image editing and transformations
4. **Ensure brand consistency** - Analyze and maintain visual identity

## How GitHub Copilot Agents Use This Skill

### 1. Official Skill Structure

Following GitHub's specification, the skill is located in `.github/skills/nano-banana-assets/`:

```
.github/skills/nano-banana-assets/
├── SKILL.md              # Main skill definition (required)
├── README.md             # Skill documentation
├── scripts/              # Helper scripts
│   ├── generate_asset.py # Python implementation
│   └── generate_asset.sh # Bash implementation
└── references/           # API docs and templates
```

**Note:** For backward compatibility, the skill is also available in the `nano-banana-assets-skill/` directory.

### 2. How GitHub Copilot Loads This Skill

**Automatic Detection:**
- GitHub Copilot automatically detects and loads this skill when you ask for asset generation tasks
- When you mention keywords like "generate icon", "create banner", "design assets", Copilot uses this skill
- No manual loading required - it's context-aware!

**What's in SKILL.md:**

The SKILL.md file has two parts:

1. **YAML Frontmatter** (required by GitHub):
   ```yaml
   ---
   name: nano-banana-assets
   description: Generate professional web assets, icons, banners...
   ---
   ```

2. **Markdown Instructions** - Complete guidance including:
   - Core capabilities and when to use them
   - API call formats and examples
   - Prompt engineering best practices
   - Error handling guidelines
   - Supported parameters

### 3. API Configuration

The skill uses OpenRouter's API:
- **Base URL:** `https://openrouter.ai/api/v1/chat/completions`
- **Model:** `google/gemini-3-pro-image-preview` (Nano Banana Pro)
- **Authentication:** Bearer token via `OPENROUTER_API_KEY` environment variable

## Practical Usage for Copilot Agents

### Prerequisites

Before using the skill, ensure:
- OpenRouter API key is available (set as `OPENROUTER_API_KEY` environment variable)
- Internet access for API calls
- Python 3.10+ or Bash available for helper scripts

### Method 1: Using Helper Scripts

The skill includes ready-to-use scripts in `.github/skills/nano-banana-assets/scripts/`:

#### Python Script

```python
from pathlib import Path
import sys

# Add the skill scripts to path
skill_path = Path('.github/skills/nano-banana-assets/scripts')
sys.path.insert(0, str(skill_path))

from generate_asset import AssetGenerator

# Initialize
generator = AssetGenerator()

# Generate single asset
response = generator.generate_asset(
    prompt="Modern hero banner for tech startup",
    aspect_ratio="16:9",
    resolution="1920x1080",
    color_palette=["#667EEA", "#764BA2"]
)

# Save generated images
generator.save_images_from_response(response, "hero-banner")
```

#### Bash Script

```bash
cd .github/skills/nano-banana-assets/scripts
./generate_asset.sh "Modern hero banner" "16:9" "1920x1080"
```

### Method 2: Direct API Calls

Follow the patterns in `SKILL.md` to make direct HTTP requests:

```bash
curl -X POST "https://openrouter.ai/api/v1/chat/completions" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-3-pro-image-preview",
    "messages": [{
      "role": "user",
      "content": [{
        "type": "text",
        "text": "Generate a modern hero banner..."
      }]
    }],
    "modalities": ["image", "text"],
    "image_config": {
      "aspect_ratio": "16:9"
    }
  }'
```

### Method 3: Understanding and Following Instructions

As an AI agent, you should:

1. **Parse the SKILL.md** to understand capabilities
2. **Match user requests** to the appropriate operation
3. **Build proper prompts** following the templates
4. **Make API calls** using the correct format
5. **Extract and present results** to the user

## Example: Agent Workflow

When a user asks: *"Generate a modern icon for my website"*

### Step 1: Identify the Operation
- This is a **single asset generation** task
- Refer to "Generate a Single Asset" section in SKILL.md

### Step 2: Collect Requirements
```
Asset type: icon
Style: modern
Use case: website navigation
Aspect ratio: 1:1 (square)
Resolution: 512x512
```

### Step 3: Build the Prompt
```
Generate a high-quality icon with the following specifications:

Description: Modern, minimalist icon for website navigation. 
Clean lines, professional appearance, suitable for use in a nav bar.

Aspect Ratio: 1:1
Resolution: 512x512

Requirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance
```

### Step 4: Make API Call
Use the Python script or direct API call with the constructed prompt.

### Step 5: Extract Results
- Parse the response JSON
- Extract images from `choices[0].message.images[]`
- Save or present images to the user

## Common Use Cases

### 1. Generate Social Media Assets

```bash
# Using Python script
python scripts/generate_asset.py \
  "Instagram post for eco-friendly brand" \
  "1:1" \
  "1080x1080"
```

### 2. Create Brand Asset Pack

```python
generator.generate_asset_pack(
    description="Social media kit for coffee shop",
    asset_types=["instagram-post", "facebook-cover", "twitter-header"],
    brand_guidelines="Cozy, artisan, warm atmosphere",
    color_palette=["#6F4E37", "#DEB887", "#FFFDD0"]
)
```

### 3. Edit Existing Asset

```python
generator.edit_asset(
    source_image="https://example.com/banner.png",
    edit_instructions="Make warmer and brighter, increase contrast",
    preserve_elements=["logo", "text"]
)
```

## Environment Variables

The skill requires the OpenRouter API key:

```bash
# Set in your environment
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Or pass to scripts
OPENROUTER_API_KEY="sk-or-v1-..." python generate_asset.py "prompt"
```

## Response Format

Generated images are returned as base64-encoded data URLs:

```json
{
  "choices": [{
    "message": {
      "content": "Description of the generated asset...",
      "images": [{
        "image_url": {
          "url": "data:image/png;base64,iVBORw0KGgo..."
        }
      }]
    }
  }]
}
```

To use the images:
1. **Save to file**: Decode base64 and write to PNG file
2. **Display in HTML**: Use data URL directly in `<img src="...">`
3. **Further processing**: Pass to other tools

## Skill Capabilities Reference

### Supported Aspect Ratios
- `1:1` - Square (icons, Instagram)
- `16:9` - Widescreen (banners, YouTube)
- `9:16` - Vertical (Stories)
- `4:3`, `3:4` - Traditional
- `21:9`, `9:21` - Ultra-wide

### Supported Resolutions
- `512x512` - Small icons
- `1080x1080` - Standard square
- `1920x1080` - Full HD
- `2K` (2560x1440) - High quality
- `4K` (3840x2160) - Ultra quality

### Asset Types
- Icons and icon sets
- Hero banners
- Backgrounds and patterns
- Social media graphics
- UI components
- Product visualizations
- Marketing materials

## Best Practices for Agents

1. **Read SKILL.md First** - All instructions are there
2. **Use Detailed Prompts** - More detail = better results
3. **Specify Colors** - Use hex codes (#667EEA)
4. **Include Context** - Mention the use case
5. **Provide References** - When available, include reference images
6. **Handle Errors** - Check API responses for errors
7. **Save Results** - Preserve generated assets appropriately

## Troubleshooting

### Common Issues

**API Key Not Set**
```bash
# Check if set
echo $OPENROUTER_API_KEY

# Set it
export OPENROUTER_API_KEY="sk-or-v1-..."
```

**Script Not Executable**
```bash
chmod +x nano-banana-assets-skill/scripts/generate_asset.sh
```

**Python Dependencies**
```bash
pip install requests
```

**API Errors**
- 401: Invalid API key
- 402: Insufficient credits
- 429: Rate limit exceeded
- 500: Server error (retry)

## Integration with GitHub Copilot Workflow

### Scenario 1: Development Workflow

When building a website, use the skill to:
1. Generate hero banners for landing pages
2. Create icon sets for navigation
3. Generate background patterns
4. Produce social media assets
5. Maintain brand consistency

### Scenario 2: Automated Asset Generation

Integrate into CI/CD:
```yaml
# .github/workflows/assets.yml
- name: Generate Assets
  env:
    OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
  run: |
    python nano-banana-assets-skill/scripts/generate_asset.py \
      "Hero banner for homepage" "16:9" "1920x1080"
```

### Scenario 3: Interactive Development

As a Copilot agent assisting a developer:
1. Listen for asset-related requests
2. Use the skill to generate assets
3. Save assets to the project directory
4. Update HTML/CSS to reference new assets
5. Validate results with the developer

## Testing the Skill

### Quick Test

```bash
# Set API key (use a real key)
export OPENROUTER_API_KEY="sk-or-v1-test-key"

# Test Python script
cd nano-banana-assets-skill/scripts
python generate_asset.py "Test icon" "1:1" "512x512"

# Check output
ls -la asset_*.png response.json
```

### Validation Checklist

- [ ] API key is set
- [ ] Scripts are executable
- [ ] Python dependencies installed
- [ ] Can make successful API call
- [ ] Images are generated and saved
- [ ] Response includes description and images

## Skill vs MCP Server

This repository includes both:

| Feature | Agent Skill | MCP Server |
|---------|-------------|------------|
| **Format** | Instructions + Scripts | Full MCP Protocol |
| **Usage** | Read SKILL.md, use scripts | Tool calls via MCP |
| **Portability** | Highly portable | Requires Node.js |
| **Integration** | Any agent | MCP clients only |
| **Best For** | Agent learning | Structured tools |

**As a GitHub Copilot agent, you're using the Agent Skill approach** - reading instructions and using the provided scripts or API patterns.

## Resources

- **SKILL.md** - Complete skill instructions (READ THIS!)
- **API Reference** - `references/api-reference.md`
- **Prompt Templates** - `references/prompt-templates.md`
- **Examples** - `EXAMPLES.md` in root directory
- **OpenRouter Docs** - https://openrouter.ai/docs

## Summary

To use the nano-banana-assets skill as a GitHub Copilot agent:

1. ✅ Read `nano-banana-assets-skill/SKILL.md` for complete instructions
2. ✅ Set the `OPENROUTER_API_KEY` environment variable
3. ✅ Use the Python or Bash scripts in `scripts/` directory
4. ✅ Follow the prompt templates and API patterns in SKILL.md
5. ✅ Parse responses and extract generated images
6. ✅ Present results to users or save to project files

The skill provides everything needed to generate professional web assets programmatically!
