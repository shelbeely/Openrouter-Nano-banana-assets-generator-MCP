#!/bin/bash

# Helper script to generate a single asset using OpenRouter API
# Usage: ./generate_asset.sh "prompt" "aspect_ratio" "resolution" [--transparent]

OPENROUTER_API_KEY="${OPENROUTER_API_KEY}"
OPENROUTER_URL="https://openrouter.ai/api/v1/chat/completions"
MODEL="google/gemini-3-pro-image-preview"
CHROMA_KEY="#00FF00"

if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "Error: OPENROUTER_API_KEY environment variable is not set"
    exit 1
fi

# Parse arguments
PROMPT=""
ASPECT_RATIO="1:1"
RESOLUTION="1080x1080"
TRANSPARENT=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --transparent|-t)
            TRANSPARENT=true
            shift
            ;;
        *)
            if [ -z "$PROMPT" ]; then
                PROMPT="$1"
            elif [ "$ASPECT_RATIO" = "1:1" ]; then
                ASPECT_RATIO="$1"
            elif [ "$RESOLUTION" = "1080x1080" ]; then
                RESOLUTION="$1"
            fi
            shift
            ;;
    esac
done

# Set default prompt if not provided
if [ -z "$PROMPT" ]; then
    PROMPT="Generate a professional web asset"
fi

# Build the full prompt with or without chroma key
if [ "$TRANSPARENT" = true ]; then
    BACKGROUND_INSTRUCTION="Location: Isolated on solid bright green ($CHROMA_KEY) chroma key background, no environmental context

IMPORTANT: The background MUST be solid bright green ($CHROMA_KEY) only.
This is a chroma key background for automated removal - DO NOT paint checkered patterns.
"
    echo "🎨 Generating with chroma key background for transparency"
else
    BACKGROUND_INSTRUCTION="Background: Professional web background"
fi

FULL_PROMPT="Generate a high-quality web asset with the following specifications:

Description: ${PROMPT}

${BACKGROUND_INSTRUCTION}
Aspect Ratio: ${ASPECT_RATIO}
Resolution: ${RESOLUTION}

Requirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance"

# Build JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "model": "${MODEL}",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": ${FULL_PROMPT@Q}
        }
      ]
    }
  ],
  "modalities": ["image", "text"],
  "image_config": {
    "aspect_ratio": "${ASPECT_RATIO}"
  },
  "temperature": 0.7,
  "max_tokens": 4096
}
EOF
)

# Make API call
echo "Generating asset..."
echo "Prompt: ${PROMPT}"
echo "Aspect Ratio: ${ASPECT_RATIO}"
echo "Resolution: ${RESOLUTION}"
if [ "$TRANSPARENT" = true ]; then
    echo "Background: Chroma Key ($CHROMA_KEY)"
fi
echo ""

RESPONSE=$(curl -s -X POST "${OPENROUTER_URL}" \
  -H "Authorization: Bearer ${OPENROUTER_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "HTTP-Referer: https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP" \
  -H "X-Title: Nano Banana Assets Generator" \
  -d "${JSON_PAYLOAD}")

# Check for errors
if echo "$RESPONSE" | grep -q "error"; then
    echo "Error from API:"
    echo "$RESPONSE" | jq '.error'
    exit 1
fi

# Extract and save images
echo "Response received. Extracting images..."
echo "$RESPONSE" > response.json

# Count images
IMAGE_COUNT=$(echo "$RESPONSE" | jq '.choices[0].message.images | length')

if [ "$IMAGE_COUNT" = "null" ] || [ "$IMAGE_COUNT" = "0" ]; then
    echo "No images generated"
    echo "Response content:"
    echo "$RESPONSE" | jq '.choices[0].message.content'
    exit 1
fi

echo "Generated ${IMAGE_COUNT} image(s)"
echo ""
echo "Full response saved to response.json"
echo ""

if [ "$TRANSPARENT" = true ]; then
    echo "💡 To remove background and create transparent PNG:"
    echo "   python remove_backgrounds.py response_image.png"
    echo "   or"
    echo "   python remove_backgrounds.py --chroma-key '$CHROMA_KEY' response_image.png"
    echo ""
fi

echo "To extract images from response.json:"
echo "  jq -r '.choices[0].message.images[0].image_url.url' response.json | sed 's/data:image\/png;base64,//' | base64 -d > image1.png"
echo ""
echo "Text description:"
echo "$RESPONSE" | jq -r '.choices[0].message.content'
