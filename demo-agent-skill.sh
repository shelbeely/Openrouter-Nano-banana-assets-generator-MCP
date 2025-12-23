#!/bin/bash

# Demonstration script for using the nano-banana-assets skill
# This shows how a GitHub Copilot agent can utilize the skill

set -e

echo "=================================================="
echo "Nano Banana Assets Skill - Agent Usage Demo"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."
echo ""

# Check if API key is set
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo -e "${RED}❌ OPENROUTER_API_KEY not set${NC}"
    echo ""
    echo "To use this demo, set your OpenRouter API key:"
    echo "  export OPENROUTER_API_KEY='sk-or-v1-your-key-here'"
    echo ""
    echo "Get your API key from: https://openrouter.ai/"
    exit 1
else
    echo -e "${GREEN}✅ API key is set${NC}"
fi

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo -e "${GREEN}✅ Python 3 found: $(python3 --version)${NC}"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo -e "${GREEN}✅ Python found: $(python --version)${NC}"
else
    echo -e "${RED}❌ Python not found${NC}"
    exit 1
fi

# Check if requests library is installed
if $PYTHON_CMD -c "import requests" 2>/dev/null; then
    echo -e "${GREEN}✅ Python 'requests' library is installed${NC}"
else
    echo -e "${YELLOW}⚠️  Python 'requests' library not found${NC}"
    echo "Installing requests..."
    pip install requests --quiet
    echo -e "${GREEN}✅ Installed 'requests' library${NC}"
fi

echo ""
echo "=================================================="
echo "Demo: How Agents Use This Skill"
echo "=================================================="
echo ""

# Create a demo directory
DEMO_DIR="agent-skill-demo"
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

echo -e "${YELLOW}📖 Step 1: Agent reads the SKILL.md file${NC}"
echo ""
echo "As an AI agent, I first read the SKILL.md file to understand:"
echo "  - What capabilities are available"
echo "  - How to structure API calls"
echo "  - What parameters are supported"
echo "  - Best practices for prompts"
echo ""
echo "The skill teaches me to generate assets using OpenRouter's API."
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}🎯 Step 2: User makes a request${NC}"
echo ""
echo "Example user request:"
echo "  'Generate a modern home icon for my website'"
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}🧠 Step 3: Agent analyzes the request${NC}"
echo ""
echo "I identify this as a 'Generate Single Asset' operation."
echo ""
echo "Requirements extracted:"
echo "  - Asset type: icon"
echo "  - Style: modern"
echo "  - Use case: website navigation"
echo "  - Aspect ratio: 1:1 (square - best for icons)"
echo "  - Resolution: 512x512 (appropriate for icons)"
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}✍️  Step 4: Agent builds a detailed prompt${NC}"
echo ""
cat > prompt.txt << 'EOF'
Generate a high-quality icon with the following specifications:

Description: Modern, minimalist home icon for website navigation. 
Simple house silhouette with clean lines, professional appearance. 
Suitable for use in a navigation bar. Monochrome design on transparent background.

Aspect Ratio: 1:1
Resolution: 512x512

Requirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance
- Simple and recognizable at small sizes
EOF

echo "Prompt created:"
cat prompt.txt
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}🚀 Step 5: Agent uses the skill's helper script${NC}"
echo ""
echo "I can use the Python script provided in the skill:"
echo ""
echo "Command:"
echo "  python ../nano-banana-assets-skill/scripts/generate_asset.py \\"
echo "    'Modern minimalist home icon for website navigation' \\"
echo "    '1:1' \\"
echo "    '512x512'"
echo ""

# Show what would happen (dry run explanation)
echo "This would:"
echo "  1. Load the OPENROUTER_API_KEY from environment"
echo "  2. Build a proper API request to OpenRouter"
echo "  3. Send the request to google/gemini-3-pro-image-preview"
echo "  4. Receive the generated image as base64 data"
echo "  5. Save the image to a PNG file"
echo ""

echo -e "${YELLOW}Note: This is a demonstration. We're not making an actual API call${NC}"
echo -e "${YELLOW}to avoid consuming credits. But the process would work as shown.${NC}"
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}📦 Step 6: Understanding the response${NC}"
echo ""
echo "The API returns JSON with this structure:"
echo ""
cat > example_response.json << 'EOF'
{
  "choices": [{
    "message": {
      "content": "I've generated a modern home icon with clean lines...",
      "images": [{
        "image_url": {
          "url": "data:image/png;base64,iVBORw0KGgoAAAANS..."
        }
      }]
    }
  }]
}
EOF
cat example_response.json
echo ""
echo "The agent extracts:"
echo "  - Description from 'content'"
echo "  - Image data from 'images[].image_url.url'"
echo ""
read -p "Press Enter to continue..."
echo ""

echo -e "${YELLOW}💾 Step 7: Agent processes and saves the result${NC}"
echo ""
echo "The agent would:"
echo "  1. Decode the base64 image data"
echo "  2. Save to project directory (e.g., assets/home-icon.png)"
echo "  3. Present the result to the user"
echo "  4. Optionally update HTML/CSS to use the new icon"
echo ""
read -p "Press Enter to continue..."
echo ""

echo "=================================================="
echo "Additional Examples"
echo "=================================================="
echo ""

echo -e "${GREEN}Example 1: Generate a hero banner${NC}"
echo ""
echo "User: 'Create a hero banner for my tech startup'"
echo ""
echo "Agent action:"
echo "  python generate_asset.py \\"
echo "    'Modern tech startup hero banner with gradient' \\"
echo "    '16:9' \\"
echo "    '1920x1080'"
echo ""

echo -e "${GREEN}Example 2: Generate social media assets${NC}"
echo ""
echo "User: 'I need Instagram and Facebook cover images'"
echo ""
echo "Agent action (using Python API):"
cat > example2.py << 'EOF'
from nano-banana-assets-skill.scripts.generate_asset import AssetGenerator

generator = AssetGenerator()
response = generator.generate_asset_pack(
    description="Social media kit for tech startup",
    asset_types=["instagram-post", "facebook-cover"],
    brand_guidelines="Modern, professional, innovative",
    color_palette=["#667EEA", "#764BA2"]
)
generator.save_images_from_response(response, "social-media")
EOF
echo ""
cat example2.py
echo ""

echo -e "${GREEN}Example 3: Edit an existing image${NC}"
echo ""
echo "User: 'Make this banner warmer and brighter'"
echo ""
echo "Agent action:"
cat > example3.py << 'EOF'
from nano-banana-assets-skill.scripts.generate_asset import AssetGenerator

generator = AssetGenerator()
response = generator.edit_asset(
    source_image="path/to/banner.png",
    edit_instructions="Adjust to warmer tones, increase brightness",
    preserve_elements=["logo", "text"]
)
generator.save_images_from_response(response, "edited-banner")
EOF
echo ""
cat example3.py
echo ""

echo "=================================================="
echo "Key Takeaways for Agents"
echo "=================================================="
echo ""
echo "✅ Read SKILL.md to understand all capabilities"
echo "✅ Use the provided Python/Bash scripts for easy integration"
echo "✅ Build detailed, specific prompts for best results"
echo "✅ Specify appropriate aspect ratios and resolutions"
echo "✅ Handle API responses properly (parse JSON, save images)"
echo "✅ Provide helpful feedback to users"
echo ""

echo "=================================================="
echo "How to Actually Use the Skill"
echo "=================================================="
echo ""
echo "1. Set your API key:"
echo "   export OPENROUTER_API_KEY='sk-or-v1-your-key'"
echo ""
echo "2. Navigate to scripts directory:"
echo "   cd nano-banana-assets-skill/scripts"
echo ""
echo "3. Generate an asset:"
echo "   python generate_asset.py 'Your prompt' '16:9' '1920x1080'"
echo ""
echo "4. Find your generated image:"
echo "   ls -la asset_*.png"
echo ""

echo "=================================================="
echo "Resources"
echo "=================================================="
echo ""
echo "📄 SKILL.md - Complete skill instructions"
echo "📄 COPILOT_AGENT_USAGE.md - This guide in detail"
echo "📄 references/api-reference.md - API documentation"
echo "📄 references/prompt-templates.md - Prompt examples"
echo "🌐 https://openrouter.ai/docs - OpenRouter API docs"
echo ""

# Cleanup
cd ..
echo "Demo complete! Cleaning up demo directory..."
rm -rf "$DEMO_DIR"

echo ""
echo -e "${GREEN}✅ Demo completed successfully!${NC}"
echo ""
echo "The nano-banana-assets skill is ready to use."
echo "Read COPILOT_AGENT_USAGE.md for complete documentation."
