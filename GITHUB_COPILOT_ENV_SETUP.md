# Setting Environment Variables for GitHub Copilot Coding Agent

This guide explains how to configure the `OPENROUTER_API_KEY` environment variable so GitHub Copilot coding agent can use the nano-banana-assets skill.

## Overview

GitHub Copilot coding agent runs in an **ephemeral GitHub Actions environment**. To provide your OpenRouter API key securely, you need to:

1. Add the API key as a **repository secret**
2. Use the **`.github/workflows/copilot-setup-steps.yml`** workflow to inject it into the environment
3. The workflow runs automatically before Copilot starts working

## Step-by-Step Setup

### 1. Get Your OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to **Keys** section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

### 2. Add API Key to Repository Secrets

#### On GitHub.com

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Set:
   - **Name:** `OPENROUTER_API_KEY`
   - **Secret:** Your OpenRouter API key (paste the full key)
6. Click **Add secret**

#### Via GitHub CLI

```bash
# Set the secret using gh CLI
gh secret set OPENROUTER_API_KEY --body "sk-or-v1-your-key-here"

# Verify it was added
gh secret list
```

### 3. Verify the Workflow File Exists

The repository includes `.github/workflows/copilot-setup-steps.yml` which:
- Sets up Node.js and Python
- Installs dependencies
- Makes scripts executable
- **Injects `OPENROUTER_API_KEY` from secrets into the environment**

Check it's in place:

```bash
cat .github/workflows/copilot-setup-steps.yml
```

### 4. Test the Setup

Trigger the workflow manually to verify it works:

1. Go to **Actions** tab in your repository
2. Click **Copilot Setup Steps** workflow
3. Click **Run workflow**
4. Check the workflow output for:
   - ✅ OpenRouter API key set from repository secret
   - ✅ OPENROUTER_API_KEY is set

### 5. Use with GitHub Copilot

Now when you use GitHub Copilot coding agent:

1. Open a PR or work in the repository
2. Ask Copilot for asset generation:
   ```
   "Generate a modern icon for my website"
   "Create a hero banner with gradient background"
   ```
3. Copilot automatically:
   - Runs the setup workflow
   - Loads the OPENROUTER_API_KEY from secrets
   - Uses the nano-banana-assets skill
   - Generates the assets!

## How It Works

### The Workflow File

The key section of `.github/workflows/copilot-setup-steps.yml`:

```yaml
jobs:
  copilot-setup-steps:  # MUST be named exactly this
    runs-on: ubuntu-latest
    steps:
      # ... other setup steps ...
      
      - name: Set OpenRouter API Key
        run: |
          if [ -n "${{ secrets.OPENROUTER_API_KEY }}" ]; then
            echo "OPENROUTER_API_KEY=${{ secrets.OPENROUTER_API_KEY }}" >> $GITHUB_ENV
            echo "✅ OpenRouter API key set from repository secret"
          else
            echo "⚠️  OPENROUTER_API_KEY not found in repository secrets"
          fi
```

**Important:** 
- The job MUST be named `copilot-setup-steps` for Copilot to use it
- It runs on the default branch before Copilot starts
- Environment variables are set with `>> $GITHUB_ENV`

### How Copilot Accesses the Variable

1. **Workflow runs first** - When Copilot starts, it runs this workflow
2. **Variable is set** - `OPENROUTER_API_KEY` is injected into `$GITHUB_ENV`
3. **Skill scripts access it** - Python/Bash scripts read it with `os.getenv()` or `$OPENROUTER_API_KEY`
4. **API calls work** - The skill can now make authenticated requests to OpenRouter

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

**Symptom:** Workflow shows "⚠️ OPENROUTER_API_KEY not found in repository secrets"

**Solution:**
1. Verify secret is added in repository settings
2. Check the name is exactly `OPENROUTER_API_KEY` (case-sensitive)
3. Ensure the workflow has permission to access secrets
4. Try deleting and re-adding the secret

### Workflow Not Running

**Symptom:** Copilot doesn't seem to use the environment

**Solution:**
1. Check the workflow file is on the **default branch** (main/master)
2. Verify the job is named exactly `copilot-setup-steps`
3. Look at Actions tab to see if workflow ran
4. Check for workflow syntax errors

### API Key Not Accessible in Scripts

**Symptom:** Scripts report "OPENROUTER_API_KEY not found"

**Solution:**
1. Verify the workflow ran successfully
2. Check the workflow output for "✅ OpenRouter API key set"
3. Ensure scripts are reading from environment:
   ```python
   import os
   api_key = os.getenv("OPENROUTER_API_KEY")
   ```
4. Make sure `>> $GITHUB_ENV` is used, not `export` alone

### Permission Errors

**Symptom:** "Permission denied" when running scripts

**Solution:**
The workflow includes a step to make scripts executable:
```yaml
- name: Make scripts executable
  run: |
    chmod +x .github/skills/nano-banana-assets/scripts/*.sh
    chmod +x .github/skills/nano-banana-assets/scripts/*.py
```

If still having issues, check the repository file permissions.

## Security Best Practices

### ✅ DO:
- **Use repository secrets** for API keys
- **Never commit secrets** to the repository
- **Add `.env` to `.gitignore`**
- **Use organization secrets** for shared access
- **Rotate keys periodically**
- **Monitor usage** at OpenRouter dashboard
- **Limit repository access** to trusted collaborators

### ❌ DON'T:
- **Never hardcode API keys** in workflow files
- **Never commit `.env` files** with real keys
- **Don't use production keys** for testing
- **Don't share secrets** in issues or PRs
- **Don't log the full API key** in workflow output
- **Don't commit `.vscode/settings.json`** with secrets

## Verification Checklist

- [ ] OpenRouter API key obtained from openrouter.ai
- [ ] Secret added to repository: `OPENROUTER_API_KEY`
- [ ] Workflow file exists: `.github/workflows/copilot-setup-steps.yml`
- [ ] Workflow job named exactly: `copilot-setup-steps`
- [ ] Workflow tested via Actions tab
- [ ] Workflow output shows: "✅ OpenRouter API key set"
- [ ] Scripts are executable (chmod +x applied)
- [ ] Tested with GitHub Copilot coding agent

## Quick Reference

### Add Secret via GitHub UI
```
Repository → Settings → Secrets and variables → Actions → New repository secret
Name: OPENROUTER_API_KEY
Secret: sk-or-v1-your-key-here
```

### Add Secret via CLI
```bash
gh secret set OPENROUTER_API_KEY --body "sk-or-v1-your-key-here"
```

### Test Workflow
```
Repository → Actions → Copilot Setup Steps → Run workflow
```

### Verify in Workflow Output
```
✅ OpenRouter API key set from repository secret
✅ OPENROUTER_API_KEY is set
   (First 20 chars: sk-or-v1-xxxxxxxxxx...)
```

## Additional Resources

- [GitHub Docs: Customizing the agent environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)
- [GitHub Docs: Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Local Setup Guide](./OPENROUTER_API_KEY_SETUP.md)
- [Agent Skills Documentation](./.github/skills/README.md)

## Summary

To provide your OpenRouter API key to GitHub Copilot coding agent:

1. ✅ Add `OPENROUTER_API_KEY` as a repository secret
2. ✅ Ensure `.github/workflows/copilot-setup-steps.yml` exists
3. ✅ Verify the workflow runs successfully
4. ✅ Use GitHub Copilot naturally - it will automatically access the key!

The workflow injects the secret into Copilot's environment, allowing the nano-banana-assets skill to authenticate with OpenRouter and generate your assets.
