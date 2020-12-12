import ply.lex as lex

tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE'
]
reservadas = {'BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
		'VAR','PROCEDURE','OUT','IN','ELSE'
}

#tokens = tokens + set (reservadas.values())

t_ignore = '\t'

t_ID = r'\-'
t_NUMBER = r'\+'
t_PLUS = r'\*'
t_MINUS = r'\/'
t_TIMES = r'\,'
t_DIVIDE = r'\('
t_ODD = r'\)'
t_ASSIGN = r'\"'
t_NE = r'<'
t_LT = r'>'
t_LTE = r'\<\='
t_GT = r'\>\='
t_LPARENT = r'\>\='
t_COMMA = r'\>\='
t_SEMMICOLOM = r'\>\='
t_DOT = r'\>\='
t_UPDATE = r'\>\='

def t_BEGIN(t):
    r'begin'
    return t
def t_END(t):
    r'end'
    return t
def t_IF(t):
    r'if'
    return t
def t_THEN(t):
    r'then'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_DO(t):
    r'do'
    return t
def t_VARIABLE(t):
    r'\w+\=|\w+\s\='
    return t
def t_CALL(t):
    r'call'
    return t
def t_CONST(t):
    r'const'
    return t
def t_VAR(t):
    r'var'
    return t
def t_PROCEDURE(t):
    r'procedure'
    return t
def t_OUT(t):
    r'out'
    return t
def t_IN(t):
    r'in'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_BOLEAN(t):
    r'true|false'
    return t
def t_espacio(t):
    r"\s"
    pass
def t_STRING(t):
    r'\w+|:'
    return t

lexer = lex.lex()


