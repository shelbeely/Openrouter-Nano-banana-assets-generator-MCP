# Quick Setup: Add Your OpenRouter API Key to Copilot Environment

This is a quick visual guide for adding your OpenRouter API key as a secret in the copilot environment for GitHub Copilot coding agent.

## Steps

### 1. Get Your OpenRouter API Key

→ Visit **[openrouter.ai](https://openrouter.ai/)**  
→ Sign up or log in  
→ Go to **Keys** section  
→ Create a new API key  
→ Copy the key (starts with `sk-or-v1-`)

### 2. Add to Copilot Environment

#### Navigate to Settings

```
Your Repository → Settings (top menu bar)
```

#### Go to Environments

```
Left sidebar → Environments
```

#### Select or Create Copilot Environment

```
Click: "copilot" environment

If it doesn't exist:
  Click: "New environment"
  Name: copilot
  Click: "Configure environment"
```

#### Add Secret

```
Under "Environment secrets" section:
  Click: "Add environment secret"

Name:   OPENROUTER_API_KEY
Secret: [paste your sk-or-v1-... key here]

Click: "Add secret"
```

### 3. Use with GitHub Copilot

Now just ask Copilot naturally:
```
"Generate a modern icon for my website"
"Create a hero banner for my landing page"
"I need social media assets for my brand"
```

Copilot will automatically:
1. Load `OPENROUTER_API_KEY` from the copilot environment
2. Use the nano-banana-assets skill
3. Generate your assets!

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
- Use copilot environment secrets for the API key
- Name the environment exactly: `copilot` (lowercase)
- Name the secret exactly: `OPENROUTER_API_KEY`
- Keep your API key confidential
- Monitor usage at openrouter.ai dashboard

❌ **DON'T:**
- Don't commit API keys to code
- Don't use regular repository secrets (use copilot environment)
- Don't share secrets publicly

## Troubleshooting

### Secret not working?

1. **Check the environment name**: Must be exactly `copilot` (lowercase)
2. **Check the secret name**: Must be exactly `OPENROUTER_API_KEY` (case-sensitive)
3. **Check location**: Settings → Environments → copilot → Environment secrets
4. **Try a new Copilot session**: Environment loads at session start

### Still having issues?

See detailed guides:
- [GitHub Copilot Environment Setup](./GITHUB_COPILOT_ENV_SETUP.md)
- [OpenRouter API Key Setup](./OPENROUTER_API_KEY_SETUP.md)

## That's It!

Once the secret is added to the copilot environment, GitHub Copilot coding agent can use the nano-banana-assets skill to generate professional web assets for you automatically.

Just ask naturally and Copilot handles the rest! 🚀
