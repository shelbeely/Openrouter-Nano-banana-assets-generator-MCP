#!/bin/bash

# Helper script to generate a single asset using OpenRouter API
# Usage: ./generate_asset.sh "prompt" "aspect_ratio" "resolution"

OPENROUTER_API_KEY="${OPENROUTER_API_KEY}"
OPENROUTER_URL="https://openrouter.ai/api/v1/chat/completions"
MODEL="google/gemini-3-pro-image-preview"

if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "Error: OPENROUTER_API_KEY environment variable is not set"
    exit 1
fi

PROMPT="${1:-Generate a professional web asset}"
ASPECT_RATIO="${2:-1:1}"
RESOLUTION="${3:-1080x1080}"

# Build the full prompt
FULL_PROMPT="Generate a high-quality web asset with the following specifications:

Description: ${PROMPT}
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
          "text": "${FULL_PROMPT}"
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
echo "To extract images from response.json:"
echo "  jq -r '.choices[0].message.images[0].image_url.url' response.json > image1.txt"
echo ""
echo "Text description:"
echo "$RESPONSE" | jq -r '.choices[0].message.content'
