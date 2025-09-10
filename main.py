import argparse
import os
import re
import json
from datetime import datetime
from pathlib import Path

patterns = {
    "creditcard": r"\b(?:\d[ -]*?){13,16}\b",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "iban": r"\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b",
    "tc": r"\b\d{11}\b",
    "phone": r"\b\d{10,11}\b",
}

def load_config(config_path):
    import yaml
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg

def scan_file(file_path, selected_patterns):
    results = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        for name, regex in selected_patterns.items():
            for match in re.findall(regex, content):
                results.append({"pattern": name, "match": match})
    return results

def save_report(results, report_type, output_dir, input_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    base_name = Path(input_file).stem
    if report_type == "json":
        out_file = output_dir / f"{base_name}_report_{timestamp}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
    elif report_type == "html":
        out_file = output_dir / f"{base_name}_report_{timestamp}.html"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("<html><body><h1>Scan Report</h1><ul>")
            for r in results:
                f.write(f"<li>{r['pattern']}: {r['match']}</li>")
            f.write("</ul></body></html>")
    print(f"Report saved to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Sensitive Data AI Detector")
    parser.add_argument("--input", required=True, help="Input file to scan")
    parser.add_argument("--pattern", default="all", help="Pattern to scan (creditcard, email, iban, tc, phone, all)")
    parser.add_argument("--report", default="json", help="Report type (json/html)")
    parser.add_argument("--output", default="reports", help="Output directory")
    parser.add_argument("--config", help="Optional config YAML file")
    args = parser.parse_args()

    selected_patterns = patterns
    if args.config:
        cfg = load_config(args.config)
        selected_patterns = {p: patterns[p] for p in cfg.get("patterns", patterns.keys())}

    if args.pattern != "all":
        selected_patterns = {args.pattern: selected_patterns[args.pattern]}

    results = scan_file(args.input, selected_patterns)
    save_report(results, args.report, args.output, args.input)

if __name__ == "__main__":
    main()



# main.py
print("SensitiveData-AI-Detector güncellendi")  # yeni satır ekle
