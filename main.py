import ply.lex as lex

def readLinesFile(fileName):
    elements = []
    try:
        with open(fileName) as File:
            elements = File.readlines()
    finally:
        File.close()
    return elements


def writeInFile(fileName, content):
    try:
        File = open(fileName, "resultado")
        File.write(content)
    finally:
        File.close()


def appendInFile(fileName, content):
    try:
        File = open(fileName, "entrada")
        File.write("\n" + content)
    finally:
        File.close()

#Seteo para tokens validadores
nameFile = 'expresiones.in'
tokens = [
    'iniciar-programa',
    'inicia-ejecucion',
    'termina-ejecucion',
    'finalizar-programa',
    'EOF'
]
#Seteo para operaciones reservadas
reserved = {
    'suma' : 'PLUS',
    'resta' : 'MINUS',
    'multiplicacion' : 'TIMES',
    'division' : 'DIVIDE',

}

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_ignore = ' \t'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() in reserved :
        t.type = reserved[ t.value.lower() ]
        t.value = switchValue (t.type)
    return t

def switchValue(x):
    return {
        'PLUS': '+',
        'MINUS': '-',
        'TIMES': '*',
        'DIVIDE': '/',
        'EQUALS' : '='
    }[x]

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Definicion para manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Definicion de nueva regla
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lex.lex()
data = ''
for exp in readLinesFile(nameFile):
    data+=exp

lex.input(data)

while True:
    tok = lex.token()
    if not tok: break
    print(str(tok.value) + " - " + str(tok.type))
