def parse(tokens):
    stack = []
    output = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "IF":
            output.append("IF")
        elif token == "ELSE":
            output.append("ELSE")
        elif token == "THEN":
            output.append("THEN")
        else:
            output.append(token)
        i += 1
    return output

