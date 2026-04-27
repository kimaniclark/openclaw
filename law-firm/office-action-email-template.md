# Office Action Reporting Email Template

## When to Use
- When USPTO office action is received (CTNF, Final, etc.)
- Send notification to client and co-counsel immediately
- Ask Kimani if reporting email should be prepared when OA detected

## Email Template

**Subject:** USPTO [Office Action Type] Received - Docket [DOCKET-NUMBER] ([Brief Case Description])

**From:** assistant@kiklisclark.com (Tron)  
**To:** [CLIENT_EMAIL]  
**CC:** [CO_COUNSEL_EMAIL], kimani@kiklisclark.com  

---

Dear [CLIENT_NAME] and [CO_COUNSEL_NAME],

I hope this email finds you well. I am writing to inform you that we received a [Office Action Type] from the USPTO on [MAILING_DATE] regarding your patent application.

**Application Details:**
- **Application Number:** [APP_NUMBER]
- **Attorney Docket:** [DOCKET_NUMBER]  
- **Title:** [APPLICATION_TITLE]
- **Office Action Type:** [OA_TYPE]
- **Mailing Date:** [MAILING_DATE]
- **Response Deadline:** [DEADLINE_DATE] ([MONTHS] months from mailing date)

The office action and cited references are attached to this email. Please let us know if you would like us to prepare a response to the office action. If we do not prepare a response, the application will go abandoned.

We will send a request for a deposit in a separate email.

Please feel free to reach out with any questions or to discuss next steps.

Best regards,

**Tron**  
Assistant to Kimani Clark, Esq.  
Kiklis Clark, P.L.L.C.  
📧 assistant@kiklisclark.com  
📞 301-674-1098  
🗓️ Schedule a call: cal.link/kimaniclark

---

## Variables to Replace

| Variable | Example | Source |
|----------|---------|---------|
| `[Office Action Type]` | "Non-Final Office Action" | Document type |
| `[DOCKET-NUMBER]` | "1009-0002" | Internal docket |
| `[Brief Case Description]` | "Law Enforcement Vehicle Detection" | Shortened title |
| `[CLIENT_EMAIL]` | "ricci@figliotech.com" | Client contact info |
| `[CO_COUNSEL_EMAIL]` | "sgiambruno@comcast.net" | Co-counsel info |
| `[CLIENT_NAME]` | "Ricci" | First name |
| `[CO_COUNSEL_NAME]` | "Scot" | First name |
| `[MAILING_DATE]` | "April 21, 2026" | USPTO mailing date |
| `[APP_NUMBER]` | "18/776,642" | USPTO app number |
| `[APPLICATION_TITLE]` | "Systems and Methods for Detecting Law Enforcement Vehicles" | Full title |
| `[OA_TYPE]` | "Non-Final Office Action" | Action type |
| `[DEADLINE_DATE]` | "July 21, 2026" | Response deadline |
| `[MONTHS]` | "3" | Response period |

## Contact Information (Keep Updated)

### Richard Giambruno II / Figlio Tech
- **Client:** ricci@figliotech.com
- **Co-counsel:** sgiambruno@comcast.net (Scot Giambruno)

### Clipboard Nation
- **Client:** Lumo@clipboardnation.com (Lu)

### A Good Walk
- **Client:** [UPDATE NEEDED]

## Workflow
1. **Office Action detected** → Alert in #law-company
2. **Ask Kimani:** "Should I prepare the reporting email for [CLIENT]?"
3. **If yes:** Customize template with case details
4. **Attach:** Office action + cited references PDFs
5. **Send** via Gmail API using assistant@kiklisclark.com
6. **Follow up:** Separate deposit request email if needed

## ⚠️ IMPORTANT: Gmail Alias Sending
- **Must send FROM:** assistant@kiklisclark.com (not kimani@kiklisclark.com)
- **CC:** kimani@kiklisclark.com 
- **Issue:** Gmail API raw email method may not properly use alias - need to research proper alias sending method
- **Current problem:** Email appears from "Kimani Clark" instead of "Tron/Assistant"

## Attachments Needed
- Office action document (CTNF, Final, etc.)
- References cited document (Form 892)
- All cited reference PDFs (patents, publications, etc.)