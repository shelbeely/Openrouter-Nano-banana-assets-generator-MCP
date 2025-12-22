# OpenRouter API Reference for Nano Banana Pro

## Overview

This document provides detailed API reference for using OpenRouter's Nano Banana Pro (Google Gemini 3 Pro Image Preview) model for asset generation.

## Base Configuration

### Endpoint
```
POST https://openrouter.ai/api/v1/chat/completions
```

### Model ID
```
google/gemini-3-pro-image-preview
```

### Authentication
```
Authorization: Bearer <your-api-key>
```

Get your API key from: https://openrouter.ai/

## Request Structure

### Minimal Request

```json
{
  "model": "google/gemini-3-pro-image-preview",
  "messages": [
    {
      "role": "user",
      "content": "Generate a professional icon"
    }
  ],
  "modalities": ["image", "text"]
}
```

### Full Request with All Options

```json
{
  "model": "google/gemini-3-pro-image-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/reference.png"
          }
        },
        {
          "type": "text",
          "text": "Your detailed prompt here"
        }
      ]
    }
  ],
  "modalities": ["image", "text"],
  "image_config": {
    "aspect_ratio": "16:9"
  },
  "temperature": 0.7,
  "max_tokens": 4096,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0
}
```

## Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Must be "google/gemini-3-pro-image-preview" |
| `messages` | array | Array of message objects |
| `modalities` | array | Must include "image" and "text" |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image_config.aspect_ratio` | string | "1:1" | Aspect ratio for generated images |
| `temperature` | number | 0.7 | Sampling temperature (0.0 to 2.0) |
| `max_tokens` | number | 4096 | Maximum tokens in response |
| `top_p` | number | 1.0 | Nucleus sampling parameter |
| `frequency_penalty` | number | 0.0 | Penalty for token frequency |
| `presence_penalty` | number | 0.0 | Penalty for token presence |

### Message Content Types

#### Text Content
```json
{
  "type": "text",
  "text": "Your prompt here"
}
```

#### Image URL Content
```json
{
  "type": "image_url",
  "image_url": {
    "url": "https://example.com/image.png"
  }
}
```

#### Base64 Image Content
```json
{
  "type": "image_url",
  "image_url": {
    "url": "data:image/png;base64,iVBORw0KGgoAAAANS..."
  }
}
```

## Aspect Ratios

Supported aspect ratios (case-sensitive):

| Aspect Ratio | Use Case | Example Dimensions |
|--------------|----------|-------------------|
| `1:1` | Square, Instagram posts, icons | 1080x1080 |
| `16:9` | Widescreen, YouTube, banners | 1920x1080 |
| `9:16` | Vertical, Stories, mobile | 1080x1920 |
| `4:3` | Traditional, presentations | 1024x768 |
| `3:4` | Vertical traditional | 768x1024 |
| `21:9` | Ultra-wide, cinematic | 2560x1080 |
| `9:21` | Ultra-tall | 1080x2560 |
| `2:3` | Portrait photography | 1080x1620 |
| `3:2` | Landscape photography | 1620x1080 |

## Response Structure

### Successful Response

```json
{
  "id": "gen-xxxxx",
  "model": "google/gemini-3-pro-image-preview",
  "object": "chat.completion",
  "created": 1234567890,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I've generated a professional icon with modern design...",
        "images": [
          {
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANS..."
            }
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 50,
    "total_tokens": 200
  }
}
```

### Image Data Format

Generated images are returned as base64-encoded data URLs:

```
data:image/png;base64,<base64-encoded-data>
```

To decode and save:

**Python:**
```python
import base64

data_url = response["choices"][0]["message"]["images"][0]["image_url"]["url"]
base64_data = data_url.split("base64,")[1]

with open("image.png", "wb") as f:
    f.write(base64.b64decode(base64_data))
```

**JavaScript:**
```javascript
const dataUrl = response.choices[0].message.images[0].image_url.url;
const base64Data = dataUrl.split('base64,')[1];
const buffer = Buffer.from(base64Data, 'base64');

fs.writeFileSync('image.png', buffer);
```

**Bash:**
```bash
echo "$DATA_URL" | sed 's/data:image\/png;base64,//' | base64 -d > image.png
```

## Error Handling

### Error Response Format

```json
{
  "error": {
    "message": "Error description",
    "type": "invalid_request_error",
    "code": "invalid_api_key"
  }
}
```

### Common Error Codes

| Status Code | Type | Description | Solution |
|-------------|------|-------------|----------|
| 400 | `invalid_request_error` | Malformed request | Check request format |
| 401 | `authentication_error` | Invalid API key | Verify API key |
| 402 | `insufficient_credits` | No credits remaining | Add credits to account |
| 429 | `rate_limit_exceeded` | Too many requests | Implement backoff |
| 500 | `server_error` | Server-side error | Retry request |
| 503 | `service_unavailable` | Service temporarily unavailable | Retry later |

### Error Handling Example

**Python:**
```python
import requests
import time

def make_request_with_retry(payload, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                # Rate limit - exponential backoff
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            elif e.response.status_code >= 500:
                # Server error - retry
                time.sleep(1)
            else:
                # Client error - don't retry
                raise
    raise Exception("Max retries exceeded")
```

## Rate Limits

Rate limits vary by account tier. General guidelines:

- **Free tier**: Lower rate limits
- **Paid tier**: Higher rate limits based on plan
- **Credits**: Charged per request based on tokens and images generated

Monitor your usage at: https://openrouter.ai/activity

### Best Practices

1. **Implement exponential backoff** for 429 errors
2. **Cache results** when appropriate
3. **Batch requests** when possible
4. **Monitor usage** regularly
5. **Set timeout values** for requests

## Request Headers

### Required Headers

```
Authorization: Bearer <your-api-key>
Content-Type: application/json
```

### Optional Headers

```
HTTP-Referer: <your-site-url>
X-Title: <your-app-name>
```

These help OpenRouter track usage and provide better analytics.

## Complete Examples

### Example 1: Simple Icon Generation

```bash
curl -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-3-pro-image-preview",
    "messages": [{
      "role": "user",
      "content": "Generate a minimalist home icon for a website"
    }],
    "modalities": ["image", "text"],
    "image_config": {
      "aspect_ratio": "1:1"
    }
  }'
```

### Example 2: Banner with Reference Image

```bash
curl -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-3-pro-image-preview",
    "messages": [{
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/reference.png"
          }
        },
        {
          "type": "text",
          "text": "Generate a hero banner in this style with modern tech elements"
        }
      ]
    }],
    "modalities": ["image", "text"],
    "image_config": {
      "aspect_ratio": "16:9"
    }
  }'
```

### Example 3: Edit Existing Image

```bash
curl -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-3-pro-image-preview",
    "messages": [{
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/existing-image.png"
          }
        },
        {
          "type": "text",
          "text": "Adjust lighting to be warmer, increase contrast, preserve the logo"
        }
      ]
    }],
    "modalities": ["image", "text"]
  }'
```

## Model Capabilities

### Strengths

- **High-quality image generation**: Professional, production-ready outputs
- **Text rendering**: Industry-leading text in images
- **Multimodal understanding**: Processes reference images effectively
- **Identity preservation**: Maintains consistency across generations
- **Fine-grained control**: Precise edits and transformations
- **Multiple aspect ratios**: Flexible output formats

### Limitations

- **Credit-based**: Each request consumes credits
- **Rate limits**: Subject to account-tier limits
- **Processing time**: May take several seconds per request
- **Token limits**: Max 4096 tokens per request
- **Image limits**: Up to 5 reference images per request

## Best Practices

### Prompt Engineering

1. **Be specific and detailed**
   - Include style, mood, composition
   - Mention technical requirements
   - Reference specific elements

2. **Use proper structure**
   - Start with the asset type
   - Add specifications
   - Include style guidelines
   - End with requirements

3. **Leverage context**
   - Provide reference images
   - Include brand colors
   - Specify use case
   - Mention target audience

### Performance Optimization

1. **Request appropriate resolutions**
   - Don't request 4K for thumbnails
   - Use aspect ratio that matches use case
   - Consider final output size

2. **Reuse successful prompts**
   - Save effective prompt templates
   - Build a library of working patterns
   - Document what works

3. **Implement caching**
   - Cache generated assets
   - Reuse similar assets
   - Avoid redundant requests

### Cost Management

1. **Monitor usage**
   - Track requests and costs
   - Set budget alerts
   - Review usage patterns

2. **Optimize requests**
   - Batch related generations
   - Use appropriate models
   - Minimize regenerations

3. **Iterate efficiently**
   - Start with lower resolution for drafts
   - Refine prompts before final generation
   - Use editing instead of regeneration when possible

## Security Considerations

### API Key Security

- **Never hardcode** API keys in source code
- **Use environment variables** for key storage
- **Rotate keys** regularly
- **Limit key permissions** if possible
- **Monitor usage** for unauthorized access

### Input Validation

- **Validate user inputs** before sending to API
- **Sanitize prompts** to prevent injection
- **Check image URLs** for validity
- **Limit request sizes** to prevent abuse

### Data Privacy

- **Don't send sensitive data** in prompts
- **Review generated content** before sharing
- **Comply with privacy regulations**
- **Implement content filtering** if needed

## Additional Resources

- **OpenRouter Dashboard**: https://openrouter.ai/
- **API Documentation**: https://openrouter.ai/docs
- **Model Playground**: https://openrouter.ai/playground
- **Pricing**: https://openrouter.ai/models
- **Status Page**: https://status.openrouter.ai/
- **Support**: support@openrouter.ai

## Version History

- **2024-12**: Current API version
- Features: Image generation, editing, multiple aspect ratios
- Model: Google Gemini 3 Pro Image Preview

---

**Note**: This API reference is specific to the Nano Banana Pro model. Other models on OpenRouter may have different capabilities and parameters.
