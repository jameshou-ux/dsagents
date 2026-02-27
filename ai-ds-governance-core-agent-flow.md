# 🧠 AI-Native Design System Governance -- Core Agent Flow

------------------------------------------------------------------------

# 1️⃣ System Overview

This system governs a Figma-based Design System using a structured
multi-agent pipeline.

Core objective:

Slack → Audit → Refactor → Token Compile → Code Sync → Slack Feedback

The system supports Slack-triggered execution and Slack-based reporting.

------------------------------------------------------------------------

# 2️⃣ Data Source

## Figma (via MCP)

Figma is the source of truth.

It provides: - Variables (tokens) - Styles - Components - Variants -
Layout structure - Naming metadata

Only the `ds-audit-agent` reads directly from Figma via MCP.

All downstream agents operate on structured outputs from upstream
agents.

------------------------------------------------------------------------

# 3️⃣ Agent List

## 1. ds-audit-agent

**Role:** Evaluation Layer

**Responsibilities:** - Read Figma data via MCP - Load WCAG profile -
Load Token Schema profile - Analyze: - Token Integrity - Component
Integrity - Accessibility - Structure & Semantics - Variant Coverage -
Naming Consistency - Compute weighted scores - Output structured audit
report and consolidated JSON

**Input:** - Figma file ID - WCAG profile - Token schema

------------------------------------------------------------------------

## 2. ds-refactor-agent

**Role:** Remediation Planning Layer

**Responsibilities:** - Read audit output - Prioritize issues - Generate
structured refactor plan - Define: - Token replacement suggestions -
Naming normalization rules - Missing state/variant additions - Component
structure corrections - Produce patch plan (not necessarily apply
changes directly)

------------------------------------------------------------------------

## 3. token-compiler-agent

**Role:** Token Standardization Layer

**Responsibilities:** - Read current token structure - Apply refactor
plan - Validate token schema compliance - Compile tokens into
standardized format - Output machine-consumable token artifacts

Optional outputs: - CSS Variables - Tailwind Config - Theme Object

------------------------------------------------------------------------

## 4. code-sync-agent

**Role:** Design-to-Code Alignment Layer

**Responsibilities:** - Sync compiled tokens to front-end codebase - Map
tokens to component library - Ensure consistency between design and
implementation - Detect design--code drift

------------------------------------------------------------------------

## 5. slack-orchestrator-agent

**Role:** Trigger & Notification Layer

**Responsibilities:** - Listen for Slack commands - Parse user intent -
Trigger appropriate agent flow - Post summarized results back to Slack -
Attach: - Audit summary - Key issues - Dashboard link - Refactor
recommendations (if requested)

**Example Slack Commands:**

/audit-ds `<figma_link>`{=html}\
/refactor-ds\
/sync-tokens\
/ds-status

------------------------------------------------------------------------

# 4️⃣ Agent Execution Order

## Core Governance Flow

**Phase 1: Analysis (Parallel)**
- Step 1A → `ds-token-gap-agent` → outputs to `0_gap-report/gap_YYYYMMDD_HHMMSS/`
- Step 1B → `ds-audit-agent` → outputs to `1_audit-report/audit_YYYYMMDD_HHMMSS/`

🔒 **Human Review & Modification** — designer previews gap proposals + audit report, makes edits as needed

**Phase 2: Consolidation & Remediation**
- Step 2 → `ds-refactor-agent` → outputs to `3_refactor-output/refactor_YYYYMMDD_HHMMSS/`

🔒 **Human Confirmation** — designer reviews refactor plan before code sync

**Phase 3: Implementation**
- Step 3 → `code-sync-agent` → outputs to `4_code-sync-output/sync_YYYYMMDD_HHMMSS/`

------------------------------------------------------------------------

# 5️⃣ Slack-Orchestrated Flow

Slack Command
↓
slack-orchestrator-agent
↓
[ds-audit-agent  +  ds-token-gap-agent]   ← Phase 1 (Parallel)
↓
🔒 Human Review & Modification
↓
ds-refactor-agent                          ← Phase 2
↓
🔒 Human Confirmation
↓
code-sync-agent                            ← Phase 3
↓
Slack Feedback + Dashboard Link

------------------------------------------------------------------------

# 6️⃣ Final Pipeline Summary

Slack
↓
Phase 1: Analysis (Audit + Token Gaps)  — parallel
↓
🔒 Human Review & Modification
↓
Phase 2: Refactor (Merge to figma-sync-tokens.json)
↓
🔒 Human Confirmation
↓
Phase 3: Code Sync
↓
Slack Notification
