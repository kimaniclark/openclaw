# Health Data API Research

**Date:** 2026-02-03  
**Researched:** LifeForce Health and Function Health APIs

---

## Findings

### LifeForce Health
- **Website:** https://www.mylifeforce.com
- **API Availability:** ❌ None found
- **Developer Documentation:** ❌ None found
- **Checked URLs:**
  - /api → Loading page only
  - /developers → Loading page only

### Function Health
- **Website:** https://www.functionhealth.com
- **API Availability:** ❌ None found
- **Developer Documentation:** ❌ None found
- **Checked URLs:**
  - /api → 404
  - /developers → 404

---

## Conclusion

**Neither platform offers a public API.** This is typical for health data platforms due to:
- HIPAA compliance requirements
- Patient privacy protection
- Liability concerns
- Business model (keeping data within their ecosystem)

---

## Data Integration Alternatives

Since no APIs exist, health data integration options:

1. **Manual entry** (current approach)
   - Weekly updates to dashboard
   - Data from Withings app + LifeForce portal
   
2. **Withings API** (for body composition + sleep)
   - Withings has a developer API: https://developer.withings.com
   - Can pull body fat, weight, sleep data automatically
   - Requires OAuth setup
   
3. **Screen scraping** (fragile, not recommended)
   - Could automate LifeForce dashboard screenshots
   - OCR to extract values
   - High maintenance, breaks when UI changes

4. **PDF parsing** (one-time imports)
   - Parse LabCorp/LifeForce PDF reports
   - Extract historical data for trends
   - Manual download required for each test

---

## Recommendation

**For MVP:** Manual weekly updates (already doing this)

**For v2:** Integrate Withings API for automatic body composition + sleep tracking

**For Life Concierge clients:** 
- Most won't have organized health data to import
- Manual entry is acceptable (weekly 5-minute update)
- Focus on making data entry fast/easy, not automation
