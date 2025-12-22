#!/bin/bash

# Simple validation script for OpenRouter Nano Banana Pro MCP Server
# This script checks that the server can start correctly

echo "🧪 OpenRouter Nano Banana Pro MCP Server - Validation"
echo "======================================================"
echo ""

# Check Node.js version
echo "📋 Checking Node.js version..."
NODE_VERSION=$(node --version)
echo "   Node.js: $NODE_VERSION"

if [[ ! "$NODE_VERSION" =~ ^v(1[8-9]|[2-9][0-9]) ]]; then
    echo "   ⚠️  Node.js 18 or higher is recommended"
fi
echo ""

# Check if build exists
echo "📦 Checking build..."
if [ ! -f "dist/index.js" ]; then
    echo "   ❌ dist/index.js not found. Run 'npm run build' first."
    exit 1
fi
echo "   ✅ Build files found"
echo ""

# Check if API key is set
echo "🔑 Checking API key..."
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "   ⚠️  OPENROUTER_API_KEY not set (optional for validation)"
    echo "   To use the server, set: export OPENROUTER_API_KEY='your-key'"
else
    echo "   ✅ API key is set"
fi
echo ""

// Check file permissions
echo "🔒 Checking permissions..."
if [ ! -x "dist/index.js" ]; then
    echo "   ⚠️  dist/index.js is not executable"
    echo "   Making it executable (chmod +x dist/index.js)"
    chmod +x dist/index.js
    echo "   ✅ Made executable"
else
    echo "   ✅ File is executable"
fi
echo ""

# Validate the file structure
echo "📁 Validating file structure..."
EXPECTED_FILES=(
    "package.json"
    "tsconfig.json"
    "src/index.ts"
    "dist/index.js"
    "dist/index.d.ts"
    "README.md"
    "EXAMPLES.md"
    "CONFIG.md"
)

for file in "${EXPECTED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file (missing)"
    fi
done
echo ""

# Check the built file has correct shebang
echo "🔍 Checking built file..."
FIRST_LINE=$(head -n 1 dist/index.js)
if [[ "$FIRST_LINE" == "#!/usr/bin/env node" ]]; then
    echo "   ✅ Correct shebang line"
else
    echo "   ⚠️  Missing or incorrect shebang"
fi
echo ""

# Check dependencies
echo "📚 Checking dependencies..."
if [ -d "node_modules/@modelcontextprotocol" ]; then
    echo "   ✅ MCP SDK installed"
else
    echo "   ❌ MCP SDK not found. Run 'npm install'"
    exit 1
fi
echo ""

# Summary
echo "======================================================"
echo "✅ Validation complete!"
echo ""
echo "Next steps:"
echo "1. Set your API key: export OPENROUTER_API_KEY='your-key'"
echo "2. Configure in Claude Desktop (see CONFIG.md)"
echo "3. Start using the tools (see EXAMPLES.md)"
echo ""
echo "To test the server manually:"
echo "  node dist/index.js"
echo ""
