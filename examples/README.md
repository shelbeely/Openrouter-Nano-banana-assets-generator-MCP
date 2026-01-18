# Nano Banana Assets Skill - Examples

This directory contains examples and test scripts demonstrating how to use the nano-banana-assets skill.

## Files

### `test-skill-locally.sh`

A comprehensive test script that demonstrates the skill's capability to generate assets using the OpenRouter API.

**Usage:**
```bash
# Set your API key
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Run the test
./examples/test-skill-locally.sh
```

**What it does:**
- Checks prerequisites (API key, Python, requests library)
- Generates a test asset (home icon)
- Saves the output to `./generated-assets-test/`
- Reports success/failure

**Requirements:**
- OpenRouter API key (from https://openrouter.ai/)
- Python 3.x
- `requests` library (auto-installed if missing)
- Internet access to OpenRouter API

## Expected Output

When successful, the test will:

1. **Verify Prerequisites**
   - ✅ API key is configured
   - ✅ Python 3 found
   - ✅ requests library installed

2. **Generate Asset**
   - ⏳ Generating asset using nano-banana-assets skill...
   - 📝 AI Description of the generated asset
   - ✅ Generated 1 image(s)
   - ✓ Saved to file

3. **Summary**
   - ✅ Skill Test - PASSED
   - 📁 Shows generated files

## Example Assets

The test generates professional-quality assets such as:

- **Home Icon** (512x512, 1:1) - Modern, minimalist home icon for navigation
- Uses brand colors (#667EEA, #764BA2)
- Web-ready PNG format
- Base64-encoded or saved to file

## Using the Skill with GitHub Copilot

When using GitHub Copilot coding agent, you can simply ask for assets in natural language:

### Example 1: Simple Icon
```
You: "Generate a modern home icon for my website"

Copilot: *loads nano-banana-assets skill*
Copilot: *generates and saves icon*
Copilot: "I've created a modern home icon. It's saved as home_icon.png"
```

### Example 2: Hero Banner
```
You: "Create a hero banner with blue and purple gradient, 16:9"

Copilot: *uses the skill*
Copilot: "I've generated a hero banner with your specified gradient and dimensions"
```

### Example 3: Social Media Kit
```
You: "I need Instagram post, story, and Facebook cover for my brand"

Copilot: *generates asset pack*
Copilot: "I've created your social media kit with 3 assets maintaining consistent branding"
```

## Troubleshooting

### Network Access Required

⚠️ **Important**: The skill requires internet access to call the OpenRouter API at `https://openrouter.ai/api/v1/chat/completions`

If you're in a sandboxed or restricted environment (like GitHub Actions runners without network access), the skill won't be able to make API calls. In such cases:

- **For local testing**: Use the test script with proper internet connection
- **For GitHub Copilot**: The skill works when Copilot has network access
- **For CI/CD**: Consider using pre-generated assets or run tests in environments with API access

### Common Issues

1. **"OPENROUTER_API_KEY not set"**
   - Solution: Export your API key before running tests
   ```bash
   export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
   ```

2. **"Could not resolve host: openrouter.ai"**
   - Solution: Check internet connectivity
   - Verify DNS resolution works
   - Ensure firewall allows HTTPS to openrouter.ai

3. **"403 Forbidden" or "401 Unauthorized"**
   - Solution: Verify your API key is correct
   - Check that your API key has credits at https://openrouter.ai/activity

4. **"429 Rate Limit Exceeded"**
   - Solution: Wait a few moments and retry
   - Check your API usage limits

## More Examples

For more detailed examples and use cases, see:

- `../SKILL_USAGE_DEMO.md` - Comprehensive usage guide
- `../.github/skills/nano-banana-assets/references/prompt-templates.md` - Prompt examples
- `../.github/skills/nano-banana-assets/README.md` - Full skill documentation
- `../EXAMPLES.md` - General usage examples

## Cost Considerations

Each API call to OpenRouter consumes credits. The cost depends on:

- Resolution (higher = more expensive)
- Number of assets generated
- Model complexity

Monitor your usage at: https://openrouter.ai/activity

**Tips to manage costs:**
- Use appropriate resolutions (don't request 4K for thumbnails)
- Cache generated assets
- Batch similar requests
- Test with lower resolutions first

## API Model Information

The skill uses:
- **Model**: `google/gemini-3-pro-image-preview` (Nano Banana Pro)
- **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Modalities**: `["image", "text"]` for image generation
- **Output**: Base64-encoded PNG/JPEG images

## License

MIT - See LICENSE file in the repository root
