// USPTO API integration
// This is real code we can port from what we already built!

const USPTO_API_BASE = 'https://api.uspto.gov/api/v1'

export interface PatentApplication {
  applicationNumber: string
  title: string
  status: string
  filingDate: string
  inventors: string[]
  examiner: string
}

export interface OfficeAction {
  documentCode: string
  description: string
  date: string
  downloadUrl: string
}

// Get application status
export async function getApplication(appNumber: string, apiKey: string): Promise<PatentApplication> {
  const res = await fetch(`${USPTO_API_BASE}/patent/applications/${appNumber}`, {
    headers: { 'X-API-Key': apiKey }
  })
  const data = await res.json()
  
  const app = data.patentFileWrapperDataBag?.[0]
  const meta = app?.applicationMetaData
  
  return {
    applicationNumber: appNumber,
    title: meta?.inventionTitle || '',
    status: meta?.applicationStatusDescriptionText || '',
    filingDate: meta?.filingDate || '',
    inventors: meta?.inventorBag?.map((i: any) => i.inventorNameText) || [],
    examiner: meta?.examinerNameText || ''
  }
}

// Get documents (office actions, responses, etc)
export async function getDocuments(appNumber: string, apiKey: string): Promise<OfficeAction[]> {
  const res = await fetch(`${USPTO_API_BASE}/patent/applications/${appNumber}/documents`, {
    headers: { 'X-API-Key': apiKey }
  })
  const data = await res.json()
  
  return (data.documentBag || []).map((doc: any) => ({
    documentCode: doc.documentCode,
    description: doc.documentCodeDescriptionText,
    date: doc.officialDate,
    downloadUrl: doc.downloadOptionBag?.[0]?.downloadUrl
  }))
}

// Check for new office actions (for monitoring)
export async function checkForOfficeActions(appNumber: string, apiKey: string, since: Date) {
  const docs = await getDocuments(appNumber, apiKey)
  
  const officeActionCodes = ['CTNF', 'CTFR', 'CTRS'] // Non-final, Final, Restriction
  
  return docs.filter(doc => 
    officeActionCodes.includes(doc.documentCode) &&
    new Date(doc.date) > since
  )
}
