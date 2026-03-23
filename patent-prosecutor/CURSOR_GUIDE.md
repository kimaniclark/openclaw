# How to Build This in Cursor

## Step 1: Open the Project

```bash
# In terminal
cd ~/.openclaw/workspace/patent-prosecutor
cursor .
```

## Step 2: Install Dependencies

Press `Cmd+J` to open terminal in Cursor, then:
```bash
npm install
```

## Step 3: The Cursor Workflow

### Talk to the AI

- **Cmd+K** → Edit code with AI (highlight code, describe changes)
- **Cmd+L** → Chat about the codebase (ask questions, plan features)
- **Cmd+I** → Composer (multi-file changes, bigger features)

### Example Prompts You'd Use

**Building the docket table:**
> "Create a React component that displays a table of patent matters. Fetch data from /api/matters. Columns: docket number, client name, application number, status, deadline. Add sorting and a search filter."

**Adding USPTO monitoring:**
> "Create an API route at /api/cron/check-uspto that loops through all active matters, checks the USPTO API for new office actions, and sends an email notification if any are found. Use the functions in src/lib/uspto.ts"

**Building the OA analysis page:**
> "Create a page at /matters/[id]/office-action that shows the office action details, has a button to run AI analysis using the function in src/lib/ai.ts, and displays the suggested arguments in a nice format"

**Client authorization flow:**
> "Add a client portal where clients can log in, see their matters, and click to authorize work on pending office actions. Use Supabase auth."

## Step 4: Iterate

The magic of Cursor:

1. Describe what you want
2. AI writes the code
3. You review it (does it look right?)
4. Run it (`npm run dev`)
5. See what happens
6. Tell AI to fix/improve

You don't need to know how to write React from scratch. You need to:
- Describe features clearly
- Recognize when something looks wrong
- Test and report what happened

## Example Session

```
You: "Add a button that fetches the application status from USPTO API and displays it"

Cursor: [writes 30 lines of code]

You: [clicks the button, sees an error]

You: "I'm getting a CORS error when calling the USPTO API"

Cursor: "You need to call it from a server-side API route instead of the browser. Let me create /api/uspto/[appNumber]/route.ts..."

You: [it works now]

You: "Make the status display look nicer with colored badges for different statuses"

Cursor: [updates the UI]
```

## What You Already Have

I've created starter files:

- `src/app/page.tsx` → Dashboard skeleton
- `src/lib/uspto.ts` → USPTO API functions (working code from what we built!)
- `src/lib/ai.ts` → AI analysis functions (your Claude workflow, codified)

## Next Steps

1. Download Cursor: https://cursor.com
2. Open this folder
3. Run `npm install` then `npm run dev`
4. Start prompting!

First feature to build: Get the docket table working with real data from a database.
