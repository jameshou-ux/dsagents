# Token Gap Report
**File:** Webapp DS — `https://www.figma.com/design/4CyZin0s6OuOEdnUwefLje`
**Node:** 321-9714
**Generated:** 2026-02-26
**Agent:** ds-token-gap-agent v1

---

## Summary

| Category | Status | Existing | Missing | Severity |
|---|---|---|---|---|
| Color — Brand Scale | ⚠️ Incomplete | 2 steps | 8 steps | High |
| Color — Neutral Scale | ⚠️ Incomplete | 4 steps | 6 steps | High |
| Color — Status / Semantic | ⚠️ Partial | 3/4 roles, missing sub-tokens | 13 tokens | High |
| Color — Functional Aliases | ⚠️ Partial | 7/19 aliases | 12 aliases | Critical |
| Spacing Scale | ❌ Absent | 0 | 13 tokens | Critical |
| Typography Scale | ⚠️ Partial | fonts present, scale incomplete | 12 tokens | High |
| Border Radius Scale | ❌ Absent | 0 | 7 tokens | High |
| Shadow / Elevation | ❌ Absent | 0 | 7 tokens | Medium |
| Z-Index Scale | ❌ Absent | 0 | 9 tokens | Medium |
| Motion / Duration | ❌ Absent | 0 | 10 tokens | Low |

**Total missing tokens: 97**
**Total existing tokens inventoried: 110 variables (of which ~40 are color, ~15 typography, ~55 duplicates/unnamed)**

---

## Category 1: Color — Brand Scale

**Anchor identified:** `Action/01Primary` = `#8034E3` → maps to `color.brand.primary.500`

**Existing brand scale steps:** 500 only (1 of 9)

**Missing steps:**

| Token | Status | Derived Value |
|---|---|---|
| color.brand.primary.50 | ❌ Missing | #f5eeff |
| color.brand.primary.100 | ❌ Missing | #e8d5fc |
| color.brand.primary.200 | ❌ Missing | #d0aaf8 |
| color.brand.primary.300 | ❌ Missing | #b87ff4 |
| color.brand.primary.400 | ❌ Missing | #9f55ec |
| color.brand.primary.500 | ✅ Present | #8034E3 (anchor) |
| color.brand.primary.600 | ❌ Missing | #6828b8 |
| color.brand.primary.700 | ❌ Missing | #4e1e8a |
| color.brand.primary.800 | ❌ Missing | #35145c |
| color.brand.primary.900 | ❌ Missing | #1c0a2e |

**Secondary blue identified:** `Blue600; Blue500` = `#007fff` → maps to `color.brand.secondary.500`

| Token | Status | Derived Value |
|---|---|---|
| color.brand.secondary.50 | ❌ Missing | #e6f3ff |
| color.brand.secondary.100 | ❌ Missing | #bfddff |
| color.brand.secondary.200 | ❌ Missing | #80bbff |
| color.brand.secondary.300 | ❌ Missing | #4d9fff |
| color.brand.secondary.400 | ❌ Missing | #1a83ff |
| color.brand.secondary.500 | ✅ Present | #007fff (anchor) |
| color.brand.secondary.600 | ❌ Missing | #0065cc |
| color.brand.secondary.700 | ❌ Missing | #004c99 |
| color.brand.secondary.800 | ❌ Missing | #003266 |
| color.brand.secondary.900 | ❌ Missing | #001933 |

---

## Category 2: Color — Neutral Scale

**Anchor identified:** `Inactive states` = `#9598AB` → maps to `color.neutral.400`

**Existing neutral steps:** 400 only (via `9598AB`, `Inactive states`)

| Token | Status | Derived Value |
|---|---|---|
| color.neutral.50 | ❌ Missing | #f7f7f9 |
| color.neutral.100 | ❌ Missing | #eaecf0 |
| color.neutral.200 | ❌ Missing | #d4d6e0 |
| color.neutral.300 | ❌ Missing | #b8bbc9 |
| color.neutral.400 | ✅ Present | #9598AB (anchor) |
| color.neutral.500 | ❌ Missing | #777a8e |
| color.neutral.600 | ❌ Missing | #5a5d70 |
| color.neutral.700 | ❌ Missing | #3f4153 |
| color.neutral.800 | ❌ Missing | #27293a |
| color.neutral.900 | ❌ Missing | #111220 |

---

## Category 3: Color — Status / Semantic

**Existing status colors found:**

| Role | Found | Token Name |
|---|---|---|
| Success | ✅ | `Success` = #4bce71, `Success background` = #4bce7133 |
| Warning | ❌ | Not present |
| Danger / Error | ✅ | `Error` = #f3636f, `Functional/Error` = #ec5d5d, `Error background` = #f3636f33 |
| Info | ✅ | Mapped from `Primary` = #007fff, `Primary background` = #007fff33 |

**Missing sub-tokens per role:**

| Missing Token | Severity | Proposed Value |
|---|---|---|
| color.status.success.default | High | #4bce71 |
| color.status.success.subtle | High | #e8fbed |
| color.status.success.text | High | #1a8c3a |
| color.status.success.border | High | #4bce71 |
| color.status.warning.default | High | #fc8c4d (inferred from `Yellow600`) |
| color.status.warning.subtle | High | #fff3ec |
| color.status.warning.text | High | #b85a1a |
| color.status.warning.border | High | #fc8c4d |
| color.status.danger.default | High | #f3636f |
| color.status.danger.subtle | High | #fdeaea |
| color.status.danger.text | High | #b81d2a |
| color.status.danger.border | High | #f3636f |
| color.status.info.default | Medium | #007fff |
| color.status.info.subtle | Medium | #e6f3ff |
| color.status.info.text | Medium | #004c99 |
| color.status.info.border | Medium | #007fff |

---

## Category 4: Color — Functional Aliases

**Existing aliases found:**

| Required Token | Status | Current Figma Name | Current Value |
|---|---|---|---|
| color.text.primary | ✅ Present | `Text/Primary`, `Text Primary` | #111d4a |
| color.text.secondary | ✅ Present | `Text/Secondary`, `Text Secondary` | #111d4a66 ⚠️ opacity |
| color.text.disabled | ❌ Missing | — | — |
| color.text.inverse | ⚠️ Partial | `Text On Color` | #ffffff |
| color.text.on-brand | ❌ Missing | — | — |
| color.text.placeholder | ✅ Present | `Text/Placeholder` | #111d4a33 ⚠️ opacity |
| color.background.primary | ✅ Present | `Bg Fill/General`, `White` | #ffffff |
| color.background.secondary | ❌ Missing | — | — |
| color.background.card | ✅ Present | `Bg Fill/Card`, `Background/Card` | #ffffff |
| color.background.overlay | ⚠️ Partial | `modal bg` | #00000066 ⚠️ opacity |
| color.background.disabled | ❌ Missing | — | — |
| color.border.default | ⚠️ Partial | `Dividers & borders` | #EAECF6 |
| color.border.strong | ❌ Missing | — | — |
| color.border.focus | ❌ Missing | — | — |
| color.border.disabled | ❌ Missing | — | — |
| color.icon.primary | ⚠️ Partial | `Fill/Fill B` | #111d4a |
| color.icon.secondary | ❌ Missing | — | — |
| color.icon.disabled | ❌ Missing | — | — |
| color.icon.on-brand | ❌ Missing | — | — |

> ⚠️ **Opacity tokens flagged:** `color.text.secondary`, `color.text.placeholder`, and `color.background.overlay` use RGBA opacity instead of solid resolved values. These will fail the accessibility check.

---

## Category 5: Spacing Scale

**Status: ❌ Entirely absent.** No spacing tokens exist in the file.

All 13 standard spacing steps are missing. See `proposed-tokens.json` for generated values.

---

## Category 6: Typography Scale

**Font families found:** SF Pro, Sora, Noto Sans (3 families in use — no unified `font.family.sans` defined)

**Font sizes found:** 10px, 12px, 14px, 16px, 24px, 32px, 48px (via inline type styles)

**Missing typography tokens:**

| Token | Status | Proposed Value |
|---|---|---|
| font.family.sans | ❌ Missing | "Noto Sans" (most used body font) |
| font.family.display | ❌ Missing | "Sora" (used for large headings) |
| font.family.ui | ❌ Missing | "SF Pro" (used for UI labels/amounts) |
| font.size.xs | ✅ Present | 10px (X-Small) |
| font.size.sm | ✅ Present | 12px (Note Small) |
| font.size.md | ✅ Present | 14px (Body Regular) |
| font.size.base | ✅ Present | 16px (Title nav) |
| font.size.lg | ❌ Missing | 18px |
| font.size.xl | ✅ Present | 24px (Amount Large) |
| font.size.2xl | ❌ Missing | 20px |
| font.size.3xl | ✅ Present | 32px (Title Max) |
| font.size.4xl | ❌ Missing | 36px |
| font.size.5xl | ✅ Present | 48px (Larger title) |
| font.weight.regular | ✅ Present | 400 |
| font.weight.medium | ✅ Present | 500 |
| font.weight.semibold | ✅ Present | 590 (non-standard — should be 600) |
| font.weight.bold | ✅ Present | 700 |
| font.lineheight.tight | ❌ Missing | 1.2 |
| font.lineheight.normal | ✅ Present (inferred) | 1.4 |
| font.lineheight.relaxed | ✅ Present (inferred) | 1.6 |
| font.tracking.tight | ❌ Missing | -0.015em |
| font.tracking.normal | ✅ Present (inferred) | 0 |
| font.tracking.wide | ❌ Missing | 0.05em |

> ⚠️ **Font weight 590 is non-standard.** No standard CSS weight maps to 590. This should be normalized to `600` (semibold).

---

## Category 7: Border Radius Scale

**Status: ❌ Entirely absent.** No radius tokens exist.

All 7 standard radius steps are missing.

---

## Category 8: Shadow / Elevation Scale

**Status: ❌ Absent.** Only a blur effect exists (`Bar overlay blur`, `Modal backdrop blur`) but no shadow tokens.

All 7 shadow steps are missing.

---

## Category 9: Z-Index Scale

**Status: ❌ Absent.** No z-index tokens exist.

---

## Category 10: Motion / Duration

**Status: ❌ Absent.** No motion tokens exist. Severity: Low.

---

## Contrast Validation

| Token Pair | Light Mode Contrast | WCAG AA Required | Status |
|---|---|---|---|
| color.text.primary (#111d4a) on color.background.primary (#ffffff) | 14.2:1 | 4.5:1 | ✅ Pass |
| color.text.secondary (#111d4a66 → resolved #888a99) on #ffffff | 3.1:1 | 4.5:1 | ❌ Fail |
| color.text.placeholder (#111d4a33 → resolved #c4c6d0) on #ffffff | 1.8:1 | 4.5:1 | ❌ Fail |
| color.status.success (#4bce71) on #ffffff | 2.8:1 | 3:1 (UI) | ❌ Fail |
| color.status.danger (#f3636f) on #ffffff | 3.2:1 | 4.5:1 | ❌ Fail |
| Light Secondary (#AEB3BE) on #ffffff | 2.9:1 | 4.5:1 | ❌ Fail |

> **5 contrast violations detected.** Resolved solid values and contrast-safe alternatives are provided in `proposed-tokens.json`.

---

## Next Steps

1. Review `proposed-tokens.json` — approve, edit, or reject each token.
2. Pass approved tokens to `ds-refactor-agent` alongside the audit report.
3. The refactor agent will sync approved tokens into Figma Variables via the Plugin.
