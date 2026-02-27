# 🛠️ Design System Refactor Plan

## 1. Overview
This refactor plan addresses the findings from the audit report `webapp-ds-audit-2026-02-25-2221.md`. The design system requires urgent architectural improvements to transition from an unorganized legacy state to an AI-ready, semantically structured token architecture.

## 2. Token Normalization Plan
The primary objective is to rebuild the token foundation using the `category.role.scale` schema.

*   **Hardcoded Value Eradication:** Replace raw hex configurations and aliases (like `9598AB` and `Deep600,White600`) with valid token paths (`color.neutral.500`, `color.brand.primary.600`).
*   **Accessibility Corrections:**
    *   Create dark mode color variable equivalents for all core tokens to ensure the system supports the `dark_mode_required` rule.
    *   Refactor opacity-based secondary layers (which fail AA contrast tests at 2.8:1 and 1.5:1) into solid resolved colors reaching a minimal 4.5:1 contrast ratio.
*   **Cleanup:** Remove identified "ghost" gradient tokens that resolve to empty strings to clean up metadata.
*   **Typography Simplification:** Migrate away from a fragmented font family system and adopt a unified, explicitly defined scale.

## 3. Component Modification Plan
Components will drastically change structure to prevent parsing errors and ease auto-generation.

*   **Structure:**
    *   Enforce Auto Layout on all interactive and container components to handle responsive design states.
    *   Resolve the identified 8 detached instances, relinking them to the core structure.
*   **Variant System Standardization:**
    *   Introduce explicit variants across all primitive interactive components: `default`, `hover`, `focus` (to solve the missing WCAG interaction states violation), `disabled`, `loading`, `error`, and `skeleton`.
*   **Semantic Renaming:**
    *   Normalize structure tags avoiding bilingual Chinese and English names. All components should move to pure English, noun-based forms (e.g., `Modal`, `Button`, `Card`). Documentation and descriptions should be handled outside the component node names.

## 4. Hierarchy Restructure
Migrate to a strict 4-layer taxonomy:

1.  **Primitive:** Base values (`color.neutral.50`)
2.  **Foundation:** Semantic usages (`color.text.secondary`)
3.  **Pattern:** Auto-layout UI primitives (`Button`, `Card`)
4.  **Template:** Abstracted page structures

## 5. Execution Summary
Following approval, the MCP token rewriter agent will synchronize the base token mapping, followed by bulk updating the interactive primitives and creating component variants.
