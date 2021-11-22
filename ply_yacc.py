# The name "yacc" stands for "Yet Another Compiler Compiler"
# pass ==> make the function without body
import ply.yacc as yacc
# Get the token map from the lexer.
from ply_lex import tokens

start = 's'


def p_start(p):
    'start : s'
    pass


def p_s(p):
    '''s: SELECT 
    | INSERT
    | UPDATE
    | DELETE'''
    pass

# ♦♦♦♦♦♦♦ VARIABLES ♦♦♦♦♦♦♦


def p_where(p):
    'where: WHERE condition'
    p[0] = p[2]


def p_condition(p):
    'condition: exp op exp'
    p[0] = p[1] + p[2] + p[3]


def p_exp(p):
    'exp: expression_term'
    p[0] = p[1]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term(p):
    '''term: COLMN_NAME
    | NUMBER
    | STRING'''


def p_op(p):
    '''op: EQUAL
    | BIGGER_THAN_OR_EQUAL_TO
    | BIGGER_THAN
    |SMALLER_THAN_OR_EQUAL_TO
    |SMALLER_THAN'''
    pass


def p_where_empty(p):
    'where: '
    pass


def p_empty(p):
    'empty:'
    pass


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_factor_num(p):
    'factor : NUMBER'
    pass


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# ♦♦♦♦♦♦♦ SELECT ♦♦♦♦♦♦♦

def p_select(p):
    'select: SELECT colums FROM DATASOURCE'
    pass


def p_select_into(p):
    'select: SELECT colums INTO DATASOURCE FROM DATASOURCE'
    pass


def p_colums(p):
    'colums: colums COMMA COLMN_NAME'
    pass


def p_colums_n(p):
    'colums: COLMN_NAME'
    pass

# ♦♦♦♦♦♦♦ INSERT ♦♦♦♦♦♦♦


def p_insert_into(p):
    'insert: INSERT INTO DATASOURCE SELECT FROM DATASOURCE'
    pass

# ♦♦♦♦♦♦♦ UPDATE ♦♦♦♦♦♦♦


def p_update(p):
    'update: UPDATE DATASOURCE colums WHERE'
    p[0] = p[3]

# ♦♦♦♦♦♦♦ DELETE ♦♦♦♦♦♦♦


def p_delete(p):
    'delete: DELETE FROM DATASOURCE WHERE'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    s = input('our yacc > ')
    if not s:
        continue
    result = parser.parse(s)
    print(result)
