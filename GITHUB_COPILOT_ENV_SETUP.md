# Setting Environment Variables for GitHub Copilot Coding Agent

This guide explains how to configure the `OPENROUTER_API_KEY` environment variable so GitHub Copilot coding agent can use the nano-banana-assets skill.

## Overview

GitHub Copilot coding agent can access environment variables through the **copilot environment** in your repository settings. To provide your OpenRouter API key securely:

1. Create a secret in the **copilot environment**
2. GitHub Copilot automatically loads it when working in your repository
3. The skill scripts can access the environment variable

## Step-by-Step Setup

### 1. Get Your OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to **Keys** section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

### 2. Add API Key to Copilot Environment

#### On GitHub.com

1. Navigate to the main page of your repository on GitHub
2. Click **Settings** (top menu bar)
   - If you cannot see the "Settings" tab, select the dropdown menu, then click Settings
3. In the left sidebar, click **Environments**
4. Click the **copilot** environment
   - If it doesn't exist, create it by clicking **New environment** and name it `copilot`
5. Under "Environment secrets," click **Add environment secret**
6. Set:
   - **Name:** `OPENROUTER_API_KEY`
   - **Secret:** Your OpenRouter API key (paste the full key starting with `sk-or-v1-`)
7. Click **Add secret**

**Alternative: Use Environment Variable Instead of Secret**

If your API key is not sensitive (e.g., for testing), you can add it as a variable:
1. Under "Environment variables," click **Add environment variable**
2. Set:
   - **Name:** `OPENROUTER_API_KEY`
   - **Value:** Your OpenRouter API key
3. Click **Add variable**

**Note:** For production use, always use **Environment secrets** for API keys.

### 3. Use with GitHub Copilot

Now when you use GitHub Copilot coding agent:

1. Open your repository or work on a PR
2. Ask Copilot for asset generation:
   ```
   "Generate a modern icon for my website"
   "Create a hero banner with gradient background"
   ```
3. Copilot automatically:
   - Loads the OPENROUTER_API_KEY from the copilot environment
   - Uses the nano-banana-assets skill
   - Generates the assets!

## How It Works

### The Copilot Environment

When you set a secret or variable in the **copilot environment**:

1. **GitHub Copilot accesses the environment** - When Copilot coding agent starts working in your repository
2. **Environment variables are loaded** - `OPENROUTER_API_KEY` is available in the execution environment
3. **Skill scripts access it** - Python/Bash scripts read it with `os.getenv()` or `$OPENROUTER_API_KEY`
4. **API calls work** - The skill can make authenticated requests to OpenRouter

**Key Points:**
- Environment name MUST be `copilot` (lowercase)
- Secrets are more secure than variables for API keys
- Changes take effect immediately for new Copilot sessions
- No workflow file needed - GitHub handles it automatically

## Alternative Setups

### For Local Development

When developing locally (not in Copilot coding agent), use traditional methods:

```bash
# In your shell profile
export OPENROUTER_API_KEY="sk-or-v1-your-key"

# Or use .env file
echo "OPENROUTER_API_KEY=sk-or-v1-your-key" > .env
source .env
```

See [OPENROUTER_API_KEY_SETUP.md](./OPENROUTER_API_KEY_SETUP.md) for detailed local setup.

### For Organization-Level Secrets

If you have multiple repositories using this skill:

1. Go to your **Organization settings**
2. Navigate to **Secrets and variables** → **Actions**
3. Add organization-level secret: `OPENROUTER_API_KEY`
4. Select which repositories can access it

### For VS Code Copilot Agent Mode

When using Copilot agent mode in VS Code (not coding agent):

Create `.vscode/settings.json`:

```json
{
  "terminal.integrated.env.linux": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key"
  },
  "terminal.integrated.env.osx": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key"
  },
  "terminal.integrated.env.windows": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key"
  }
}
```

**Important:** Add `.vscode/settings.json` to `.gitignore`!

## Troubleshooting

### Secret Not Found

**Symptom:** Skill reports "OPENROUTER_API_KEY not found in environment"

**Solution:**
1. Verify environment name is exactly `copilot` (lowercase)
2. Check the secret is added: Settings → Environments → copilot → Environment secrets
3. Ensure the secret name is exactly `OPENROUTER_API_KEY` (case-sensitive)
4. Try removing and re-adding the secret
5. Start a new Copilot session (environment loads at session start)

### Environment Not Visible

**Symptom:** Can't find "Environments" in repository settings

**Solution:**
1. Make sure you're in repository Settings (not organization or user settings)
2. Look in the left sidebar for "Environments"
3. If missing, create a new environment named `copilot`
4. Ensure you have admin permissions on the repository

### API Key Not Accessible in Scripts

**Symptom:** Scripts report "OPENROUTER_API_KEY not found"

**Solution:**
1. Verify the copilot environment secret is set correctly
2. Ensure scripts are reading from environment:
   ```python
   import os
   api_key = os.getenv("OPENROUTER_API_KEY")
   ```
3. Start a fresh Copilot session
4. Check if the secret value is correct (no extra spaces)

## Security Best Practices

### ✅ DO:
- **Use copilot environment secrets** for API keys
- **Never commit secrets** to the repository
- **Add `.env` to `.gitignore`**
- **Rotate keys periodically**
- **Monitor usage** at OpenRouter dashboard
- **Limit repository access** to trusted collaborators

### ❌ DON'T:
- **Never hardcode API keys** in code files
- **Never commit `.env` files** with real keys
- **Don't use production keys** for testing
- **Don't share secrets** in issues or PRs
- **Don't commit `.vscode/settings.json`** with secrets

## Verification Checklist

- [ ] OpenRouter API key obtained from openrouter.ai
- [ ] Copilot environment created in repository settings
- [ ] Secret added: Settings → Environments → copilot → Environment secrets
- [ ] Secret name is exactly: `OPENROUTER_API_KEY`
- [ ] Tested with GitHub Copilot coding agent

## Quick Reference

### Add Secret to Copilot Environment
```
Repository → Settings → Environments → copilot
→ Environment secrets → Add environment secret
Name: OPENROUTER_API_KEY
Secret: sk-or-v1-your-key-here
```
Repository → Settings → Secrets and variables → Actions → New repository secret
Name: OPENROUTER_API_KEY
Secret: sk-or-v1-your-key-here
```

### Add Secret via CLI
```bash
gh secret set OPENROUTER_API_KEY --body "sk-or-v1-your-key-here"
```
### Use with Copilot
Just ask Copilot for asset generation - it will automatically use the secret!

## Additional Resources

- [GitHub Docs: Customizing the agent environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)
- [GitHub Docs: Using environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Local Setup Guide](./OPENROUTER_API_KEY_SETUP.md)
- [Agent Skills Documentation](./.github/skills/README.md)

## Summary

To provide your OpenRouter API key to GitHub Copilot coding agent:

1. ✅ Navigate to **Settings** → **Environments** → **copilot**
2. ✅ Add `OPENROUTER_API_KEY` as an environment secret
3. ✅ Use GitHub Copilot naturally - it will automatically access the key!

The copilot environment provides the secret to Copilot's execution environment, allowing the nano-banana-assets skill to authenticate with OpenRouter and generate your assets.
