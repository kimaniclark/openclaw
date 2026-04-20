#!/usr/bin/env node

/**
 * Test Framer API Connection
 * Simple test to verify API key and connection
 */

// Try different import approaches
async function testFramerAPI() {
  console.log('🔍 Testing Framer API connection...');
  
  const API_KEY = 'fr_4h9z8zkdxr9z1rq5xfrx526ymz';
  
  try {
    // Test direct API call first
    const response = await fetch('https://api.framer.com/v1/sites', {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      }
    });
    
    if (response.ok) {
      const data = await response.json();
      console.log('✅ API connection successful!');
      console.log('📊 Sites found:', data);
      return data;
    } else {
      console.log('❌ API response error:', response.status, response.statusText);
      const errorText = await response.text();
      console.log('Error details:', errorText);
    }
    
  } catch (error) {
    console.error('💥 API connection failed:', error.message);
    
    // Fallback: try the npm package
    try {
      console.log('🔄 Trying framer-api package...');
      const { createFramerAPI } = await import('framer-api');
      const framer = createFramerAPI(API_KEY);
      console.log('✅ Package loaded successfully!');
      return framer;
    } catch (pkgError) {
      console.error('📦 Package import failed:', pkgError.message);
    }
  }
}

// Run the test
testFramerAPI()
  .then(result => {
    if (result) {
      console.log('🎉 Framer API is ready for Crown Acquisitions automation!');
    }
  })
  .catch(console.error);