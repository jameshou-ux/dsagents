---
description: Run a full DS Audit Agent round — produces both a .md report and a matching interactive .html report under audit-report/
---

# DS Audit Workflow

This workflow governs a complete end-to-end audit run using the `ds-audit-agent` skill.
It ensures that every audit produces two output files with matching names:
- `audit-report/{slug}-audit-{YYYY-MM-DD-HHMM}.md` — structured markdown report
- `audit-report/{slug}-audit-{YYYY-MM-DD-HHMM}.html` — interactive visual report

---

## Step 1 — Collect Inputs

Ask the user for the following if not already provided in the prompt:

1. **Figma URL or Node ID** — the design system file to audit  
   _(or)_ **Local JSON path** — path to a local token file (e.g. `design-tokens.json`)
2. **Project slug** — short kebab-case identifier for the report filename  
   Example: `webapp-ds`, `mobile-tokens`, `brand-v2`

If the project slug is not given, derive it from the Figma file name or JSON filename.

---

## Step 2 — Run the Audit

Adopt the persona and rules defined in `.agent/skills/ds-audit-agent/SKILL.md`.

Execute the full 8-step audit workflow exactly as specified in the skill:

1. Ingest tokens and components from the provided data source
2. Analyze Token Integrity (using `ai-token-schema-simple-v1.json`)
3. Analyze Component Integrity
4. Evaluate Accessibility (using `wcag-profile-customer-v1.json`)
5. Check Structure, Semantics & Naming
6. Determine Variant Coverage
7. Compute dimension scores and overall + AI readiness scores
8. Finalize all findings, critical issues, and roadmap items

Hold the complete audit results in memory as a structured data object before writing any files.

---

## Step 3 — Determine Output Filenames

Compute the output filenames using this convention:

```
slug   = {project-slug}               # e.g. "webapp-ds"
datetime = {YYYY-MM-DD-HHMM}          # e.g. "2026-02-25-1150" (current date and time)
base   = {slug}-audit-{datetime}      # e.g. "webapp-ds-audit-2026-02-25-1150"
mdFile  = audit-report/{base}.md
htmlFile = audit-report/{base}.html
```

---

## Step 4 — Write the Markdown Report

Save the full structured markdown audit report to `{mdFile}`.

The report must contain all 8 required sections as defined in `SKILL.md`:
1. Metadata (JSON block)
2. Executive Summary
3. Dimension Scores (JSON block)
4. Detailed Findings (one subsection per dimension)
5. Critical Issues (JSON block)
6. Systemic Risks
7. Optimization Roadmap (JSON block)
8. AI Readiness Evaluation (JSON block)

---

## Step 5 — Build the AUDIT_DATA Object

From the audit results, construct a JavaScript object conforming exactly to the
`AUDIT_DATA` schema used by the HTML template. The schema is defined inside
`.agent/skills/ds-audit-agent/templates/audit-report-template.html`
between the comments `① DATA LAYER` and `② i18n STRINGS`.

The object must include:

```javascript
const AUDIT_DATA = {
  metadata: {
    project_name,      // Full display name of the design system
    file_id,           // Figma file ID or JSON filename
    figma_url,         // Full Figma URL (or "" if local JSON)
    audit_timestamp,   // ISO 8601 timestamp of audit run
    auditor,           // "ds-audit-agent v1"
    wcag_profile,      // from wcag-profile-customer-v1.json
    wcag_target,       // "AA" or "AAA"
    theme_modes_checked, // array e.g. ["light","dark"]
    dark_mode_required,  // boolean
    token_schema_version // from ai-token-schema-simple-v1.json
  },
  summary: {
    overall_score,        // integer 0-100
    ai_readiness_score,   // integer 0-100
    risk_level,           // "High" | "Medium" | "Low"
    text,                 // English prose summary
    text_zh               // Chinese prose summary (translate from text)
  },
  dimensions: [
    // 6 entries, one per dimension. Each must include:
    // key, label, label_zh, score (int), weight (string e.g. "25%"),
    // color ("#ef4444"|"#f59e0b"|"#22c55e"),
    // metrics: [{ label, label_zh, value }]
  ],
  critical_issues: [
    // Each: { area, area_zh, issue, issue_zh, impact, impact_zh, severity }
  ],
  roadmap: [
    // Each: { priority, area, area_zh, action, action_zh, expected_impact, expected_impact_zh }
  ],
  ai_readiness: {
    score,                             // integer
    overall_score_used,
    hard_code_penalty_applied,         // boolean
    semantic_instability_detected,     // boolean
    prompt_generation_stability_estimate, // integer percent
    penalties: [
      // Each: { condition, condition_zh, deduction (negative integer) }
    ],
    notes,     // English string
    notes_zh   // Chinese string
  }
};
```

**Important:** All `_zh` fields must be provided. Translate from English using accurate
design terminology in Simplified Chinese.

---

## Step 6 — Generate the HTML Report

1. Read the full contents of `.agent/skills/ds-audit-agent/templates/audit-report-template.html`
2. Locate the `AUDIT_DATA` constant — it begins at the line `const AUDIT_DATA = {` and ends
   at the line `};` immediately before the comment `② i18n STRINGS`
3. Replace that entire `const AUDIT_DATA = { ... };` block with the new `AUDIT_DATA` object
   built in Step 5
4. Write the resulting HTML string to `{htmlFile}`
5. Do NOT modify any other part of the template — only the `AUDIT_DATA` block changes

---

## Step 7 — Confirm Outputs

Report back to the user with a summary:

```
✅ Audit complete for: {project_name}

📄 Markdown report → audit-report/{base}.md
🌐 HTML report     → audit-report/{base}.html

Overall Score:    {overall_score}/100
AI Readiness:     {ai_readiness_score}/100
Risk Level:       {risk_level}
```

If any file write fails, report the error and retry once.

---

## Naming Rules (Summary)

| Variable    | Format                | Example                          |
|-------------|----------------------|----------------------------------|
| `slug`      | kebab-case           | `webapp-ds`                      |
| `date`      | `YYYY-MM-DD`         | `2026-02-25`                     |
| `base`      | `{slug}-audit-{date}`| `webapp-ds-audit-2026-02-25`     |
| `.md` path  | `audit-report/{base}.md`  | `audit-report/webapp-ds-audit-2026-02-25.md`  |
| `.html` path| `audit-report/{base}.html`| `audit-report/webapp-ds-audit-2026-02-25.html`|

---

## Dependencies

| File | Role |
|------|------|
| `.agent/skills/ds-audit-agent/SKILL.md` | Audit logic, scoring model, output structure |
| `.agent/skills/ds-audit-agent/wcag-profile-customer-v1.json` | Accessibility rules |
| `.agent/skills/ds-audit-agent/ai-token-schema-simple-v1.json` | Token naming rules |
| `.agent/skills/ds-audit-agent/templates/audit-report-template.html` | HTML output template |
| `audit-report/` | Output directory for all generated reports |
