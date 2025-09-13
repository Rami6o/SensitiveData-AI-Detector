import re
from main import patterns

def test_email():
    text = "Email: test@example.com"
    matches = patterns["email"].findall(text)
    assert "test@example.com" in matches

def test_phone():
    text = "Telefon: +90 555 123 4567"
    matches = patterns["phone"].findall(text)
    assert any("555" in m for m in matches)

def test_credit_card():
    text = "Kredi Kartı: 4111 1111 1111 1111"
    matches = patterns["credit_card"].findall(text)
    assert any("4111" in m for m in matches)

def test_iban():
    text = "IBAN: TR12 3456 7890 1234 5678 9012 34"
    matches = patterns["iban"].findall(text)
    assert any("TR12" in m for m in matches)

def test_tc_kimlik():
    text = "TC: 12345678901"
    matches = patterns["tc_kimlik"].findall(text)
    assert "12345678901" in matches

def test_ip_address():
    text = "Server IP: 192.168.1.1"
    matches = patterns["ip_address"].findall(text)
    assert "192.168.1.1" in matches

def test_url():
    text = "Website: https://example.com/test"
    matches = patterns["url"].findall(text)
    assert any("example.com" in m for m in matches)

def test_passport():
    text = "Pasaport No: U1234567"
    matches = patterns["passport"].findall(text)
    assert "U1234567" in matches

def test_driver_license():
    text = "Ehliyet: 12345678AB"
    matches = patterns["driver_license"].findall(text)
    assert "12345678AB" in matches

def test_plate():
    text = "Plaka: 34 ABC 1234"
    matches = patterns["plate"].findall(text)
    assert "34 ABC 1234" in matches
