# GitHub Workflows for Copilot Agent

This directory contains workflows that customize the environment for GitHub Copilot coding agent.

## copilot-setup-steps.yml

This workflow prepares the environment for GitHub Copilot coding agent by:

1. **Setting up runtime environments**
   - Node.js 20 (for MCP server)
   - Python 3.11 (for agent skill scripts)

2. **Installing dependencies**
   - npm packages for MCP server
   - Python requests library for API calls

3. **Building the project**
   - Compiles TypeScript MCP server

4. **Making scripts executable**
   - Ensures all helper scripts can run

5. **Injecting environment variables**
   - Loads `OPENROUTER_API_KEY` from repository secrets
   - Sets additional environment variables

## How It Works

### When Does It Run?

The workflow runs automatically when:
- GitHub Copilot coding agent starts working
- You manually trigger it via Actions tab
- The workflow file is pushed/updated

### Job Requirements

**Critical:** The job MUST be named `copilot-setup-steps` for Copilot to use it.

```yaml
jobs:
  copilot-setup-steps:  # This exact name is required!
    runs-on: ubuntu-latest
    steps:
      # ... setup steps ...
```

### Environment Variable Injection

The workflow injects secrets into the environment:

```yaml
- name: Set OpenRouter API Key
  run: |
    echo "OPENROUTER_API_KEY=${{ secrets.OPENROUTER_API_KEY }}" >> $GITHUB_ENV
```

This makes `OPENROUTER_API_KEY` available to:
- All subsequent workflow steps
- Scripts run by Copilot
- The nano-banana-assets skill

## Setup Instructions

### 1. Add Your API Key as a Secret

**Via GitHub UI:**
```
Repository → Settings → Secrets and variables → Actions
→ New repository secret
Name: OPENROUTER_API_KEY
Secret: sk-or-v1-your-key-here
```

**Via GitHub CLI:**
```bash
gh secret set OPENROUTER_API_KEY --body "sk-or-v1-your-key-here"
```

### 2. Verify Workflow Exists

Check this file is on your default branch:
```bash
git ls-files .github/workflows/copilot-setup-steps.yml
```

### 3. Test the Workflow

Run it manually:
```
Repository → Actions → Copilot Setup Steps → Run workflow
```

Check the output for:
- ✅ OpenRouter API key set from repository secret
- ✅ Build successful
- ✅ Scripts executable
- ✅ Environment ready

## What Gets Set Up

### Installed Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Node.js | 20 | MCP server runtime |
| Python | 3.11 | Agent skill scripts |
| npm packages | latest | MCP SDK dependencies |
| requests (Python) | latest | HTTP API calls |

### Environment Variables

| Variable | Source | Purpose |
|----------|--------|---------|
| `OPENROUTER_API_KEY` | Repository secret | OpenRouter API authentication |
| `NODE_ENV` | Workflow | Environment mode (production) |
| `SKILL_PATH` | Workflow | Location of agent skill |

### Built Artifacts

- `dist/index.js` - Compiled MCP server
- `dist/index.d.ts` - TypeScript definitions

### Executable Scripts

- `.github/skills/nano-banana-assets/scripts/generate_asset.py`
- `.github/skills/nano-banana-assets/scripts/generate_asset.sh`
- `demo-agent-skill.sh`
- `setup-api-key.sh`
- `validate.sh`

## Workflow Output

When successful, you'll see:

```
======================================
GitHub Copilot Environment Setup
======================================

Node.js version: v20.x.x
npm version: 10.x.x
Python version: 3.11.x

Build status:
-rwxr-xr-x 1 runner runner 123456 Dec 23 00:00 dist/index.js

Skill location:
-rw-r--r-- 1 runner runner 45678 Dec 23 00:00 .github/skills/nano-banana-assets/SKILL.md

Python scripts:
-rwxr-xr-x 1 runner runner 12345 Dec 23 00:00 generate_asset.py
-rwxr-xr-x 1 runner runner 6789 Dec 23 00:00 generate_asset.sh

✅ OPENROUTER_API_KEY is set
   (First 20 chars: sk-or-v1-xxxxxxxxxx...)

Environment ready for GitHub Copilot!
======================================
```

## Troubleshooting

### Workflow Fails with "Secret not found"

**Cause:** `OPENROUTER_API_KEY` not added to repository secrets.

**Fix:** Add the secret following [SECRET_SETUP_GUIDE.md](../SECRET_SETUP_GUIDE.md)

### Workflow Not Running

**Cause:** File not on default branch or job name incorrect.

**Fix:**
1. Ensure file is on `main` or `master` branch
2. Verify job name is exactly `copilot-setup-steps`
3. Check Actions tab for errors

### Scripts Not Executable

**Cause:** chmod step failed.

**Fix:** The workflow includes:
```yaml
- name: Make scripts executable
  run: chmod +x .github/skills/nano-banana-assets/scripts/*.{sh,py}
```

If it still fails, check file permissions in the repo.

### Build Fails

**Cause:** TypeScript compilation errors.

**Fix:**
1. Check `src/index.ts` for syntax errors
2. Ensure `package.json` dependencies are correct
3. Run locally: `npm run build`

## Modifying the Workflow

### Adding More Environment Variables

Add to the "Set additional environment variables" step:

```yaml
- name: Set additional environment variables
  run: |
    echo "NODE_ENV=production" >> $GITHUB_ENV
    echo "SKILL_PATH=.github/skills/nano-banana-assets" >> $GITHUB_ENV
    echo "YOUR_VAR=your_value" >> $GITHUB_ENV  # Add here
```

### Adding More Secrets

1. Add secret to repository:
   ```
   Settings → Secrets and variables → Actions → New repository secret
   ```

2. Inject in workflow:
   ```yaml
   - name: Set your secret
     run: |
       echo "YOUR_SECRET=${{ secrets.YOUR_SECRET }}" >> $GITHUB_ENV
   ```

### Installing Additional Tools

Add setup steps before the "Verify setup" step:

```yaml
- name: Setup additional tool
  run: |
    # Your installation commands
```

## Best Practices

✅ **DO:**
- Keep the job name as `copilot-setup-steps`
- Use repository secrets for sensitive data
- Test the workflow via Actions tab
- Include verification steps
- Document changes in comments

❌ **DON'T:**
- Don't rename the job
- Don't hardcode secrets in workflow
- Don't remove the workflow from default branch
- Don't skip the checkout step

## Resources

- [GitHub Docs: Customize Agent Environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)
- [GitHub Docs: Using Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [GitHub Docs: Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Secret Setup Guide](../SECRET_SETUP_GUIDE.md)
- [Environment Setup Guide](../GITHUB_COPILOT_ENV_SETUP.md)

## Summary

This workflow:
1. ✅ Runs automatically when Copilot coding agent starts
2. ✅ Sets up Node.js and Python environments
3. ✅ Installs all dependencies
4. ✅ Builds the MCP server
5. ✅ Makes scripts executable
6. ✅ Injects `OPENROUTER_API_KEY` from secrets
7. ✅ Prepares everything for the nano-banana-assets skill

Once configured, GitHub Copilot can seamlessly use the skill to generate professional web assets! 🎨
