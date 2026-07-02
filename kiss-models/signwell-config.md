# KiSS Models — SignWell Configuration

## API Access
- **API Key:** stored in `credentials.json` → `signwell.apiKey`
- **Account:** KiSS Models (Light plan)
- **Owner email:** info@kissmodelmanagement.com

## Templates

### Non Exclusive Modeling Contract
- **Template ID:** `3e941446-9e62-47e2-b57a-8a3d9b2f0712`
- **Pages:** 8
- **Signers:** Victoria Kulicheva only
- **Use for:** Standard non-exclusive contracts

### Mother Agency - Adults
- **Template ID:** `dd6463e3-3b42-4f35-b3a3-ebe446eeaccc`
- **Pages:** 7
- **Signers:** Victoria Kulicheva + Model
- **Model fields:**
  - Name_1 (autofill_name, page 1)
  - TextField_1 (text, page 1) — model's details
  - DateSigned_1 (autofill_date_signed, page 1)
  - Signature_2 (signature, page 7)
- **Victoria fields:**
  - Signature_1 (signature, page 7)
  - DateField_1 (date, page 7)

## Post-Meeting Email Template (updated July 1, 2026)
Default contract type: **Non-exclusive contract** (change per case)

```
Hi [Name],

Victoria mentioned she had a great conversation with you.

We'd like to offer you a [Non-exclusive contract / Mother Agency Agreement / Exclusive contract]. In order to proceed, please provide the following:

Full Name:

Once we receive this, we'll send over the contract for your review. Please take your time to go through it, and feel free to reach out if you have any questions or need clarification.

You can contact Victoria directly at victoria@kissmodelmanagement.com, and for urgent matters, she can be reached by text at (310) 422-6802.

Best,

Maria Mara
Head Booker
```

**Sending from:** info@kissmodelmanagement.com (Gmail OAuth — `gmailKissModels` in credentials)
**Signature from:** Maria Mara, Head Booker
**Font:** Sans-serif, normal weight (plain text / default sans-serif — Kimani approved this style)

## Automated Flow
1. Model meets with Victoria
2. We send post-meeting email from info@kissmodelmanagement.com
3. Model replies with full name
4. Automatically create & send SignWell contract (template based on contract type)
5. Alert #ai-model-applications when contract sent
