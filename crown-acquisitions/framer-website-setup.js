#!/usr/bin/env node

/**
 * Crown Acquisitions Website Setup
 * Customizes Orbai template for M&A and CFE business
 */

import FramerAPI from 'framer-api';

const API_KEY = 'fr_4h9z8zkdxr9z1rq5xfrx526ymz';

const crownAcquisitionsContent = {
  // Hero Section
  hero: {
    headline: "Strategic Business Acquisitions & CFE Partnerships",
    subheadline: "We help business owners achieve successful exits through direct acquisitions and consulting-for-equity partnerships.",
    cta: "Explore Your Options"
  },

  // Navigation
  navigation: [
    "Home",
    "Services", 
    "Process",
    "Portfolio",
    "About",
    "Contact"
  ],

  // Services
  services: [
    {
      title: "Direct Business Acquisitions",
      description: "Strategic acquisition of profitable businesses with proven track records and growth potential.",
      features: ["Due Diligence", "Valuation Analysis", "Deal Structuring", "Smooth Transitions"]
    },
    {
      title: "Consulting for Equity (CFE)",
      description: "Partner with growing businesses through consulting services in exchange for equity stakes.",
      features: ["Business Consulting", "Growth Strategy", "Operational Improvements", "Exit Planning"]
    },
    {
      title: "Business Valuations", 
      description: "Professional business assessments to determine fair market value for acquisitions or exits.",
      features: ["Financial Analysis", "Market Comparisons", "Asset Evaluation", "Growth Projections"]
    },
    {
      title: "Exit Strategy Consulting",
      description: "Help business owners prepare for successful exits and maximize their business value.",
      features: ["Exit Preparation", "Value Optimization", "Buyer Matching", "Deal Negotiation"]
    }
  ],

  // Process
  process: [
    {
      step: "1",
      title: "Initial Discovery",
      description: "We start with a comprehensive discussion about your business, goals, and ideal outcomes."
    },
    {
      step: "2", 
      title: "Business Assessment",
      description: "Thorough evaluation of financials, operations, market position, and growth potential."
    },
    {
      step: "3",
      title: "Deal Structure",
      description: "Custom deal structuring that works for all parties - direct acquisition or CFE partnership."
    },
    {
      step: "4",
      title: "Due Diligence", 
      description: "Comprehensive review of all business aspects to ensure transparency and risk mitigation."
    },
    {
      step: "5",
      title: "Closing & Transition",
      description: "Seamless deal closing and smooth operational transition to ensure continued success."
    }
  ],

  // About
  about: {
    headline: "Experienced M&A Professional with a Strategic Approach",
    description: "Kimani Clark brings deep expertise in business acquisitions, legal analysis, and strategic partnerships. As an Epic Network-trained acquisition specialist with a background in patent law and business consulting, Kimani combines analytical rigor with entrepreneurial insight to structure deals that create value for all parties.",
    credentials: [
      "Epic Network M&A Training",
      "Patent Attorney (Kiklis & Clark)",
      "Business Consultant & Coach", 
      "CFE Partnership Specialist"
    ]
  },

  // Contact
  contact: {
    headline: "Ready to Explore Your Options?",
    description: "Whether you're considering selling your business or exploring strategic partnerships, we're here to help you achieve your goals.",
    cta: "Schedule a Confidential Consultation",
    email: "kimani@crownacquisitions.co",
    phone: "301-674-1098"
  }
};

async function setupCrownAcquisitionsWebsite() {
  try {
    console.log('🚀 Setting up Crown Acquisitions website...');
    
    // Initialize Framer API
    const framer = new FramerAPI(API_KEY);
    
    // Get project info
    const projects = await framer.getProjects();
    console.log('📋 Projects found:', projects.length);
    
    // Find Crown Acquisitions project
    const crownProject = projects.find(p => p.name.includes('Crown Acquisitions'));
    
    if (!crownProject) {
      throw new Error('Crown Acquisitions project not found');
    }
    
    console.log('✅ Found project:', crownProject.name);
    
    // Update content systematically
    await updateHeroSection(framer, crownProject.id);
    await updateServices(framer, crownProject.id);
    await updateProcess(framer, crownProject.id);
    await updateAbout(framer, crownProject.id);
    await updateContact(framer, crownProject.id);
    
    console.log('🎉 Crown Acquisitions website customization complete!');
    
  } catch (error) {
    console.error('❌ Setup failed:', error.message);
    throw error;
  }
}

async function updateHeroSection(framer, projectId) {
  console.log('📝 Updating hero section...');
  
  await framer.updateContent(projectId, 'hero', {
    headline: crownAcquisitionsContent.hero.headline,
    subheadline: crownAcquisitionsContent.hero.subheadline,
    ctaText: crownAcquisitionsContent.hero.cta
  });
}

async function updateServices(framer, projectId) {
  console.log('🛠️ Updating services section...');
  
  await framer.updateContent(projectId, 'services', {
    services: crownAcquisitionsContent.services
  });
}

async function updateProcess(framer, projectId) {
  console.log('⚙️ Updating process section...');
  
  await framer.updateContent(projectId, 'process', {
    steps: crownAcquisitionsContent.process
  });
}

async function updateAbout(framer, projectId) {
  console.log('👨‍💼 Updating about section...');
  
  await framer.updateContent(projectId, 'about', crownAcquisitionsContent.about);
}

async function updateContact(framer, projectId) {
  console.log('📞 Updating contact section...');
  
  await framer.updateContent(projectId, 'contact', crownAcquisitionsContent.contact);
}

// Export for use
export {
  setupCrownAcquisitionsWebsite,
  crownAcquisitionsContent
};

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  setupCrownAcquisitionsWebsite()
    .then(() => {
      console.log('✅ Website setup completed successfully!');
      process.exit(0);
    })
    .catch(error => {
      console.error('💥 Setup failed:', error);
      process.exit(1);
    });
}