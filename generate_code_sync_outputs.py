import json
import os
from datetime import datetime

INPUT_PATH = "/Users/jameshou/Desktop/DS revamp trial/refactor-output/refactor_20260227_094500/figma-sync-tokens.json"
DARK_MODE_PATH = "/Users/jameshou/Desktop/DS revamp trial/refactor-output/refactor_20260227_094500/dark-mode-tokens.json"

# Generate timestamped output directory
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
SESSION_DIR = "code-sync"
OUT_DIR = f"/Users/jameshou/Desktop/DS revamp trial/code-sync-output/{SESSION_DIR}_{timestamp}"

os.makedirs(OUT_DIR, exist_ok=True)

# 1. Load Data
try:
    with open(INPUT_PATH, "r") as f:
        master_data = json.load(f)
    with open(DARK_MODE_PATH, "r") as f:
        dark_data = json.load(f)
except FileNotFoundError as e:
    print(f"Error loading inputs: {e}")
    exit(1)

# Ensure tokens is a list
tokens_list = master_data.get("tokens", [])
dark_list = dark_data.get("tokens", [])

# Mapping from dot notation to nested dict wrapper
def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

# ==========================================
# 2. W3C DTCG Format Converter (tokens.w3c.json)
# ==========================================
w3c_dict = {}

# Map custom simple types to standard W3C types if needed
# (color, dimension, fontFamily, fontWeight, duration, cubicBezier, shadow)
type_mapping = {
    "color": "color",
    "spacing": "dimension",
    "radius": "dimension",
    "size": "dimension",
    "fontFamily": "fontFamily",
    "fontWeight": "fontWeight",
    "lineHeight": "number", # or dimension depending on standard, using number for ratios
    "letterSpacing": "dimension",
    "shadow": "shadow",
    "duration": "duration",
    "easing": "cubicBezier",
    "z": "number"
}

for t in tokens_list:
    name_parts = t["name"].split(".")
    val = t["value"]
    
    # Determine type from either explicit type property or first path segment
    raw_type = t.get("type") or name_parts[0]
    w3c_type = type_mapping.get(raw_type, raw_type)
    
    if raw_type == "font":
        if "size" in name_parts: w3c_type = "dimension"
        if "family" in name_parts: w3c_type = "fontFamily"
        if "weight" in name_parts: w3c_type = "fontWeight"
        
    nested_set(w3c_dict, name_parts, {
        "$value": val,
        "$type": w3c_type
    })

w3c_output = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "tokens": w3c_dict
}

with open(f"{OUT_DIR}/tokens.w3c.json", "w") as f:
    json.dump(w3c_output, f, indent=4)

print("Generated W3C Tokens: tokens.w3c.json")


# ==========================================
# 3. CSS Variables Converter (variables.css)
# ==========================================
css_lines = [":root {"]

# Generate light mode (base)
for t in tokens_list:
    var_name = "--" + t["name"].replace(".", "-")
    css_lines.append(f"  {var_name}: {t['value']};")
css_lines.append("}\n")

# Generate dark mode if provided
if dark_list:
    css_lines.append("@media (prefers-color-scheme: dark) {")
    css_lines.append("  :root {")
    for dt in dark_list:
        var_name = "--" + dt["name"].replace(".", "-")
        # Only output if value exists (some might just be mapped placeholders)
        if "value" in dt:
            css_lines.append(f"    {var_name}: {dt['value']};")
    css_lines.append("  }")
    css_lines.append("}\n")
    
    # Also add standard .dark class override for Tailwind support
    css_lines.append(".dark {")
    for dt in dark_list:
        var_name = "--" + dt["name"].replace(".", "-")
        if "value" in dt:
            css_lines.append(f"  {var_name}: {dt['value']};")
    css_lines.append("}\n")

with open(f"{OUT_DIR}/variables.css", "w") as f:
    f.write("\n".join(css_lines))

print("Generated CSS Variables: variables.css")


# ==========================================
# 4. Tailwind Config Extender (tailwind.theme.js)
# ==========================================
# Extracting standard tailwind categories
tw_colors = {}
tw_spacing = {}
tw_radius = {}
tw_fonts = {}
tw_shadows = {}

# Convert "color.brand.primary.500" -> colors[brand][primary][500] = var(--...)
for t in tokens_list:
    name_parts = t["name"].split(".")
    var_ref = f"var(--{t['name'].replace('.', '-')})"
    
    if name_parts[0] == "color":
        nested_set(tw_colors, name_parts[1:], var_ref)
    elif name_parts[0] == "spacing":
        nested_set(tw_spacing, name_parts[1:], var_ref)
    elif name_parts[0] == "radius":
        nested_set(tw_radius, name_parts[1:], var_ref)
    elif name_parts[0] == "shadow":
        nested_set(tw_shadows, name_parts[1:], var_ref)
    elif name_parts[0] == "font":
        if name_parts[1] == "family":
            nested_set(tw_fonts, ["family"] + name_parts[2:], var_ref)
        elif name_parts[1] == "size":
            nested_set(tw_fonts, ["size"] + name_parts[2:], var_ref)

tw_output = f"""/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  theme: {{
    extend: {{
      colors: {json.dumps(tw_colors, indent=6)},
      spacing: {json.dumps(tw_spacing, indent=6)},
      borderRadius: {json.dumps(tw_radius, indent=6)},
      boxShadow: {json.dumps(tw_shadows, indent=6)},
      fontFamily: {json.dumps(tw_fonts.get('family', dict()), indent=6)},
      fontSize: {json.dumps(tw_fonts.get('size', dict()), indent=6)}
    }}
  }}
}}
"""

with open(f"{OUT_DIR}/tailwind.theme.js", "w") as f:
    f.write(tw_output)

print("Generated Tailwind Config: tailwind.theme.js")


# ==========================================
# 5. Figma Variables Sync Payload (figma-api-payload.json)
# ==========================================
# Figma API expects collections, modes, and variables with resolved RGBA
figma_collections = {
    "colors": {
        "modes": {"Light": "light_mode_id", "Dark": "dark_mode_id"},
        "variables": []
    },
    "numbers": {
        "modes": {"Value": "default_mode"},
        "variables": []
    },
    "strings": {
         "modes": {"Value": "default_mode"},
         "variables": []
    }
}

# Helper to convert HEX to Figma RGB/A dict structure {r, g, b, a}
def hex_to_figma_rgba(hex_str: str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join(c+c for c in hex_str)
    
    r = int(hex_str[0:2], 16) / 255.0
    g = int(hex_str[2:4], 16) / 255.0
    b = int(hex_str[4:6], 16) / 255.0
    a = 1.0
    if len(hex_str) == 8:
        a = int(hex_str[6:8], 16) / 255.0
    
    return {"r": r, "g": g, "b": b, "a": a}

# Map dark mode values for quick lookup
dark_mode_map = {dt["name"]: dt for dt in dark_list}

for t in tokens_list:
    cat = t["name"].split(".")[0]
    val = t["value"]
    
    if cat == "color" or cat == "background" or cat == "border" or cat == "text" or cat == "icon":
        # It's a color
        try:
            light_val = hex_to_figma_rgba(val)
            dark_val = hex_to_figma_rgba(dark_mode_map.get(t["name"], {}).get("value", val))
            
            figma_collections["colors"]["variables"].append({
                "name": t["name"].replace(".", "/"),
                "type": "COLOR",
                "valuesByMode": {
                    "light_mode_id": light_val,
                    "dark_mode_id": dark_val
                }
            })
        except:
             # Skip if not hex (e.g. references not resolved)
             pass
    
    elif cat in ["spacing", "radius", "z"]:
        # Extract numeric float
        try:
            num = float(str(val).replace("px", ""))
            figma_collections["numbers"]["variables"].append({
                "name": t["name"].replace(".", "/"),
                "type": "FLOAT",
                "valuesByMode": {
                    "default_mode": num
                }
            })
        except:
             pass
    else:
        # Defaults to String for Figma
        figma_collections["strings"]["variables"].append({
             "name": t["name"].replace(".", "/"),
             "type": "STRING",
             "valuesByMode": {
                 "default_mode": str(val)
             }
        })

with open(f"{OUT_DIR}/figma-api-payload.json", "w") as f:
    json.dump({"collections": figma_collections}, f, indent=4)

print("Generated Figma Variables API Payload: figma-api-payload.json")
