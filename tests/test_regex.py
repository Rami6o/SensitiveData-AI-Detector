import re
from main import patterns

def test_email():
    sample = "user@example.com"
    regex = patterns["email"]
    matches = re.findall(regex, sample)
    assert matches[0] == "user@example.com"

def test_creditcard():
    sample = "My card 1234-5678-9012-3456"
    regex = patterns["creditcard"]
    matches = re.findall(regex, sample)
    assert matches[0] == "1234-5678-9012-3456"

