import ply.lex as lex
import re
from math import *


class lexer:
    # RESERVED
    reserved = {
        'select': 'SELECT',
        'from': 'FROM',
        'where': 'WHERE',
        'order': 'ORDER',
        'group': 'GROUP',
        'by': 'BY',
        'and': 'AND',
        'or': 'OR',
        'as': 'AS',
        'not': 'NOT',
        'into': 'INTO',
        'insert': 'INSERT',
        'values': 'VALUES',
        'like': 'LIKE',
        'update': 'UPDATE',
        'set': 'SET',
        'delete': 'DELETE',
        'asc': 'ASC',
        'desc': 'DESC',
        'join': 'JOIN',
        'inner': 'INNER',
        'left': 'LEFT',
        'right': 'RIGHT',
        'full': 'FULL',
        'on': 'ON',
        'limit': 'LIMIT',
        'offset': 'OFFSET',

    }

    # TOKENS
    tokens = ['FLOAT', 'NUMBER', 'NAME', 'NE', 'LE', 'GE',
              'SQ', 'DQ', 'STRING', "INDEX", 'DATASOURCE'] + list(reserved.values())

    literals = ['=', '+', '-', '*', '^', '>', '<', '/',
                '.', '(', ')', ',', '!', '|', '&', ';']

    t_NE = r"!="
    t_LE = r"<="
    t_GE = r">="
    t_SQ = r"'"
    t_DQ = r"\""
    t_STRING = r"'[^\']*'|\"[^\"]*\""
    t_INDEX = r"\[\d+\]"
    t_DATASOURCE = r"\[\'[^\]]+\'\]|\[\"[^\]]+\"\]"

    # DEFINE OF TOKENS

    def t_NAME(self, t):
        r'[a-zA-Z_]+[a-zA-Z0-9_]*\.?[a-zA-Z0-9_]+'
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    def t_FLOAT(self, t):
        r'\d+\.\d+|\.\d+'
        t.value = float(t.value)
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # IGNORED
    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # scan sql statement
    def scan(self, statement):
        self.lexer.input(statement)

    # return sacned token
    def get_token(self):
        return self.lexer.token()
