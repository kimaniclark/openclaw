// AI integration for patent analysis
// This is where your Claude prompting workflow would live

import Anthropic from '@anthropic-ai/sdk'

const anthropic = new Anthropic()

// Analyze an office action and suggest arguments
export async function analyzeOfficeAction(
  officeActionText: string,
  claimsText: string,
  priorArtCitations: string[]
) {
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4000,
    messages: [{
      role: 'user',
      content: `You are a patent prosecution expert. Analyze this office action and suggest the best arguments for response.

## Office Action
${officeActionText}

## Current Claims  
${claimsText}

## Prior Art Cited
${priorArtCitations.join('\n')}

Provide:
1. Summary of each rejection (102, 103, 112, etc.)
2. Strength assessment (weak/medium/strong) for each rejection
3. Recommended arguments for each rejection
4. Suggested claim amendments if needed
5. Overall strategy recommendation`
    }]
  })
  
  return response.content[0].type === 'text' ? response.content[0].text : ''
}

// Generate draft response
export async function generateOAResponse(
  analysis: string,
  clientName: string,
  applicationNumber: string,
  template: string
) {
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 8000,
    messages: [{
      role: 'user', 
      content: `Generate a formal office action response based on this analysis.

## Analysis & Arguments
${analysis}

## Application Info
Client: ${clientName}
Application: ${applicationNumber}

## Template Format
${template}

Generate the complete response document with proper legal formatting.`
    }]
  })
  
  return response.content[0].type === 'text' ? response.content[0].text : ''
}

// Generate client reporting email
export async function generateClientReport(
  clientName: string,
  applicationTitle: string,
  officeActionType: string,
  deadline: string,
  summary: string
) {
  // This is like the Morris Brown email we drafted!
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 2000,
    messages: [{
      role: 'user',
      content: `Generate a professional client email reporting a patent office action.

Client: ${clientName}
Application: ${applicationTitle}  
Office Action Type: ${officeActionType}
Response Deadline: ${deadline}
Summary: ${summary}

The email should:
- Be professional but clear
- Explain what happened in plain English
- List response options with estimated costs
- Request authorization to proceed
- Include deadline prominently`
    }]
  })
  
  return response.content[0].type === 'text' ? response.content[0].text : ''
}
