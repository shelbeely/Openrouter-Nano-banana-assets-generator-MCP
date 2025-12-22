# Configuration Guide

## MCP Server Configuration

### Claude Desktop Configuration

The server can be configured in Claude Desktop's config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

#### Basic Configuration

```json
{
  "mcpServers": {
    "nano-banana-assets": {
      "command": "node",
      "args": [
        "/absolute/path/to/openrouter-nano-banana-mcp/dist/index.js"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

#### With NPM Package (if installed globally)

```json
{
  "mcpServers": {
    "nano-banana-assets": {
      "command": "npx",
      "args": [
        "openrouter-nano-banana-mcp"
      ],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-..."
      }
    }
  }
}
```

## Environment Variables

### Required

- **OPENROUTER_API_KEY**: Your OpenRouter API key (get it from https://openrouter.ai/)

### Optional

You can add additional environment variables for customization:

```json
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-...",
    "NODE_ENV": "production"
  }
}
```

## API Key Setup

### Getting Your OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to the API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

### Storing Your API Key

#### Option 1: Environment Variable (Recommended for Development)

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

#### Option 2: In Claude Desktop Config (Recommended for Production)

Store directly in the `claude_desktop_config.json` as shown above.

#### Option 3: .env File (For Local Testing)

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

**Note**: The `.env` file is gitignored by default.

## Model Configuration

The server uses the `google/gemini-3-pro-image-preview` model by default. This is Nano Banana Pro via OpenRouter.

### Model Features

- **Context Window**: Large multimodal context for complex requests
- **Image Understanding**: Can analyze up to 5 reference images
- **Generation Quality**: Professional-grade outputs
- **Resolution Support**: Up to 4K (3840x2160)
- **Aspect Ratios**: Flexible ratios from 1:1 to 21:9

## Usage Limits

OpenRouter has usage limits based on your account tier:

- **Free Tier**: Limited requests per day
- **Paid Tier**: Higher limits, priority access

Check your current usage at [OpenRouter Dashboard](https://openrouter.ai/dashboard).

## Troubleshooting

### Server Not Starting

1. Check if Node.js is installed: `node --version` (requires 18+)
2. Verify the path in config is absolute
3. Check if the dist folder exists and contains index.js
4. Ensure the file is executable: `chmod +x dist/index.js`

### API Key Issues

1. Verify your API key is correct
2. Check if the key has sufficient credits
3. Ensure the key has access to the Gemini model
4. Try regenerating the API key

### Connection Errors

1. Check your internet connection
2. Verify OpenRouter API is accessible
3. Check for firewall blocking
4. Ensure no proxy configuration issues

### Build Issues

```bash
# Clean and rebuild
rm -rf dist node_modules
npm install
npm run build
```

## Advanced Configuration

### Custom Timeout Settings

For longer-running requests, you may want to increase timeout settings in your MCP client configuration.

### Logging

The server logs to stderr. To capture logs:

```bash
node dist/index.js 2> server.log
```

### Multiple Instances

You can run multiple instances with different configurations:

```json
{
  "mcpServers": {
    "nano-banana-dev": {
      "command": "node",
      "args": ["/path/to/dev/dist/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-dev-key",
        "NODE_ENV": "development"
      }
    },
    "nano-banana-prod": {
      "command": "node",
      "args": ["/path/to/prod/dist/index.js"],
      "env": {
        "OPENROUTER_API_KEY": "sk-or-v1-prod-key",
        "NODE_ENV": "production"
      }
    }
  }
}
```

## Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** for sensitive data
3. **Rotate keys regularly** for production use
4. **Monitor usage** to detect unauthorized access
5. **Use separate keys** for development and production

## Performance Tips

1. **Use appropriate resolutions**: Don't request 4K if 1080p suffices
2. **Batch requests**: Use asset packs instead of individual assets
3. **Optimize reference images**: Compress images before sending
4. **Cache results**: Reuse generated assets when possible
5. **Use specific prompts**: Detailed prompts reduce iteration needs

## Integration Examples

### With CI/CD

```yaml
# .github/workflows/generate-assets.yml
name: Generate Assets
on: [push]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '20'
      - run: npm install
      - run: npm run build
      - name: Generate Assets
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        run: |
          # Your asset generation script here
```

### With Docker

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
ENV OPENROUTER_API_KEY=""
CMD ["node", "dist/index.js"]
```

## Support

For issues or questions:

1. Check the [README](./README.md) and [EXAMPLES](./EXAMPLES.md)
2. Review [OpenRouter Documentation](https://openrouter.ai/docs)
3. Open an issue on GitHub
4. Check OpenRouter's status page
