import argparse
import re
import json
from src.ai_model import train

def regex_scan(text):
    patterns = {
        "email": r"[\w\.-]+@[\w\.-]+",
        "credit_card": r"\b(?:\d[ -]*?){13,16}\b"
    }
    findings = {}
    for key, pattern in patterns.items():
        findings[key] = re.findall(pattern, text)
    return findings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sensitive Data Detector")
    parser.add_argument("--file", required=True, help="Taranacak dosya")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    regex_results = regex_scan(content)
    ai_results = {"ai_detected": ["Örnek AI sonucu"]}  # Placeholder

    report = {"regex": regex_results, "ai": ai_results}

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("Tarama tamamlandı. Sonuçlar report.json içinde.")
