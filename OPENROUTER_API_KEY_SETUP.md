# OpenRouter API Key Setup Guide

This guide shows you how to configure your OpenRouter API key so the nano-banana-assets skill can access it.

## Quick Setup

The skill requires the `OPENROUTER_API_KEY` environment variable to be set.

### Get Your API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to **Keys** section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

## Setup Methods

Choose the method that works best for your environment:

### Method 1: Set in Your Shell Profile (Recommended)

This makes the key available in all terminal sessions:

#### For Linux/macOS (Bash)

```bash
# Add to ~/.bashrc or ~/.bash_profile
echo 'export OPENROUTER_API_KEY="sk-or-v1-your-key-here"' >> ~/.bashrc

# Reload your profile
source ~/.bashrc
```

#### For Linux/macOS (Zsh)

```bash
# Add to ~/.zshrc
echo 'export OPENROUTER_API_KEY="sk-or-v1-your-key-here"' >> ~/.zshrc

# Reload your profile
source ~/.zshrc
```

#### For Windows (PowerShell)

```powershell
# Set user environment variable
[System.Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', 'sk-or-v1-your-key-here', 'User')

# Restart PowerShell for changes to take effect
```

#### For Windows (Command Prompt)

```cmd
# Set user environment variable
setx OPENROUTER_API_KEY "sk-or-v1-your-key-here"

# Restart Command Prompt for changes to take effect
```

### Method 2: Set for Current Session Only

If you only need it temporarily:

```bash
# Linux/macOS/Git Bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Windows PowerShell
$env:OPENROUTER_API_KEY = "sk-or-v1-your-key-here"

# Windows Command Prompt
set OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### Method 3: Use a .env File (For Local Development)

Create a `.env` file in the repository root:

```bash
# Create .env file
cat > .env << 'EOF'
OPENROUTER_API_KEY=sk-or-v1-your-key-here
EOF
```

**Important:** The `.env` file is already in `.gitignore` so it won't be committed to git.

To load it in your current session:

```bash
# Linux/macOS/Git Bash
export $(cat .env | xargs)

# Or use source
source .env
```

### Method 4: VS Code Configuration

If you're using VS Code with GitHub Copilot, add to your workspace settings:

**File: `.vscode/settings.json`**

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

**Important:** Add `.vscode/settings.json` to `.gitignore` if it contains secrets!

### Method 5: Pass Directly When Running Scripts

You can pass the key when running the helper scripts:

```bash
# Python script
OPENROUTER_API_KEY="sk-or-v1-your-key" python .github/skills/nano-banana-assets/scripts/generate_asset.py "prompt"

# Bash script
OPENROUTER_API_KEY="sk-or-v1-your-key" .github/skills/nano-banana-assets/scripts/generate_asset.sh "prompt"
```

## Verify Setup

After setting your API key, verify it's accessible:

### Check the Variable

```bash
# Linux/macOS/Git Bash
echo $OPENROUTER_API_KEY

# Windows PowerShell
echo $env:OPENROUTER_API_KEY

# Windows Command Prompt
echo %OPENROUTER_API_KEY%
```

You should see your API key (starting with `sk-or-v1-`).

### Test with Python Script

```bash
cd .github/skills/nano-banana-assets/scripts

# Run test generation
python generate_asset.py "Test icon" "1:1" "512x512"
```

If successful, you'll see:
- "Generating asset..." message
- Response saved to `response.json`
- Image(s) saved as `asset_*.png`

### Test with Bash Script

```bash
cd .github/skills/nano-banana-assets/scripts

# Run test generation
./generate_asset.sh "Test icon" "1:1" "512x512"
```

## How GitHub Copilot Accesses the Key

When GitHub Copilot agents use this skill:

1. **Copilot reads SKILL.md** which instructs it to use `OPENROUTER_API_KEY`
2. **Agent runs scripts** that automatically read the environment variable
3. **Scripts make API calls** with the key as a Bearer token

The Python script checks for the key like this:

```python
import os

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment")
```

The Bash script checks like this:

```bash
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "Error: OPENROUTER_API_KEY environment variable is not set"
    exit 1
fi
```

## Troubleshooting

### Error: "OPENROUTER_API_KEY not found"

**Cause:** Environment variable not set or not accessible.

**Solutions:**
1. Check if variable is set: `echo $OPENROUTER_API_KEY`
2. If empty, set it using one of the methods above
3. Restart your terminal/IDE after setting
4. Make sure there are no typos in the variable name

### Error: "401 Unauthorized"

**Cause:** Invalid API key.

**Solutions:**
1. Verify your key at [OpenRouter Dashboard](https://openrouter.ai/dashboard)
2. Check for extra spaces or quotes in the key
3. Regenerate the API key if needed
4. Ensure the key starts with `sk-or-v1-`

### Error: "402 Payment Required"

**Cause:** Insufficient credits in your OpenRouter account.

**Solutions:**
1. Check your balance at [OpenRouter Dashboard](https://openrouter.ai/dashboard)
2. Add credits to your account
3. Review your usage limits

### Variable Set But Scripts Can't Find It

**For VS Code:**
- Restart VS Code completely after setting the variable
- Check if the terminal inherits environment variables
- Use the VS Code settings method (Method 4)

**For Shell:**
- Make sure you sourced your profile: `source ~/.bashrc`
- Check the variable in the same terminal you're running scripts
- Try setting it in the current session as a test

### Using in GitHub Actions

If running in CI/CD:

```yaml
name: Generate Assets
on: [push]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate Asset
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        run: |
          cd .github/skills/nano-banana-assets/scripts
          python generate_asset.py "Hero banner" "16:9" "1920x1080"
```

Don't forget to add `OPENROUTER_API_KEY` to your repository secrets!

## Security Best Practices

### ✅ DO:
- Use environment variables for API keys
- Add `.env` files to `.gitignore`
- Add settings files with secrets to `.gitignore`
- Use repository secrets for CI/CD
- Rotate keys periodically
- Monitor usage at OpenRouter dashboard

### ❌ DON'T:
- Commit API keys to git
- Share keys in code or documentation
- Use production keys for testing
- Store keys in plaintext files tracked by git
- Include keys in screenshots or logs

## Quick Reference

### Check if key is set:
```bash
echo $OPENROUTER_API_KEY
```

### Set for current session:
```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

### Set permanently (Linux/macOS):
```bash
echo 'export OPENROUTER_API_KEY="sk-or-v1-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Test the skill:
```bash
cd .github/skills/nano-banana-assets/scripts
python generate_asset.py "Test" "1:1" "512x512"
```

### Get help:
- OpenRouter Docs: https://openrouter.ai/docs
- OpenRouter Dashboard: https://openrouter.ai/dashboard
- This Repository: [COPILOT_AGENT_USAGE.md](../COPILOT_AGENT_USAGE.md)

## Summary

The nano-banana-assets skill needs access to your OpenRouter API key via the `OPENROUTER_API_KEY` environment variable. Set it using any of the methods above, verify it's accessible, and you're ready to generate assets with GitHub Copilot!

**Recommended Setup:**
1. Get your API key from OpenRouter
2. Add to your shell profile (`~/.bashrc` or `~/.zshrc`)
3. Reload your profile or restart terminal
4. Verify with `echo $OPENROUTER_API_KEY`
5. Test with the Python script

That's it! The skill will automatically use the key when generating assets.
