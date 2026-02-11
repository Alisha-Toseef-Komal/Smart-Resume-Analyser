import re

def extract_email(text):
    match = re.search(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        text
    )
    return match.group() if match else None


def extract_phone(text):
    match = re.search(
        r"\b(\+?\d{1,3}[-.\s]?)?\d{10}\b",
        text
    )
    return match.group() if match else None
