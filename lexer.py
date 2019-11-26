import sys
import re

def lex(characters, token_exprs):
    line = 1
    pos = 0
    tokens = []
    while pos < len(characters):
        if characters[pos] == '\n':
            line += 1
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print("Illegal character %s at line %d" % (characters[pos], line))
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens