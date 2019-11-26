import lexer


token_exprs = [
    (r'[ \t]+',              None),
    (r'#[^\n]*',               None),
    (r'[\n]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'\n[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'[\+\-]?[0-9]*\.[0-9]+',            "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',     "INT"),
    (r'\n',              "NEWLINE"),
    (r'\=(?!\=)',                    "EQ"),
    (r'\==',                  "ISEQUAL"),
    (r'\(',                    "LP"),
    (r'\)',                    "RP"),
    (r'\;',                     "SC"),
    (r'\:',                     "TITIKDUA"),
    (r'\->',                    "ARROW"),
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
    (r'\bformat\b',            "FORMAT"),
    (r'\band\b',                   "AND"),
    (r'\bor\b',                    "OR"),
    (r'\bnot\b',                   "NOT"),
    (r'\bif\b',                    "IF"),
    (r'\bthen\b',                  "THEN"),
    (r'\belse\b',                  "ELSE"),
    (r'\belif\b',                  "ELIF"),
    (r'\bwhile\b',                 "WHILE"),
    (r'\brange\b',                 "RANGE"),
    (r'\bFalse\b',                 "FALSE"),
    (r'\bTrue\b',                  "TRUE"),
    (r'\bNone\b',                  "NONE"),
    (r'\bbreak\b',                 "BREAK"),
    (r'\bas\b',                    "AS"),
    (r'\bclass\b',                 "CLASS"),
    (r'\bcontinue\b',              "CONTINUE"),
    (r'\bdef\b',                   "DEF"),
    (r'\bfor\b',                   "FOR"),
    (r'\bfrom\b',                  "FROM"),
    (r'\bimport\b',                "IMPORT"),
    (r'\bin\b',                    "IN"),
    (r'\bis\b',                    "IS"),
    (r'\breturn\b',                "RETURN"),
    (r'\braise\b',                 "RAISE"),
    (r'\bpass\b',                  "PASS"),
    (r'\bwith\b',                  "WITH"),
    (r'\bdict\b',                    "TIPE"),
    (r'\bint\b',                    "TIPE"),
    (r'\bstr\b',                    "TIPE"),
    (r'\bfloat\b',                    "TIPE"),
    (r'\bcomplex\b',                    "TIPE"),
    (r'\blist\b',                    "TIPE"),
    (r'\btuple\b',                    "TIPE"),
    (r'\,',                    "COMMA"),
    (r'\w+[.]\w+',                    "KARTITIK"),
    (r'\.',                    "TITIK"),
    (r'\[',                    "LSB"),
    (r'\]',                    "RSB"),
    (r'\{',                    "LCB"),
    (r'\}',                    "RCB"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'\"[^\"\n]*\"',                    "STRING"),
    (r'\'[^\'\n]*\'',                    "STRING"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

def imp_lex(characters):
    return lexer.lex(characters, token_exprs)
