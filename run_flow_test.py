import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def extract_figma_parts(figma_url: str):
    file_match = re.search(r"/design/([^/]+)/", figma_url)
    file_id = file_match.group(1) if file_match else "unknown-file"
    query = parse_qs(urlparse(figma_url).query)
    node_id = query.get("node-id", [""])[0]
    return file_id, node_id


def first_hex(colors: dict, fallback="#007fff"):
    for v in colors.values():
        if isinstance(v, str) and re.match(r"^#[0-9a-fA-F]{6}$", v):
            return v.lower()
    return fallback


def build_proposed_tokens(design_tokens: dict):
    colors = design_tokens.get("colors", {})
    typo = design_tokens.get("typography", {})
    primary = colors.get("Primary") or colors.get("Action/01Primary") or first_hex(colors)

    family = "SF Pro"
    if typo:
        first_typo = next(iter(typo.values()))
        family = first_typo.get("family", family)

    return {
        "tokens": {
            "color": {
                "brand": {
                    "primary": {
                        "50": {"value": "#eff6ff"},
                        "100": {"value": "#dbeafe"},
                        "200": {"value": "#bfdbfe"},
                        "300": {"value": "#93c5fd"},
                        "400": {"value": "#60a5fa"},
                        "500": {"value": primary},
                        "600": {"value": "#2563eb"},
                        "700": {"value": "#1d4ed8"},
                        "800": {"value": "#1e40af"},
                        "900": {"value": "#1e3a8a"},
                    }
                },
                "neutral": {
                    "50": {"value": "#f8fafc"},
                    "100": {"value": "#f1f5f9"},
                    "200": {"value": "#e2e8f0"},
                    "300": {"value": "#cbd5e1"},
                    "400": {"value": "#94a3b8"},
                    "500": {"value": "#64748b"},
                    "600": {"value": "#475569"},
                    "700": {"value": "#334155"},
                    "800": {"value": "#1e293b"},
                    "900": {"value": "#0f172a"},
                },
            },
            "background": {
                "primary": {"value": colors.get("Background/General", "#ffffff")},
                "surface": {"value": colors.get("Background/Card", "#ffffff")},
            },
            "text": {
                "primary": {"value": colors.get("Text/Primary", "#111d4a")},
                "secondary": {"value": colors.get("Text/Secondary", "#64748b")},
                "oncolor": {"value": colors.get("Text On Color", "#ffffff")},
            },
            "border": {
                "default": {"value": colors.get("Dividers & borders", "#e2e8f0")}
            },
            "spacing": {
                "0": {"value": "0px"},
                "1": {"value": "4px"},
                "2": {"value": "8px"},
                "3": {"value": "12px"},
                "4": {"value": "16px"},
                "5": {"value": "20px"},
                "6": {"value": "24px"},
                "8": {"value": "32px"},
                "10": {"value": "40px"},
                "12": {"value": "48px"},
            },
            "radius": {
                "none": {"value": "0px"},
                "sm": {"value": "4px"},
                "md": {"value": "8px"},
                "lg": {"value": "12px"},
                "xl": {"value": "16px"},
                "full": {"value": "9999px"},
            },
            "font": {
                "family": {
                    "base": {"value": family},
                },
                "size": {
                    "sm": {"value": "14px"},
                    "base": {"value": "16px"},
                    "lg": {"value": "18px"},
                    "xl": {"value": "20px"},
                },
                "weight": {
                    "regular": {"value": "400"},
                    "medium": {"value": "500"},
                    "bold": {"value": "700"},
                },
            },
            "shadow": {
                "sm": {"value": "0 1px 2px rgba(0,0,0,0.08)"},
                "md": {"value": "0 4px 8px rgba(0,0,0,0.12)"},
            },
            "z": {
                "base": {"value": "0"},
                "dropdown": {"value": "1000"},
                "modal": {"value": "1300"},
                "tooltip": {"value": "1500"},
            },
            "motion": {
                "duration": {
                    "fast": {"value": "120ms"},
                    "normal": {"value": "200ms"},
                    "slow": {"value": "320ms"},
                },
                "easing": {
                    "standard": {"value": "cubic-bezier(0.2, 0, 0, 1)"}
                },
            },
            "icon": {
                "primary": {"value": colors.get("Stoke/Icon stroke", "#111d4a")}
            },
        }
    }


def write_audit_outputs(audit_dir: Path, figma_url: str, file_id: str, node_id: str, design_tokens: dict):
    colors_count = len(design_tokens.get("colors", {}))
    typo_count = len(design_tokens.get("typography", {}))
    overall_score = 62
    ai_readiness = 58

    audit_json = {
        "metadata": {
            "project_name": "Webapp Design System",
            "file_id": file_id,
            "node_id": node_id,
            "figma_url": figma_url,
            "audit_timestamp": datetime.now().isoformat(),
            "auditor": "ds-audit-agent v1 (local-smoke)",
            "data_source": "local design-tokens.json fallback",
        },
        "summary": {
            "overall_score": overall_score,
            "ai_readiness_score": ai_readiness,
            "risk_level": "Medium",
        },
        "metrics": {
            "color_tokens": colors_count,
            "typography_tokens": typo_count,
        },
    }

    audit_md = f"""# DS Audit Report (Smoke Test)\n\n- Project: Webapp Design System\n- Figma URL: {figma_url}\n- File ID: {file_id}\n- Node ID: {node_id}\n- Source: local `design-tokens.json` fallback\n\n## Scores\n- Overall Score: {overall_score}/100\n- AI Readiness: {ai_readiness}/100\n- Risk Level: Medium\n\n## Token Counts\n- Color tokens: {colors_count}\n- Typography tokens: {typo_count}\n"""

    audit_html = f"""<!doctype html><html><head><meta charset='utf-8'><title>Audit Smoke</title></head><body><h1>DS Audit Report (Smoke Test)</h1><p>Figma URL: <a href='{figma_url}'>{figma_url}</a></p><p>File ID: {file_id}</p><p>Node ID: {node_id}</p><p>Overall: {overall_score}/100</p><p>AI Readiness: {ai_readiness}/100</p></body></html>"""

    (audit_dir / "audit-report.json").write_text(json.dumps(audit_json, indent=2))
    (audit_dir / "audit-report.md").write_text(audit_md)
    (audit_dir / "audit-report.html").write_text(audit_html)


def main():
    parser = argparse.ArgumentParser(description="Run DS flow smoke test with a Figma URL.")
    parser.add_argument("--figma-url", required=True, help="Figma file/design URL")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_id, node_id = extract_figma_parts(args.figma_url)

    with (base_dir / "design-tokens.json").open("r") as f:
        design_tokens = json.load(f)

    gap_dir = base_dir / "0_gap-report" / f"gap_{timestamp}"
    audit_dir = base_dir / "1_audit-report" / f"audit_{timestamp}"
    refactor_dir = base_dir / "3_refactor-output" / f"refactor_{timestamp}"
    sync_dir = base_dir / "4_code-sync-output" / f"sync_{timestamp}"

    gap_dir.mkdir(parents=True, exist_ok=True)
    audit_dir.mkdir(parents=True, exist_ok=True)

    proposed = build_proposed_tokens(design_tokens)
    (gap_dir / "proposed-tokens.json").write_text(json.dumps(proposed, indent=2))

    gap_report_json = {
        "figma_url": args.figma_url,
        "file_id": file_id,
        "node_id": node_id,
        "source": "local design-tokens.json fallback",
        "status": "smoke_test_generated",
    }
    (gap_dir / "token-gap-report.json").write_text(json.dumps(gap_report_json, indent=2))
    (gap_dir / "token-gap-log.json").write_text(json.dumps({"events": ["generated_proposed_tokens"]}, indent=2))
    (gap_dir / "token-gap-report.md").write_text(
        "# Token Gap Report (Smoke Test)\n\n"
        f"- Figma URL: {args.figma_url}\n"
        f"- File ID: {file_id}\n"
        f"- Node ID: {node_id}\n"
        "- Source: local design-tokens.json fallback\n"
    )

    write_audit_outputs(audit_dir, args.figma_url, file_id, node_id, design_tokens)

    subprocess.run(
        [
            "python3",
            str(base_dir / "generate_refactor_outputs.py"),
            "--design-tokens",
            str(base_dir / "design-tokens.json"),
            "--proposed",
            str(gap_dir / "proposed-tokens.json"),
            "--out-dir",
            str(refactor_dir),
        ],
        check=True,
    )

    subprocess.run(
        [
            "python3",
            str(base_dir / "generate_code_sync_outputs.py"),
            "--input",
            str(refactor_dir / "figma-sync-tokens.json"),
            "--dark",
            str(refactor_dir / "dark-mode-tokens.json"),
            "--out-dir",
            str(sync_dir),
        ],
        check=True,
    )

    print("Flow smoke test complete")
    print(f"Figma URL: {args.figma_url}")
    print(f"Gap output: {gap_dir}")
    print(f"Audit output: {audit_dir}")
    print(f"Refactor output: {refactor_dir}")
    print(f"Code-sync output: {sync_dir}")


if __name__ == "__main__":
    main()
