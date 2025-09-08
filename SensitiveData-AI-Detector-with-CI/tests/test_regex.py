from main import regex_scan

def test_email_detection():
    text = "contact me at test@example.com"
    results = regex_scan(text)
    assert "test@example.com" in results["email"]
