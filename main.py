from patterns import patterns

def detect_sensitive_data(text):
    results = {}
    for key, pattern in patterns.items():
        results[key] = pattern.findall(text)
    return results


if __name__ == "__main__":
    sample = "Mail: test@example.com, Card: 4111-1111-1111-1111, Tel: +90 555 123 4567"
    print(detect_sensitive_data(sample))
