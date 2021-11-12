import ply.lex as lex
from ply.lex import TOKEN


class Lexer(object):

    # ♦♦♦♦♦♦♦♦♦♦ Reseverd Words Definiatons ♦♦♦♦♦♦♦♦♦♦
    reseverd_words = {
        'select': 'SELECT',
        'from': 'FROM',
        'into': 'INTO',
        'where': 'WHERE',
    }

    
    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'NAME',
        'EQUAL',
        'BIGGER_THAN_OR_EQUAL_TO',
        'BIGGER_THAN',
        'SMALLER_THAN_OR_EQUAL_TO',
        'SMALLER_THAN',
        'SIME_COLON',
        'COMAA',
        'LPAREN',
        'RPAREN',
    ] + list(reseverd_words.values())

    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUAL = r'='
    t_BIGGER_THAN_OR_EQUAL_TO = r'>='
    t_BIGGER_THAN = r'>'
    t_SMALLER_THAN_OR_EQUAL_TO = r'<='
    t_SMALLER_THAN = r'<'
    t_SIME_COLON = r';'
    t_COMAA = r','
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'
    t_ignore_COMMENT = r'\#.*'

    digit = r'([0-9])'
    nondigit = r'([_A-Za-z])'
    identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'
    #identifier = r'[a-zA-Z_][a-zA-Z_0-9]*'

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs) 

    # Check for reserved words
    #@TOKEN(identifier)
    def t_NAME(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reseverd_words.get(t.value, 'NAME')
        return t 

    # A regular expression rule with some action code
    #@TOKEN(r'\d')
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print("Illegal Charcter '%s'" % t.value[0])
        t.lexer.skip(1)

    def tokenize(self, data):
        self.lexer.input(data)
        print('♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
        print('The SQL Statement Tokens: ')
        while True:
            my_token = self.lexer.token()
            if not my_token:
                break
            print("♦♦♦ ", my_token.value, " ======> ", my_token.type, )#, sep=""
        


# ♦♦♦♦♦♦♦♦♦♦ Build The Lexer ♦♦♦♦♦♦♦♦♦♦
test = Lexer()

while(True):
    print('♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    q = input('Enter Query, Q to Exit: ')
    if q == 'q':
        break
    test.tokenize(q)




# env\Scripts\activate
# python ply_lex.py
