import json
import os
import re

DESIGN_TOKENS_PATH = "/Users/jameshou/Desktop/DS revamp trial/design-tokens.json"
PROPOSED_TOKENS_PATH = "/Users/jameshou/Desktop/DS revamp trial/token-gap-outputs/proposed-tokens.json"
OUT_DIR = "/Users/jameshou/Desktop/DS revamp trial/refactor-outputs/webapp/"

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 6:
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    elif len(hex_str) == 8:
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4, 6))
    return (0,0,0)

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def overlay_on_white(r, g, b, a):
    # a is 0 to 255
    alpha = a / 255.0
    out_r = int(r * alpha + 255 * (1 - alpha))
    out_g = int(g * alpha + 255 * (1 - alpha))
    out_b = int(b * alpha + 255 * (1 - alpha))
    return rgb_to_hex(out_r, out_g, out_b)

with open(DESIGN_TOKENS_PATH, "r") as f:
    design_tokens = json.load(f)

with open(PROPOSED_TOKENS_PATH, "r") as f:
    proposed_data = json.load(f)

proposed_tokens = proposed_data.get("tokens", {})

# 1. Generate Accessibility Fixes (Opacity to Solid)
accessibility_fixes = []
for k, v in design_tokens.get("colors", {}).items():
    if len(v) == 9 and v.startswith('#'):
        rgba = hex_to_rgb(v)
        solid_hex = overlay_on_white(rgba[0], rgba[1], rgba[2], rgba[3])
        accessibility_fixes.append({
            "legacy_name": k,
            "legacy_value": v,
            "resolved_solid_hex": solid_hex,
            "action": "Converted opacity hex to solid hex based on white background"
        })

with open(os.path.join(OUT_DIR, "accessibility-fixes.json"), "w") as f:
    json.dump({"fixes": accessibility_fixes}, f, indent=4)

# 2. Generate Dark Mode Tokens
# We will invert light scales
dark_mode_tokens = {}
for category, roles in proposed_tokens.get("color", {}).items():
    dark_mode_tokens[category] = {}
    for role, scales in roles.items():
        dark_mode_tokens[category][role] = {}
        # Simple inversion for scales like 50->900, 100->800, etc.
        if "500" in scales: 
            for scale_val, data in scales.items():
                if scale_val.isdigit():
                    num = int(scale_val)
                    inverted_num = 950 - num if num != 50 else 900
                    if inverted_num == 450: inverted_num = 500
                    # Just map it to the string value of the new inverted key if it existed, otherwise fallback
                    legacy_val = scales.get(str(inverted_num), data)["value"]
                    dark_mode_tokens[category][role][scale_val] = {
                        "value": legacy_val,
                        "method": f"Inverted from light mode {inverted_num}"
                    }
                else:
                    dark_mode_tokens[category][role][scale_val] = {
                        "value": data["value"],
                        "method": "Direct passthrough for non-numeric scales (requires manual tuning)"
                    }

with open(os.path.join(OUT_DIR, "dark-mode-tokens.json"), "w") as f:
    json.dump({"color": dark_mode_tokens}, f, indent=4)

# 3. Variant Gaps
variant_gaps = [
    {
        "component": "Button",
        "missing_states": ["focus", "loading", "error", "skeleton"],
        "recommended_action": "Add variant property 'state' with values: focus, loading, error, skeleton"
    },
    {
        "component": "Input",
        "missing_states": ["focus", "error", "disabled"],
        "recommended_action": "Add variant property 'state' with values: focus, error, disabled"
    },
    {
        "component": "Card",
        "missing_states": ["hover", "focus", "skeleton"],
        "recommended_action": "Add variant property 'state' with values: hover, focus, skeleton for clickable cards"
    }
]

with open(os.path.join(OUT_DIR, "variant-gaps.json"), "w") as f:
    json.dump(variant_gaps, f, indent=4)

# 4. Auto Layout Fixes
auto_layout_fixes = [
    {
        "target": "Modal Container",
        "issue": "Detached instance and absolute positioning",
        "fix": {
            "layoutMode": "VERTICAL",
            "primaryAxisAlignItems": "MIN",
            "counterAxisAlignItems": "MIN",
            "itemSpacing": "spacing.4"
        }
    },
    {
        "target": "Page Header",
        "issue": "Missing auto-layout",
        "fix": {
            "layoutMode": "HORIZONTAL",
            "primaryAxisAlignItems": "SPACE_BETWEEN",
            "counterAxisAlignItems": "CENTER",
            "itemSpacing": "spacing.5"
        }
    }
]

with open(os.path.join(OUT_DIR, "auto-layout-fixes.json"), "w") as f:
    json.dump(auto_layout_fixes, f, indent=4)

def flatten_dict(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict) and 'value' not in v:
            items.extend(flatten_dict(v, new_key))
        elif isinstance(v, dict) and 'value' in v:
            items.append((new_key, v['value']))
    return items

flat_sync_tokens = []
for k, v in flatten_dict(proposed_tokens):
    # k might be 'color.brand.primary.50'
    node_type = "color" if k.startswith("color") else "number" if k.startswith(("spacing", "radius", "z", "shadow", "motion.duration")) else "string"
    if k.startswith("font"): node_type = "typography"
    flat_sync_tokens.append({
        "name": k,
        "value": v,
        "type": node_type
    })

figma_sync_payload = {
    "schema": "ai_token_schema_simple_v1",
    "status": "ready_for_figma_sync",
    "tokens": flat_sync_tokens
}

with open(os.path.join(OUT_DIR, "figma-sync-tokens.json"), "w") as f:
    json.dump(figma_sync_payload, f, indent=4)

print("Generated all files successfully.")
