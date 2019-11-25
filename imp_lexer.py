import lexer

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'


token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\=',                    "EQ"),
    (r'\=\=',                  "ISEQUAL"),
    (r'\(',                    "LP"),
    (r'\)',                    "RP"),
    (r'\;',                     "SC"),
    (r'\:',                     "TITIKDUA"),
    (r'\+',                    "ADD"),
    (r'\-',                     "SUBTR"),
    (r'\*',                    "MUL"),
    (r'/',                     "DIV"),
    (r'<=',                    "LE"),
    (r'<',                     "L"),
    (r'>=',                    "GE"),
    (r'>',                     "G"),
    (r'!=',                    "NEQ"),
    (r'-=',                    "SUBAS"),
    (r'\*=',                   "MULAS"),
    (r'\+=',                   "SUMAS"),
    (r'/=',                    "DIVAS"),
    (r'and',                   "AND"),
    (r'or',                    "OR"),
    (r'not',                   "NOT"),
    (r'if',                    "IF"),
    (r'then',                  "THEN"),
    (r'else',                  "ELSE"),
    (r'elif',                  "ELIF"),
    (r'while',                 "WHILE"),
    (r'range',                 "RANGE"),
    (r'False',                 "FALSE"),
    (r'True',                  "TRUE"),
    (r'None',                  "NONE"),
    (r'break',                 "BREAK"),
    (r'as',                    "AS"),
    (r'class',                 "CLASS"),
    (r'continue',              "CONTINUE"),
    (r'def',                   "DEF"),
    (r'for',                   "FOR"),
    (r'from',                  "FROM"),
    (r'import',                "IMPORT"),
    (r'in',                    "IN"),
    (r'is',                    "IS"),
    (r'return',                "RETURN"),
    (r'raise',                 "RAISE"),
    (r'pass',                  "PASS"),
    (r'with',                  "WITH"),
    (r'\,',                    "COMMA"),
    (r'\.',                    "TITIK"),
    (r'\'',                    "PETIKSATU"),
    (r'\"',                    "PETIKDUA"),
    (r'\[',                    "LSB"),
    (r'\]',                    "RSB"),
    (r'\{',                    "LCB"),
    (r'\}',                    "RCB"),
    (r'[0-9]+',                INT), #integer masih nerima 003, gaboleh
    (r'[A-Za-z_][A-Za-z0-9_]*',ID),
]

def imp_lex(characters):
    return lexer.lex(characters, token_exprs)
