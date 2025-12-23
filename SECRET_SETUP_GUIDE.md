# Quick Setup: Add Your OpenRouter API Key as a GitHub Secret

This is a quick visual guide for adding your OpenRouter API key as a repository secret for GitHub Copilot coding agent.

## Steps

### 1. Get Your OpenRouter API Key

→ Visit **[openrouter.ai](https://openrouter.ai/)**  
→ Sign up or log in  
→ Go to **Keys** section  
→ Create a new API key  
→ Copy the key (starts with `sk-or-v1-`)

### 2. Add as Repository Secret

#### Navigate to Settings

```
Your Repository → Settings (top menu bar)
```

#### Go to Secrets

```
Left sidebar → Secrets and variables → Actions
```

#### Add New Secret

```
Click: "New repository secret"

Name:   OPENROUTER_API_KEY
Secret: [paste your sk-or-v1-... key here]

Click: "Add secret"
```

### 3. Verify Setup

The secret is now available to GitHub Copilot coding agent!

Check the workflow:
```
Repository → Actions → Copilot Setup Steps → Run workflow
```

Look for in the output:
```
✅ OpenRouter API key set from repository secret
✅ OPENROUTER_API_KEY is set
```

### 4. Use with GitHub Copilot

Now just ask Copilot naturally:
```
"Generate a modern icon for my website"
"Create a hero banner for my landing page"
"I need social media assets for my brand"
```

Copilot will automatically:
1. Run the setup workflow
2. Load `OPENROUTER_API_KEY` from your secret
3. Use the nano-banana-assets skill
4. Generate your assets!

## Visual Flow

```
┌─────────────────────────────────────────────┐
│  1. You: Set Repository Secret             │
│     Name: OPENROUTER_API_KEY                │
│     Value: sk-or-v1-your-key                │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  2. GitHub Copilot: Starts working          │
│     Runs: .github/workflows/                │
│           copilot-setup-steps.yml           │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  3. Workflow: Injects secret                │
│     OPENROUTER_API_KEY → $GITHUB_ENV        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  4. Skill: Uses API key                     │
│     .github/skills/nano-banana-assets/      │
│     Calls OpenRouter API                    │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  5. Result: Assets generated! 🎨            │
└─────────────────────────────────────────────┘
```

## Important Notes

✅ **DO:**
- Use repository secrets for the API key
- Name the secret exactly: `OPENROUTER_API_KEY`
- Keep your API key confidential
- Monitor usage at openrouter.ai dashboard

❌ **DON'T:**
- Don't commit API keys to code
- Don't hardcode keys in workflows
- Don't share secrets publicly

## Troubleshooting

### Secret not working?

1. **Check the name**: Must be exactly `OPENROUTER_API_KEY` (case-sensitive)
2. **Check the workflow**: Must be on default branch (main/master)
3. **Check Actions tab**: See if workflow ran successfully
4. **Check workflow output**: Look for "✅ OpenRouter API key set"

### Still having issues?

See detailed guides:
- [GitHub Copilot Environment Setup](./GITHUB_COPILOT_ENV_SETUP.md)
- [OpenRouter API Key Setup](./OPENROUTER_API_KEY_SETUP.md)

## CLI Alternative

If you prefer using GitHub CLI:

```bash
# Add the secret
gh secret set OPENROUTER_API_KEY

# When prompted, paste your API key
# Or provide directly:
gh secret set OPENROUTER_API_KEY --body "sk-or-v1-your-key-here"

# Verify
gh secret list
```

## That's It!

Once the secret is added, GitHub Copilot coding agent can use the nano-banana-assets skill to generate professional web assets for you automatically.

Just ask naturally and Copilot handles the rest! 🚀
