#!/bin/bash
#
# Test Script for Nano Banana Assets Skill
# This script demonstrates how to use the skill to generate assets locally
#

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "========================================================"
echo "🎨 Nano Banana Assets Skill - Local Test"
echo "========================================================"
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."
echo ""

# 1. Check API key
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo -e "${RED}❌ OPENROUTER_API_KEY not set${NC}"
    echo ""
    echo "To use this skill, you need an OpenRouter API key."
    echo ""
    echo "Steps:"
    echo "  1. Get your API key from: https://openrouter.ai/"
    echo "  2. Set it in your environment:"
    echo "     export OPENROUTER_API_KEY='sk-or-v1-your-key-here'"
    echo ""
    exit 1
else
    echo -e "${GREEN}✅ API key is configured${NC}"
fi

# 2. Check Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo -e "${GREEN}✅ Python 3 found: $(python3 --version)${NC}"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo -e "${GREEN}✅ Python found: $(python --version)${NC}"
else
    echo -e "${RED}❌ Python not found${NC}"
    echo "Please install Python 3.10+ to use this script"
    exit 1
fi

# 3. Check requests library
if ! $PYTHON_CMD -c "import requests" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Python 'requests' library not installed${NC}"
    echo "Installing requests..."
    $PYTHON_CMD -m pip install requests --quiet
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Installed 'requests' library${NC}"
    else
        echo -e "${RED}❌ Failed to install 'requests'${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ Python 'requests' library is installed${NC}"
fi

echo ""
echo "========================================================"
echo "🎯 Running Skill Tests"
echo "========================================================"
echo ""

# Create output directory
OUTPUT_DIR="./generated-assets-test"
mkdir -p "$OUTPUT_DIR"
echo "📁 Output directory: $OUTPUT_DIR"
echo ""

# Test: Generate a simple icon
echo -e "${BLUE}Test: Generate a Modern Home Icon${NC}"
echo "------------------------------------------------------"

cat > /tmp/test_skill_generation.py << 'SCRIPT_EOF'
#!/usr/bin/env python3
import os
import json
import sys
import base64
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests library required")
    sys.exit(1)

API_KEY = os.environ.get("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"

if not API_KEY:
    print("Error: OPENROUTER_API_KEY not set")
    sys.exit(1)

prompt = """Generate a high-quality modern home icon with the following specifications:

Description: A clean, modern home icon for website navigation. Simple geometric house shape with roof and base. Minimalist, professional design suitable for a tech startup.

Aspect Ratio: 1:1
Resolution: 512x512
Color Palette: #667EEA, #764BA2

Requirements:
- Professional, web-ready quality
- Modern and visually appealing
- Optimized for digital use
- Clear at small sizes"""

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
    "X-Title": "Nano Banana Assets Test"
}

payload = {
    "model": MODEL,
    "messages": [{
        "role": "user",
        "content": [{"type": "text", "text": prompt}]
    }],
    "modalities": ["image", "text"],
    "image_config": {"aspect_ratio": "1:1"},
    "temperature": 0.7,
    "max_tokens": 4096
}

print("⏳ Generating asset using nano-banana-assets skill...")
print(f"   Model: {MODEL}")
print(f"   Type: Home Icon")
print(f"   Size: 512x512 (1:1)")
print()

try:
    response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    response.raise_for_status()
    result = response.json()
    
    if "choices" in result and result["choices"]:
        message = result["choices"][0].get("message", {})
        images = message.get("images", [])
        description = message.get("content", "")
        
        if description:
            print("📝 AI Description:")
            print(f"   {description[:300]}...")
            print()
        
        if images:
            print(f"✅ Generated {len(images)} image(s)")
            output_dir = Path("./generated-assets-test")
            output_dir.mkdir(exist_ok=True)
            
            for idx, img in enumerate(images):
                image_url = img.get("image_url", {}).get("url", "")
                if image_url.startswith("data:image"):
                    header, encoded = image_url.split(",", 1)
                    image_data = base64.b64decode(encoded)
                    ext = "png" if "png" in header else "jpg"
                    filename = f"home_icon_{idx + 1}.{ext}"
                    filepath = output_dir / filename
                    
                    with open(filepath, "wb") as f:
                        f.write(image_data)
                    
                    print(f"   ✓ Saved: {filepath}")
                    print(f"   ✓ Size: {len(image_data):,} bytes")
            
            print()
            print("✨ SUCCESS! The nano-banana-assets skill generated the asset successfully.")
        else:
            print("⚠️  No images in response")
            print("Response:", json.dumps(result, indent=2)[:500])
    else:
        print("❌ Unexpected response format")
        
except requests.exceptions.RequestException as e:
    print(f"❌ API Error: {e}")
    if hasattr(e, 'response') and e.response:
        print(f"Status: {e.response.status_code}")
        print(f"Response: {e.response.text[:500]}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
SCRIPT_EOF

$PYTHON_CMD /tmp/test_skill_generation.py
TEST_RESULT=$?
echo ""

# Summary
echo "========================================================"
echo "📊 Test Summary"
echo "========================================================"
echo ""

if [ $TEST_RESULT -eq 0 ]; then
    echo -e "${GREEN}✅ Skill Test - PASSED${NC}"
    echo ""
    echo "🎉 The nano-banana-assets skill is working correctly!"
    echo ""
    echo "📁 Generated files:"
    ls -lh "$OUTPUT_DIR" 2>/dev/null
    echo ""
    echo "Next steps:"
    echo "  • View generated images in: $OUTPUT_DIR"
    echo "  • Try with GitHub Copilot: Just ask for assets naturally!"
    echo "  • Customize prompts for your specific needs"
    echo "  • Check SKILL_USAGE_DEMO.md for more examples"
else
    echo -e "${RED}❌ Skill Test - FAILED${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "  • Verify API key has credits: https://openrouter.ai/activity"
    echo "  • Check internet connectivity"
    echo "  • Review error messages above"
    echo "  • Make sure you're in an environment with internet access"
fi

echo ""
echo "========================================================"
