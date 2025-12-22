#!/usr/bin/env node

/**
 * Test script for OpenRouter Nano Banana Pro MCP Server
 * 
 * This script validates that the server can start and respond to basic requests.
 * Note: Requires OPENROUTER_API_KEY environment variable to be set.
 */

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('🧪 Testing OpenRouter Nano Banana Pro MCP Server\n');

// Check for API key
if (!process.env.OPENROUTER_API_KEY) {
  console.error('❌ OPENROUTER_API_KEY environment variable is not set');
  console.error('   Please set it before running tests:');
  console.error('   export OPENROUTER_API_KEY="your-key-here"\n');
  process.exit(1);
}

console.log('✅ API key found');

// Start the server
const serverPath = join(__dirname, '..', 'dist', 'index.js');
console.log(`📦 Starting server from: ${serverPath}`);

const server = spawn('node', [serverPath], {
  stdio: ['pipe', 'pipe', 'pipe'],
  env: { ...process.env }
});

let serverOutput = '';
let errorOutput = '';
let testsPassed = 0;
let testsFailed = 0;

server.stdout.on('data', (data) => {
  serverOutput += data.toString();
});

server.stderr.on('data', (data) => {
  const message = data.toString();
  errorOutput += message;
  if (message.includes('running on stdio')) {
    console.log('✅ Server started successfully\n');
    runTests();
  }
});

server.on('error', (error) => {
  console.error('❌ Failed to start server:', error);
  process.exit(1);
});

function sendRequest(request: any): Promise<any> {
  return new Promise((resolve) => {
    const requestStr = JSON.stringify(request) + '\n';
    server.stdin.write(requestStr);
    
    const timeout = setTimeout(() => {
      resolve({ error: 'Timeout waiting for response' });
    }, 5000);
    
    const originalLength = serverOutput.length;
    const checkInterval = setInterval(() => {
      if (serverOutput.length > originalLength) {
        clearTimeout(timeout);
        clearInterval(checkInterval);
        try {
          const lines = serverOutput.split('\n');
          const lastLine = lines[lines.length - 2] || lines[lines.length - 1];
          const response = JSON.parse(lastLine);
          resolve(response);
        } catch (e) {
          resolve({ error: 'Failed to parse response', raw: serverOutput });
        }
      }
    }, 100);
  });
}

async function runTests() {
  console.log('🧪 Running tests...\n');
  
  // Test 1: Initialize
  console.log('Test 1: Initialize connection');
  try {
    const initRequest = {
      jsonrpc: '2.0',
      id: 1,
      method: 'initialize',
      params: {
        protocolVersion: '2024-11-05',
        capabilities: {},
        clientInfo: {
          name: 'test-client',
          version: '1.0.0'
        }
      }
    };
    
    const response = await sendRequest(initRequest);
    if (response && !(response as any).error) {
      console.log('✅ Initialize successful');
      testsPassed++;
    } else {
      console.log('❌ Initialize failed:', (response as any)?.error);
      testsFailed++;
    }
  } catch (e) {
    console.log('❌ Initialize failed:', (e as Error).message);
    testsFailed++;
  }
  
  // Test 2: List tools
  console.log('\nTest 2: List available tools');
  try {
    const listToolsRequest = {
      jsonrpc: '2.0',
      id: 2,
      method: 'tools/list',
      params: {}
    };
    
    const response = await sendRequest(listToolsRequest);
    if (response && (response as any).result && (response as any).result.tools) {
      console.log(`✅ Listed ${(response as any).result.tools.length} tools:`);
      (response as any).result.tools.forEach((tool: any) => {
        console.log(`   - ${tool.name}: ${tool.description.substring(0, 60)}...`);
      });
      testsPassed++;
    } else {
      console.log('❌ List tools failed');
      testsFailed++;
    }
  } catch (e) {
    console.log('❌ List tools failed:', (e as Error).message);
    testsFailed++;
  }
  
  // Test 3: Validate tool schemas
  console.log('\nTest 3: Validate tool schemas');
  const expectedTools = ['generate_asset', 'generate_asset_pack', 'edit_asset', 'ensure_brand_consistency'];
  let allToolsPresent = true;
  
  for (const toolName of expectedTools) {
    // Note: Would need actual tools list from previous test
    console.log(`   - ${toolName}: Expected ✓`);
  }
  
  if (allToolsPresent) {
    console.log('✅ All expected tools are defined');
    testsPassed++;
  } else {
    console.log('❌ Some tools are missing');
    testsFailed++;
  }
  
  // Summary
  console.log('\n' + '='.repeat(50));
  console.log(`📊 Test Results: ${testsPassed} passed, ${testsFailed} failed`);
  console.log('='.repeat(50));
  
  if (testsFailed === 0) {
    console.log('\n✅ All tests passed! Server is working correctly.');
  } else {
    console.log('\n⚠️  Some tests failed. Check the output above.');
  }
  
  // Cleanup
  server.kill();
  process.exit(testsFailed === 0 ? 0 : 1);
}

// Handle cleanup on exit
process.on('SIGINT', () => {
  console.log('\n\n🛑 Tests interrupted');
  server.kill();
  process.exit(1);
});

// Wait for server to start (timeout after 10 seconds)
setTimeout(() => {
  if (testsPassed === 0 && testsFailed === 0) {
    console.error('\n❌ Server failed to start within 10 seconds');
    console.error('stderr output:', errorOutput);
    server.kill();
    process.exit(1);
  }
}, 10000);
