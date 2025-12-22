#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from "@modelcontextprotocol/sdk/types.js";

// OpenRouter API configuration
const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;
const OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions";
const MODEL = "google/gemini-3-pro-image-preview";

interface ImageGenerationParams {
  prompt: string;
  aspectRatio?: string;
  resolution?: string;
  referenceImages?: string[];
  colorPalette?: string[];
  logoFile?: string;
  editInstructions?: string;
}

interface AssetPackParams {
  description: string;
  assetTypes: string[];
  brandGuidelines?: string;
  referenceImages?: string[];
  colorPalette?: string[];
  logoFile?: string;
  aspectRatio?: string;
  resolution?: string;
}

interface OpenRouterResponse {
  textContent?: string;
  images?: string[];
  fullResponse: any;
}

interface OpenRouterImage {
  image_url?: { url: string };
  url?: string;
}

interface OpenRouterMessage {
  content?: string;
  images?: OpenRouterImage[];
}

interface OpenRouterAPIResponse {
  choices: Array<{
    message: OpenRouterMessage;
  }>;
}

// Helper function to call OpenRouter API
async function callOpenRouter(
  messages: any[], 
  imageData?: string[], 
  aspectRatio?: string
): Promise<OpenRouterResponse> {
  if (!OPENROUTER_API_KEY) {
    throw new Error("OPENROUTER_API_KEY environment variable is required");
  }

  // Prepare content with images if provided (for input/reference images)
  const userContent: any[] = [];
  
  if (imageData && imageData.length > 0) {
    // Add images first for context
    for (const image of imageData) {
      userContent.push({
        type: "image_url",
        image_url: {
          url: image
        }
      });
    }
  }

  // Add text message
  userContent.push({
    type: "text",
    text: messages[0].content
  });

  // Build request body with modalities for image generation
  const requestBody: any = {
    model: MODEL,
    messages: [
      {
        role: "user",
        content: userContent
      }
    ],
    modalities: ["image", "text"], // Enable image generation
    temperature: 0.7,
    max_tokens: 4096,
  };

  // Add image configuration if aspect ratio specified
  if (aspectRatio) {
    requestBody.image_config = {
      aspect_ratio: aspectRatio
    };
  }

  const response = await fetch(OPENROUTER_API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${OPENROUTER_API_KEY}`,
      "Content-Type": "application/json",
      "HTTP-Referer": "https://github.com/shelbeely/Openrouter-Nano-banana-assets-generator-MCP",
      "X-Title": "Nano Banana Assets Generator MCP"
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`OpenRouter API error: ${response.status} - ${error}`);
  }

  const data = await response.json() as OpenRouterAPIResponse;
  const message = data.choices[0].message;
  
  // Extract both text content and generated images
  const result: OpenRouterResponse = {
    fullResponse: data
  };

  // Get text content if available
  if (message.content) {
    result.textContent = message.content;
  }

  // Get generated images if available (base64 data URLs)
  if (message.images && Array.isArray(message.images)) {
    result.images = message.images.map((img: OpenRouterImage) => 
      img.image_url?.url || img.url || ''
    ).filter(url => url !== '');
  }

  return result;
}

// Create server instance
const server = new Server(
  {
    name: "openrouter-nano-banana-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Define available tools
const TOOLS: Tool[] = [
  {
    name: "generate_asset",
    description: "Generate a single web asset using Nano Banana Pro. Supports reference images, color palettes, logos, and various aspect ratios/resolutions (including 2K/4K). Can generate icons, banners, backgrounds, UI elements, and more.",
    inputSchema: {
      type: "object",
      properties: {
        prompt: {
          type: "string",
          description: "Detailed description of the asset to generate (e.g., 'Create a modern hero banner with gradient background for a tech startup')"
        },
        aspectRatio: {
          type: "string",
          description: "Aspect ratio for the asset (e.g., '16:9', '1:1', '4:3', '21:9', '9:16')",
          enum: ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21", "2:3", "3:2"]
        },
        resolution: {
          type: "string",
          description: "Target resolution (e.g., '1920x1080', '2K', '4K', '1080x1080')",
          enum: ["1080x1080", "1920x1080", "2K", "4K", "3840x2160", "2560x1440", "1280x720"]
        },
        referenceImages: {
          type: "array",
          description: "Array of reference image URLs or base64-encoded data URLs for style guidance (max 5)",
          items: { type: "string" }
        },
        colorPalette: {
          type: "array",
          description: "Array of hex color codes to incorporate into the design (e.g., ['#FF5733', '#3498DB'])",
          items: { type: "string" }
        },
        logoFile: {
          type: "string",
          description: "Logo file URL or base64-encoded data URL to include in the asset"
        },
        editInstructions: {
          type: "string",
          description: "Optional editing instructions if modifying an existing asset (e.g., 'Adjust lighting', 'Change background color')"
        }
      },
      required: ["prompt"]
    }
  },
  {
    name: "generate_asset_pack",
    description: "Generate a complete pack of related web assets maintaining brand consistency. Perfect for creating cohesive sets of icons, banners, social media graphics, or UI kits.",
    inputSchema: {
      type: "object",
      properties: {
        description: {
          type: "string",
          description: "Overall description of the asset pack and its purpose (e.g., 'Social media kit for eco-friendly brand')"
        },
        assetTypes: {
          type: "array",
          description: "Types of assets to generate (e.g., ['hero-banner', 'icon-set', 'background', 'social-media-post', 'button-set'])",
          items: { type: "string" }
        },
        brandGuidelines: {
          type: "string",
          description: "Brand guidelines and style requirements to ensure consistency"
        },
        referenceImages: {
          type: "array",
          description: "Reference images to establish visual style (max 5)",
          items: { type: "string" }
        },
        colorPalette: {
          type: "array",
          description: "Brand color palette as hex codes",
          items: { type: "string" }
        },
        logoFile: {
          type: "string",
          description: "Brand logo to incorporate across assets"
        },
        aspectRatio: {
          type: "string",
          description: "Default aspect ratio for assets (can be overridden per asset type)",
          enum: ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21", "2:3", "3:2"]
        },
        resolution: {
          type: "string",
          description: "Default resolution (can be overridden per asset type)",
          enum: ["1080x1080", "1920x1080", "2K", "4K", "3840x2160", "2560x1440", "1280x720"]
        }
      },
      required: ["description", "assetTypes"]
    }
  },
  {
    name: "edit_asset",
    description: "Edit an existing asset with fine-grained controls. Supports localized edits, lighting adjustments, focus changes, camera transformations, and more using Nano Banana Pro's advanced editing capabilities.",
    inputSchema: {
      type: "object",
      properties: {
        sourceImage: {
          type: "string",
          description: "Source image URL or base64-encoded data URL to edit"
        },
        editInstructions: {
          type: "string",
          description: "Detailed editing instructions (e.g., 'Adjust lighting to be warmer, increase contrast, blur background')"
        },
        preserveElements: {
          type: "array",
          description: "Elements to preserve during editing (e.g., ['logo', 'text', 'main-subject'])",
          items: { type: "string" }
        },
        aspectRatio: {
          type: "string",
          description: "Target aspect ratio if different from source",
          enum: ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21", "2:3", "3:2"]
        },
        resolution: {
          type: "string",
          description: "Target resolution if upscaling/downscaling needed",
          enum: ["1080x1080", "1920x1080", "2K", "4K", "3840x2160", "2560x1440", "1280x720"]
        }
      },
      required: ["sourceImage", "editInstructions"]
    }
  },
  {
    name: "ensure_brand_consistency",
    description: "Analyze and refine assets to ensure they follow brand guidelines. Uses Nano Banana Pro's identity preservation to maintain consistency across multiple images.",
    inputSchema: {
      type: "object",
      properties: {
        assets: {
          type: "array",
          description: "Array of asset URLs or base64 data to analyze for consistency",
          items: { type: "string" }
        },
        brandGuidelines: {
          type: "string",
          description: "Detailed brand guidelines including color usage, typography, style, tone"
        },
        referenceImages: {
          type: "array",
          description: "Brand reference images showing the desired style",
          items: { type: "string" }
        },
        colorPalette: {
          type: "array",
          description: "Official brand colors as hex codes",
          items: { type: "string" }
        },
        logoFile: {
          type: "string",
          description: "Official logo file"
        }
      },
      required: ["assets", "brandGuidelines"]
    }
  }
];

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools: TOOLS };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "generate_asset": {
        const params = args as unknown as ImageGenerationParams;
        
        // Build comprehensive prompt
        let prompt = `Generate a high-quality web asset with the following specifications:\n\n`;
        prompt += `Description: ${params.prompt}\n\n`;
        
        if (params.aspectRatio) {
          prompt += `Aspect Ratio: ${params.aspectRatio}\n`;
        }
        
        if (params.resolution) {
          prompt += `Resolution: ${params.resolution}\n`;
        }
        
        if (params.colorPalette && params.colorPalette.length > 0) {
          prompt += `Color Palette: Use these colors - ${params.colorPalette.join(", ")}\n`;
        }
        
        if (params.logoFile) {
          prompt += `Logo: Incorporate the provided logo naturally into the design\n`;
        }
        
        if (params.editInstructions) {
          prompt += `\nEditing Instructions: ${params.editInstructions}\n`;
        }
        
        prompt += `\nRequirements:
- Professional, web-ready quality
- Modern and visually appealing design
- Optimized for digital use
- Clean and polished appearance
- Follow web design best practices`;

        // Collect all reference images
        const imageData: string[] = [];
        if (params.referenceImages) {
          imageData.push(...params.referenceImages);
        }
        if (params.logoFile) {
          imageData.push(params.logoFile);
        }

        const result = await callOpenRouter(
          [{ role: "user", content: prompt }],
          imageData.length > 0 ? imageData : undefined,
          params.aspectRatio
        );

        // Build response with both text and images
        let responseText = `Asset Generation Complete!\n\n`;
        
        if (result.textContent) {
          responseText += `${result.textContent}\n\n`;
        }
        
        responseText += `Specifications:\n`;
        responseText += `- Aspect Ratio: ${params.aspectRatio || "default (1:1)"}\n`;
        responseText += `- Resolution: ${params.resolution || "standard"}\n`;
        
        if (params.colorPalette && params.colorPalette.length > 0) {
          responseText += `- Color Palette: ${params.colorPalette.join(", ")}\n`;
        }
        
        if (result.images && result.images.length > 0) {
          responseText += `\n✅ Generated ${result.images.length} image(s)\n`;
          responseText += `Images are provided as base64 data URLs below.\n`;
        }

        const contentItems: any[] = [
          {
            type: "text",
            text: responseText
          }
        ];

        // Add generated images to response
        if (result.images && result.images.length > 0) {
          for (let i = 0; i < result.images.length; i++) {
            contentItems.push({
              type: "image",
              data: result.images[i],
              mimeType: "image/png"
            });
          }
        }

        return {
          content: contentItems
        };
      }

      case "generate_asset_pack": {
        const params = args as unknown as AssetPackParams;
        
        let prompt = `Generate a complete, brand-consistent asset pack for web development:\n\n`;
        prompt += `Project Description: ${params.description}\n\n`;
        prompt += `Asset Types to Generate:\n`;
        params.assetTypes.forEach((type, idx) => {
          prompt += `${idx + 1}. ${type}\n`;
        });
        prompt += `\n`;
        
        if (params.brandGuidelines) {
          prompt += `Brand Guidelines:\n${params.brandGuidelines}\n\n`;
        }
        
        if (params.colorPalette && params.colorPalette.length > 0) {
          prompt += `Brand Color Palette: ${params.colorPalette.join(", ")}\n`;
        }
        
        if (params.aspectRatio) {
          prompt += `Default Aspect Ratio: ${params.aspectRatio}\n`;
        }
        
        if (params.resolution) {
          prompt += `Default Resolution: ${params.resolution}\n`;
        }
        
        prompt += `\nRequirements:
- All assets must maintain visual consistency
- Follow the brand guidelines strictly
- Use the provided color palette throughout
- Professional, production-ready quality
- Each asset should be optimized for its specific use case
- Cohesive design language across all assets
- Modern and contemporary style
- Web-optimized output`;

        const imageData: string[] = [];
        if (params.referenceImages) {
          imageData.push(...params.referenceImages);
        }
        if (params.logoFile) {
          imageData.push(params.logoFile);
        }

        const result = await callOpenRouter(
          [{ role: "user", content: prompt }],
          imageData.length > 0 ? imageData : undefined,
          params.aspectRatio
        );

        let responseText = `Asset Pack Generation Complete!\n\n`;
        
        if (result.textContent) {
          responseText += `${result.textContent}\n\n`;
        }
        
        responseText += `Generated ${params.assetTypes.length} asset types with consistent branding:\n`;
        params.assetTypes.forEach((t, i) => {
          responseText += `${i + 1}. ${t}\n`;
        });
        
        if (result.images && result.images.length > 0) {
          responseText += `\n✅ Generated ${result.images.length} image(s)\n`;
        }

        const contentItems: any[] = [
          {
            type: "text",
            text: responseText
          }
        ];

        // Add generated images
        if (result.images && result.images.length > 0) {
          for (const image of result.images) {
            contentItems.push({
              type: "image",
              data: image,
              mimeType: "image/png"
            });
          }
        }

        return {
          content: contentItems
        };
      }

      case "edit_asset": {
        const params = args as unknown as {
          sourceImage: string;
          editInstructions: string;
          preserveElements?: string[];
          aspectRatio?: string;
          resolution?: string;
        };
        
        let prompt = `Edit the provided image with the following instructions:\n\n`;
        prompt += `Edit Instructions: ${params.editInstructions}\n\n`;
        
        if (params.preserveElements && params.preserveElements.length > 0) {
          prompt += `Preserve These Elements: ${params.preserveElements.join(", ")}\n`;
        }
        
        if (params.aspectRatio) {
          prompt += `Target Aspect Ratio: ${params.aspectRatio}\n`;
        }
        
        if (params.resolution) {
          prompt += `Target Resolution: ${params.resolution}\n`;
        }
        
        prompt += `\nEditing Requirements:
- Apply edits precisely as instructed
- Maintain image quality and professional appearance
- Preserve specified elements without alteration
- Ensure smooth transitions and natural-looking results
- Output should be web-ready and optimized`;

        const result = await callOpenRouter(
          [{ role: "user", content: prompt }],
          [params.sourceImage],
          params.aspectRatio
        );

        let responseText = `Asset Editing Complete!\n\n`;
        
        if (result.textContent) {
          responseText += `${result.textContent}\n\n`;
        }
        
        responseText += `Applied edits: ${params.editInstructions}\n`;
        responseText += `Preserved elements: ${params.preserveElements?.join(", ") || "none specified"}\n`;
        
        if (result.images && result.images.length > 0) {
          responseText += `\n✅ Generated ${result.images.length} edited image(s)\n`;
        }

        const contentItems: any[] = [
          {
            type: "text",
            text: responseText
          }
        ];

        // Add edited images
        if (result.images && result.images.length > 0) {
          for (const image of result.images) {
            contentItems.push({
              type: "image",
              data: image,
              mimeType: "image/png"
            });
          }
        }

        return {
          content: contentItems
        };
      }

      case "ensure_brand_consistency": {
        const params = args as unknown as {
          assets: string[];
          brandGuidelines: string;
          referenceImages?: string[];
          colorPalette?: string[];
          logoFile?: string;
        };
        
        let prompt = `Analyze the following assets for brand consistency and provide recommendations:\n\n`;
        prompt += `Brand Guidelines:\n${params.brandGuidelines}\n\n`;
        
        if (params.colorPalette && params.colorPalette.length > 0) {
          prompt += `Brand Colors: ${params.colorPalette.join(", ")}\n`;
        }
        
        prompt += `\nAnalysis Requirements:
- Check adherence to brand guidelines
- Verify consistent use of colors, typography, and style
- Identify inconsistencies across assets
- Provide specific recommendations for improvements
- Suggest refinements to maintain brand identity
- Ensure logo usage is consistent and appropriate
- Verify visual cohesion across all assets\n\n`;
        
        prompt += `I have ${params.assets.length} assets to analyze. Please review them for consistency.`;

        const allImages = [...params.assets];
        if (params.referenceImages) {
          allImages.push(...params.referenceImages);
        }
        if (params.logoFile) {
          allImages.push(params.logoFile);
        }

        const result = await callOpenRouter(
          [{ role: "user", content: prompt }],
          allImages
        );

        let responseText = `Brand Consistency Analysis Complete!\n\n`;
        
        if (result.textContent) {
          responseText += `${result.textContent}\n\n`;
        }
        
        responseText += `Analyzed ${params.assets.length} assets against your brand guidelines.\n`;
        
        if (result.images && result.images.length > 0) {
          responseText += `\n✅ Generated ${result.images.length} corrected/refined image(s)\n`;
        }

        const contentItems: any[] = [
          {
            type: "text",
            text: responseText
          }
        ];

        // Add any refined images if the model generated improvements
        if (result.images && result.images.length > 0) {
          for (const image of result.images) {
            contentItems.push({
              type: "image",
              data: image,
              mimeType: "image/png"
            });
          }
        }

        return {
          content: contentItems
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    return {
      content: [
        {
          type: "text",
          text: `Error: ${errorMessage}`
        }
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("OpenRouter Nano Banana Pro MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});
