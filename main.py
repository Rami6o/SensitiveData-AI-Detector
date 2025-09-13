import re

patterns = {
    "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
    "phone": re.compile(r"\+?\d{1,3}[-.\s]??\d{2,4}[-.\s]??\d{3,4}[-.\s]??\d{3,4}"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "iban": re.compile(r"\b[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){1,7}[ ]?[0-9]{0,16}\b"),
    "tc_kimlik": re.compile(r"\b[1-9]\d{10}\b"),
    "ip_address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "url": re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"),

    # Yeni eklenenler:
    "passport": re.compile(r"\b[A-Z]{1}[0-9]{6,8}\b"),  # Örn: U1234567
    "driver_license": re.compile(r"\b[0-9]{6,8}[A-Z]{1,2}\b"),  # Örn: 12345678AB
    "plate": re.compile(r"\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b")  # Örn: 34 ABC 1234
}

def detect_sensitive_data(text):
    results = {}
    for key, pattern in patterns.items():
        results[key] = pattern.findall(text)
    return results


if __name__ == "__main__":
    sample = """
    Mail: test@example.com,
    Card: 4111-1111-1111-1111,
    Tel: +90 555 123 4567,
    IBAN: TR12 3456 7890 1234 5678 9012 34,
    TC: 12345678901,
    IP: 192.168.1.1,
    URL: https://example.com/test,
    Pasaport: U1234567,
    Ehliyet: 12345678AB,
    Plaka: 34 ABC 1234
    """
    print(detect_sensitive_data(sample))
