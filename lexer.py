# lexer.py

def tokenize(source_code: str):
    tokens = []
    for line in source_code.splitlines():
        line = line.strip()
        if not line or line.startswith("\\"):  # allow comments with backslash
            continue
        tokens.extend(line.split())
    return tokens

