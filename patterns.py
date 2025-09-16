import re

patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": re.compile(r"\+?\d{1,3}[-.\s]??\d{2,4}[-.\s]??\d{3,4}[-.\s]??\d{3,4}"),
    "credit_card": r"^\d{16}$",
    "iban": re.compile(r"\b[A-Z]{2}[0-9]{2}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{0,16}\b"),
    "tc_kimlik": re.compile(r"\b[1-9]\d{10}\b"),
    "ip_address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "url": re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
}

EMAIL_REGEX = re.compile(patterns["email"])
CC_REGEX = re.compile(patterns["credit_card"])
# Telefon numarası (Türkiye formatı: +90 veya 0 ile başlayabilir, toplam 10 haneli)
PHONE_REGEX = re.compile(r"^(?:\+90|0)?5\d{9}$")
# Türkiye Cumhuriyeti Kimlik Numarası (11 haneli, ilk rakam 0 olamaz, son hane çift kontrol kurallarıyla doğrulanabilir ama basit regex şimdilik yeterli)
TCKN_REGEX = re.compile(r"^[1-9]\d{10}$")
# IBAN (Türkiye: TR + 24 hane)
IBAN_REGEX = re.compile(r"^TR\d{24}$")
