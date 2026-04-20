#!/usr/bin/env node

/**
 * Test available Framer API methods
 */

import { connect } from 'framer-api';

const PROJECT_URL = "https://framer.com/projects/Crown-Acquisitions--uHcBdn1ioxiHR3jSoOfx-de4Kb";
const API_KEY = "fr_4h9z8zkdxr9z1rq5xfrx526ymz";

async function exploreFramerAPI() {
  console.log('🔍 Exploring available Framer API methods...');
  
  try {
    using framer = await connect(PROJECT_URL, API_KEY);
    console.log('✅ Connected successfully!');
    
    // Check what methods are available
    console.log('📋 Available methods:');
    console.log(Object.getOwnPropertyNames(framer));
    console.log(Object.getOwnPropertyNames(Object.getPrototypeOf(framer)));
    
    // Try some common methods
    try {
      const collections = await framer.getCMSCollections();
      console.log('✅ CMS Collections:', collections);
    } catch (error) {
      console.log('❌ getCMSCollections failed:', error.message);
    }
    
    try {
      const pages = await framer.getPages();
      console.log('✅ Pages:', pages);
    } catch (error) {
      console.log('❌ getPages failed:', error.message);
    }
    
    // Try to get any available data
    try {
      const data = await framer.getData();
      console.log('✅ Data:', data);
    } catch (error) {
      console.log('❌ getData failed:', error.message);
    }
    
  } catch (error) {
    console.error('❌ Connection failed:', error);
  }
}

exploreFramerAPI();