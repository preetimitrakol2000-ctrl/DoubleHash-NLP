def extract_tokens(text_string):
    cleaned = "".join(c for c in text_string.lower() if c.isalnum() or c.isspace())
    return [word for word in cleaned.split() if len(word) > 2]
