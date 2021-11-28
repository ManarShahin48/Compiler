# The name "yacc" stands for "Yet Another Compiler Compiler"
# pass ==> make the function without body
import ply.yacc as yacc
import petl as etl
import csv
import sqlite3
# Get the token map from the lexer.
from ply_lex import tokens

start = 'start'


def p_start(p):
    '''s: select 
    | insert
    | update
    | delete'''
    pass

# ♦♦♦♦♦♦♦ SELECT ♦♦♦♦♦♦♦


def p_select(p):
    'select: SELECT colums INTO DATASOURCE FROM DATASOURCE'

    if p[4] == p[4].find('.db'):
        with open(f'{p[4]}', 'r') as f:
            connection = sqlite3.connect(f'{p[4]}')
            # p[0] ==> SELECT * FROM example
            table = etl.fromdb(connection, f'{p[0]}')

    elif p[4] == p[4].find('.csv'):
        with open(f'{p[4]}', 'r') as f:
            table = etl.fromcsv(f'{p[4]}')

    elif p[4] == p[4].find('.txt'):
        with open(f'{p[4]}', 'r') as f:
            table = etl.fromtext(f'{p[4]}')

    elif p[4] == p[4].find('.xml'):
        with open(f'{p[4]}', 'r') as f:
            table = etl.fromxml(f'{p[4]}', 'tr', 'td')

    elif p[4] == p[4].find('.json'):
        with open(f'{p[4]}', 'r') as f:
            table = etl.fromjson(f'{p[4]}', header=['foo', 'bar'])

    elif p[4] == p[4].find('.p'):
        with open(f'{p[4]}', 'r') as f:
            table = etl.frompickle(f'{p[4]}')
    print(table)


def p_select_into(p):

    pass


def p_column_all(p):
    'colum: TIMIS'  # '*'
    p[0] = ['*']


def p_column_name(p):
    'colum: COLMN_NAME'
    p[0] = [p[1]]


def p_column_number(p):
    'colum: COLUMN_NUMBER'
    p[1] = int(p[1][1:-1])
    p[0] = [p[1]]


def p_colums(p):
    '''colum: colum COMMA colum
    | empty'''
    pass

# ♦♦♦♦♦♦♦ INSERT ♦♦♦♦♦♦♦


def p_insert_into(p):
    'insert: INSERT INTO DATASOURCE (colums) VALUES (STRING)'
    if p[3] == p[3].find('.csv'):
        table1 = [[f'{p[5]}', f'{p[5]}'],
                  [f'{p[9]}', f'{p[9]}'],
                  [f'{p[9]}', f'{p[9]}'],
                  [f'{p[9]}', f'{p[9]}']]
        with open(f'{p[5]}', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(table1)
        table2 = etl.fromcsv('example.csv')
        table2


def p_insert_select(p):
    'insert: INSERT INTO DATASOURCE SELECT FROM DATASOURCE'
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


def p_error(p):  # Error rule for syntax errors
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    s = input('Our yacc > ')
    if not s:
        continue
    result = parser.parse(s)
    print(result)
