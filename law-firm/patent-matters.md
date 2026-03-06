# Patent Matters Reference

Last updated: 2026-03-06

## Active Client Matters (Kimani's Cases)

### Clipboard Nation
| Matter | App # | Title | Status | Deadline |
|--------|-------|-------|--------|----------|
| 3021-0002 | 15/636,654 | METHOD AND SYSTEM FOR GENERATING AND MANAGING PLAYS IN AN ELECTRONIC FORUM | **Issued** | - |
| 3021-0003 | 18/534,782 | METHOD AND SYSTEM FOR GENERATING AND MANAGING PLAYS IN AN ELECTRONIC FORUM | Non-Final OA | Mar 20, 2026 |

**Client Contact:** Lu Molenje
**Deposit Due:** $3,500

---

### A Good Walk (Morris Brown)
| Matter | App # | Title | Status | Deadline |
|--------|-------|-------|--------|----------|
| 1002-0002 | 18/325,585 | Method and System For Golf Content Displayed on a Computing Device | **Final Rejection** | Mar 21, 2026 |

**Client Contact:** Morris Brown
**Deposit Due:** $3,500

---

### Archivox, Inc.
| Matter | App # | Title | Status | Deadline |
|--------|-------|-------|--------|----------|
| 1013-0002-PRO | 63/820,629 | METHOD AND SYSTEM FOR ADVANCED DIGITAL TWIN ARCHITECTURE FOR EXPERT INSIGHTS PLATFORM | Pending (Missing Parts) | Jan 16, 2026 |

**Client Contact:** Chris Cresswell
**Deposit Due:** $12,000

---

### Fifth Weapon
| Matter | App # | Title | Status | Deadline |
|--------|-------|-------|--------|----------|
| (Provisional) | TBD | TBD | Pending | TBD |

**Client Contact:** Roop Sood
**Deposit Due:** $2,500

---

### Everlaw, Inc.
| Matter | App # | Title | Status |
|--------|-------|-------|--------|
| 1005-0002 | 18/161,233 | DISTRIBUTED EMAIL THREADING | Pending |
| 1005-0003 | 17/978,552 | DOCUMENT DIFFERENCE VIEWING AND NAVIGATION | Published |
| 1005-0004 | 18/061,037 | PROVIDING OVERLAPPING TIME REDACTIONS IN MEDIA ITEMS | Pending |
| 1005-0006 | 17/548,377 | SWEEP ALGORITHM FOR OUTPUT OF GRAPHICAL OBJECTS | Pending |
| 1005-0007 | PCT/US22/52075 | SWEEP ALGORITHM FOR OUTPUT OF GRAPHICAL OBJECTS | PCT Pending |
| 1005-0008 | 17/544,771 | ALPHA SHAPE APPROXIMATION OF DATA POINTS | Pending |
| 1005-0009 | PCT/US22/80890 | ALPHA SHAPE APPROXIMATION OF DATA POINTS | PCT Pending |

---

### Richard Giambruno II
| Matter | App # | Title | Status | Deadline |
|--------|-------|-------|--------|----------|
| 1009-0002 | 18/776,642 | SYSTEMS AND METHODS FOR DETECTING LAW ENFORCEMENT VEHICLES | Published | Jul 18, 2025 (Foreign App) |

---

### Elissa Alden
| Matter | App # | Title | Status |
|--------|-------|-------|--------|
| 1012-0002-PRO | 63/730,503 | METHOD AND SYSTEM FOR PERSONALIZED MENTAL FITNESS PROGRAMS AND TRACKING | Expired |

---

## USPTO API Access

- **API Key:** Stored in `credentials.json` under `usptoODP`
- **Endpoints:**
  - `GET /api/v1/patent/applications/{appNum}` — Full application data
  - `GET /api/v1/patent/applications/{appNum}/documents` — Document list
  - `GET /api/v1/patent/applications/{appNum}/transactions` — Transaction history
- **Rate Limits:** 1.2M document retrievals/week, 5M metadata retrievals/week

## Data Sources

- **AppColl Docket:** `appcoll_docket_2026-03-01.csv` (from Black Hills IP email)
- **USPTO API:** Real-time via api.uspto.gov
- **Law Firm Email:** kimani@kiklisclark.com (monitored for USPTO correspondence)
