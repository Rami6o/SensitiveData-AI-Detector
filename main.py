import re

patterns = {
    "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
    "phone": re.compile(r"\+?\d{1,3}[-.\s]??\d{2,4}[-.\s]??\d{3,4}[-.\s]??\d{3,4}"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),

    # Yeni eklenenler:
    "iban": re.compile(r"\b[A-Z]{2}[0-9]{2}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{0,16}\b"),
    "tc_kimlik": re.compile(r"\b[1-9]\d{10}\b"),
    "ip_address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "url": re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
}

def detect_sensitive_data(text):
    results = {}
    for key, pattern in patterns.items():
        results[key] = pattern.findall(text)
    return results


if __name__ == "__main__":
    sample = "Mail: test@example.com, Card: 4111-1111-1111-1111, Tel: +90 555 123 4567"
    print(detect_sensitive_data(sample))
