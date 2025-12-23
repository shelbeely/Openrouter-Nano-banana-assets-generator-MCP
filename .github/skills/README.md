# GitHub Copilot Agent Skills

This directory contains Agent Skills for GitHub Copilot, following the [official GitHub Agent Skills specification](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

## About Agent Skills

Agent Skills are special folders containing instructions, scripts, and resources that GitHub Copilot agents can load to perform specialized, repeatable tasks. When you use GitHub Copilot in:

- **VS Code** (with Copilot agent mode)
- **GitHub Copilot CLI**
- **Copilot coding agent**

These skills are automatically detected and loaded when relevant to your coding task.

## Available Skills

### nano-banana-assets

Generate professional web assets, icons, banners, backgrounds, and UI elements using OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview).

**Capabilities:**
- Generate single assets (icons, banners, backgrounds, UI elements)
- Create cohesive asset packs with consistent branding
- Edit existing images with fine-grained controls
- Ensure brand consistency across multiple assets

**Usage Example:**

Just ask GitHub Copilot naturally:
```
"Generate a modern home icon for my website navigation"
"Create a hero banner for my tech startup with blue and purple gradient"
"I need a complete social media kit for my coffee brand"
```

Copilot will automatically use this skill to generate the assets!

**Documentation:**
- [Skill Documentation](./nano-banana-assets/README.md)
- [Complete Skill Definition](./nano-banana-assets/SKILL.md)

**Requirements:**
- OpenRouter API key (set as `OPENROUTER_API_KEY` environment variable)
- Internet access for API calls
- Get your API key at: https://openrouter.ai/

## How Skills Work

### Directory Structure

```
.github/skills/
├── README.md                    # This file
└── nano-banana-assets/          # Each skill has its own directory
    ├── SKILL.md                 # Required: Skill definition with YAML frontmatter
    ├── README.md                # Optional: Additional documentation
    ├── scripts/                 # Optional: Helper scripts
    │   ├── generate_asset.py
    │   └── generate_asset.sh
    └── references/              # Optional: Reference materials
        ├── api-reference.md
        └── prompt-templates.md
```

### SKILL.md Format

Each skill must have a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what this skill does
---

# Detailed instructions in Markdown...
```

### Automatic Loading

GitHub Copilot automatically:
1. Detects when a skill is relevant to your prompt
2. Loads the skill's instructions
3. Uses the skill to complete your task
4. Can access scripts and resources in the skill directory

## Using Skills in This Repository

### In VS Code with Copilot

1. Open this repository in VS Code
2. Ensure GitHub Copilot extension is installed and active
3. Start a conversation with Copilot (Ctrl+I or Cmd+I)
4. Ask for asset generation tasks - Copilot will use the skill automatically!

**Example:**
```
User: "Create a 1920x1080 hero banner for my landing page with a gradient background"

Copilot: [Automatically loads nano-banana-assets skill and generates the asset]
```

### In GitHub Copilot CLI

```bash
# The skill is available when using gh copilot
gh copilot suggest "generate a modern icon set"
```

### In Copilot Coding Agent

When working with the Copilot coding agent, simply mention asset-related tasks:
- "Generate assets for my project"
- "Create icons for the navigation"
- "Design a hero banner"

The agent will automatically use the nano-banana-assets skill.

## Setting Up

### 1. Set API Key

The nano-banana-assets skill requires an OpenRouter API key:

```bash
# In your shell profile (~/.bashrc, ~/.zshrc, etc.)
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

Or in VS Code settings.json:
```json
{
  "terminal.integrated.env.linux": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key-here"
  },
  "terminal.integrated.env.osx": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key-here"
  },
  "terminal.integrated.env.windows": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key-here"
  }
}
```

### 2. Verify Installation

```bash
# Check the skill exists
ls -la .github/skills/nano-banana-assets/SKILL.md

# Check scripts are executable
ls -la .github/skills/nano-banana-assets/scripts/
```

### 3. Test the Skill

```bash
# Test using the Python script directly
cd .github/skills/nano-banana-assets/scripts
python generate_asset.py "Test icon" "1:1" "512x512"
```

## Creating Your Own Skills

To add more skills to this repository:

1. **Create a directory** in `.github/skills/`
   ```bash
   mkdir -p .github/skills/my-custom-skill
   ```

2. **Create SKILL.md** with required frontmatter
   ```yaml
   ---
   name: my-custom-skill
   description: What this skill does
   ---
   
   # Instructions
   
   Detailed instructions for how to use this skill...
   ```

3. **Add resources** (optional)
   - Scripts in `scripts/`
   - Documentation in `references/`
   - Examples in `examples/`

4. **Test with Copilot**
   - Ask Copilot to perform tasks related to your skill
   - Verify it loads and uses the skill correctly

## Skill Comparison

### Agent Skills vs. Custom Instructions

| Feature | Agent Skills | Custom Instructions |
|---------|--------------|---------------------|
| **Purpose** | Specialized task workflows | Coding standards/guidelines |
| **Portability** | Used across all Copilot agents | Limited to specific channels |
| **Content** | Instructions, scripts, resources | Instructions only |
| **Loading** | On-demand, by context | Always applied |
| **Location** | `.github/skills/` | Agent-specific configs |

### Agent Skills vs. MCP Servers

This repository also provides an MCP Server for the same functionality:

| Feature | Agent Skills | MCP Server |
|---------|-------------|------------|
| **Format** | Markdown + Scripts | MCP Protocol |
| **Usage** | Natural language with Copilot | Tool calls via MCP |
| **Platform** | Copilot agents | MCP-compatible clients |
| **Integration** | Automatic, context-aware | Manual configuration |
| **Best For** | General Copilot usage | Structured tool access |

Use **Agent Skills** when working with GitHub Copilot agents.  
Use **MCP Server** when integrating with MCP clients like Claude Desktop.

## Resources

### Official Documentation
- [About Agent Skills - GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Agent Mode 101 - GitHub Blog](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/)

### Community Resources
- [Build Applications with GitHub Copilot Agent Mode](https://github.com/skills/build-applications-w-copilot-agent-mode)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)

### This Repository
- [Main README](../../README.md)
- [Copilot Agent Usage Guide](../../COPILOT_AGENT_USAGE.md)
- [Examples](../../EXAMPLES.md)
- [Quick Start Guide](../../QUICKSTART.md)

## Support

For issues or questions:
1. Check the [COPILOT_AGENT_USAGE.md](../../COPILOT_AGENT_USAGE.md) guide
2. Review the [nano-banana-assets skill documentation](./nano-banana-assets/README.md)
3. Consult [GitHub's Agent Skills documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
4. Open an issue on GitHub

## License

MIT - See the repository LICENSE file for details.
