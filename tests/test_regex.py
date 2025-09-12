import sys
import os
import pytest

# Proje kök dizinini Python path'e ekliyoruz
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import patterns


def test_email_regex():
    text = "Mailim test@example.com"
    matches = patterns["email"].findall(text)
    assert matches == ["test@example.com"]


def test_credit_card_regex():
    text = "Kart numaram 4111-1111-1111-1111"
    matches = patterns["credit_card"].findall(text)
    assert matches[0].replace("-", "") == "4111111111111111"


def test_phone_regex():
    text = "Telefon: +90 555 123 45 67"
    matches = patterns["phone"].findall(text)
    assert matches[0].replace(" ", "") == "+905551234567"
