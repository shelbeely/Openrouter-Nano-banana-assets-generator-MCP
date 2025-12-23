#!/bin/bash

# Setup script for nano-banana-assets skill
# This helps you configure the OPENROUTER_API_KEY environment variable

set -e

echo "=================================================="
echo "Nano Banana Assets Skill - Setup"
echo "=================================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}This script will help you set up your OpenRouter API key.${NC}"
echo ""

# Check if key is already set
if [ -n "$OPENROUTER_API_KEY" ]; then
    echo -e "${GREEN}✅ OPENROUTER_API_KEY is already set!${NC}"
    echo ""
    echo "Current key (first 20 characters): ${OPENROUTER_API_KEY:0:20}..."
    echo ""
    read -p "Do you want to update it? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Keeping existing key. Setup complete!"
        exit 0
    fi
fi

# Get API key from user
echo -e "${YELLOW}Step 1: Get your OpenRouter API key${NC}"
echo ""
echo "1. Visit: https://openrouter.ai/"
echo "2. Sign up or log in"
echo "3. Go to the 'Keys' section"
echo "4. Create a new API key"
echo "5. Copy the key (starts with 'sk-or-v1-')"
echo ""

read -p "Enter your OpenRouter API key: " api_key

# Validate key format
if [[ ! $api_key =~ ^sk-or-v1- ]]; then
    echo -e "${RED}❌ Invalid key format. Key should start with 'sk-or-v1-'${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}Step 2: Choose how to save your key${NC}"
echo ""
echo "1. Add to shell profile (recommended - persistent)"
echo "2. Set for current session only (temporary)"
echo "3. Create .env file in this repository (local development)"
echo ""
read -p "Choose option (1-3): " -n 1 -r option
echo ""
echo ""

case $option in
    1)
        echo -e "${YELLOW}Adding to shell profile...${NC}"
        echo ""
        
        # Detect shell
        if [ -n "$ZSH_VERSION" ]; then
            PROFILE="$HOME/.zshrc"
            SHELL_NAME="Zsh"
        elif [ -n "$BASH_VERSION" ]; then
            if [ -f "$HOME/.bashrc" ]; then
                PROFILE="$HOME/.bashrc"
            else
                PROFILE="$HOME/.bash_profile"
            fi
            SHELL_NAME="Bash"
        else
            echo -e "${YELLOW}⚠️  Could not detect shell type${NC}"
            PROFILE="$HOME/.profile"
            SHELL_NAME="default"
        fi
        
        echo "Detected shell: $SHELL_NAME"
        echo "Profile file: $PROFILE"
        echo ""
        
        # Check if already in profile
        if grep -q "OPENROUTER_API_KEY" "$PROFILE" 2>/dev/null; then
            echo -e "${YELLOW}⚠️  OPENROUTER_API_KEY already exists in $PROFILE${NC}"
            read -p "Replace it? (y/N): " -n 1 -r
            echo ""
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                # Remove old line
                sed -i.bak '/OPENROUTER_API_KEY/d' "$PROFILE"
                echo "Removed old key"
            else
                echo "Keeping existing key in profile"
                exit 0
            fi
        fi
        
        # Add to profile
        echo "" >> "$PROFILE"
        echo "# OpenRouter API Key for nano-banana-assets skill" >> "$PROFILE"
        echo "export OPENROUTER_API_KEY=\"$api_key\"" >> "$PROFILE"
        
        echo -e "${GREEN}✅ Added to $PROFILE${NC}"
        echo ""
        echo "To activate now, run:"
        echo -e "${BLUE}  source $PROFILE${NC}"
        echo ""
        echo "Or restart your terminal."
        
        # Apply for current session
        export OPENROUTER_API_KEY="$api_key"
        ;;
        
    2)
        echo -e "${YELLOW}Setting for current session...${NC}"
        export OPENROUTER_API_KEY="$api_key"
        echo -e "${GREEN}✅ Set for current session${NC}"
        echo ""
        echo -e "${YELLOW}⚠️  This will only work in this terminal session.${NC}"
        echo "The key will be lost when you close the terminal."
        echo ""
        echo "To make it permanent, run this script again and choose option 1."
        ;;
        
    3)
        echo -e "${YELLOW}Creating .env file...${NC}"
        
        if [ -f ".env" ]; then
            echo -e "${YELLOW}⚠️  .env file already exists${NC}"
            read -p "Overwrite it? (y/N): " -n 1 -r
            echo ""
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                echo "Keeping existing .env file"
                exit 0
            fi
        fi
        
        cat > .env << EOF
# OpenRouter API Key
# Get your key from: https://openrouter.ai/
OPENROUTER_API_KEY=$api_key

# Optional: Environment (development/production)
NODE_ENV=development
EOF
        
        echo -e "${GREEN}✅ Created .env file${NC}"
        echo ""
        echo "To use it, load it in your terminal:"
        echo -e "${BLUE}  export \$(cat .env | xargs)${NC}"
        echo ""
        echo -e "${YELLOW}⚠️  The .env file is in .gitignore and won't be committed to git.${NC}"
        
        # Apply for current session
        export OPENROUTER_API_KEY="$api_key"
        ;;
        
    *)
        echo -e "${RED}❌ Invalid option${NC}"
        exit 1
        ;;
esac

echo ""
echo "=================================================="
echo "Verification"
echo "=================================================="
echo ""

# Verify it's set
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo -e "${RED}❌ Failed to set OPENROUTER_API_KEY${NC}"
    exit 1
fi

echo -e "${GREEN}✅ OPENROUTER_API_KEY is set${NC}"
echo ""
echo "Key (first 20 characters): ${OPENROUTER_API_KEY:0:20}..."
echo ""

# Test if Python is available
if command -v python3 &> /dev/null || command -v python &> /dev/null; then
    echo -e "${YELLOW}Would you like to test the skill now? (y/N):${NC} "
    read -n 1 -r test_now
    echo ""
    
    if [[ $test_now =~ ^[Yy]$ ]]; then
        echo ""
        echo "Testing skill with a simple asset generation..."
        echo ""
        
        # Check if requests is installed
        PYTHON_CMD=$(command -v python3 || command -v python)
        if ! $PYTHON_CMD -c "import requests" 2>/dev/null; then
            echo "Installing Python requests library..."
            pip install requests --quiet
        fi
        
        # Run test
        cd .github/skills/nano-banana-assets/scripts
        $PYTHON_CMD generate_asset.py "Simple test icon" "1:1" "512x512"
        
        echo ""
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Test successful! Skill is working.${NC}"
            echo ""
            echo "Generated files:"
            ls -lh asset_*.png response.json 2>/dev/null || echo "  (check the scripts directory)"
        else
            echo -e "${RED}❌ Test failed. Check the error message above.${NC}"
            echo ""
            echo "Common issues:"
            echo "- API key may be invalid"
            echo "- No credits in OpenRouter account"
            echo "- Network connectivity issues"
        fi
        cd - > /dev/null
    fi
fi

echo ""
echo "=================================================="
echo "Setup Complete!"
echo "=================================================="
echo ""
echo -e "${GREEN}Your nano-banana-assets skill is ready to use!${NC}"
echo ""
echo "Next steps:"
echo "1. Start using GitHub Copilot in VS Code or CLI"
echo "2. Ask for asset generation tasks naturally"
echo "3. Copilot will automatically use this skill"
echo ""
echo "Examples:"
echo '  "Generate a modern home icon for my website"'
echo '  "Create a hero banner with blue and purple gradient"'
echo '  "I need a social media kit for my brand"'
echo ""
echo "Documentation:"
echo "  - OPENROUTER_API_KEY_SETUP.md - Detailed setup guide"
echo "  - COPILOT_AGENT_USAGE.md - How to use the skill"
echo "  - .github/skills/README.md - Agent skills overview"
echo ""
echo -e "${BLUE}Happy asset generating! 🎨${NC}"
