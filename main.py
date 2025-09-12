import re

# Regex pattern sözlüğü (compiled objects)
patterns = {
    "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "phone": re.compile(r"\+?\d[\d\s-]{7,}\d"),
}

def detect_sensitive_data(text):
    results = {}
    for key, pattern in patterns.items():
        results[key] = pattern.findall(text)
    return results


if __name__ == "__main__":
    sample = "Mail: test@example.com, Card: 4111-1111-1111-1111, Tel: +90 555 123 4567"
    print(detect_sensitive_data(sample))
