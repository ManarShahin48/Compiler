# The name "yacc" stands for "Yet Another Compiler Compiler"
# pass ==> make the function without body
import ply.yacc as yacc
import petl as etl
import csv
import sqlite3

# Get the token map from the lexer.
from ply_lex import tokens


start = "start"


def p_start(p):
    """start : select
    | insert
    | update
    | delete"""
    pass


# ♦♦♦♦♦♦♦ OPERATIONS ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_expression_plus(p):
    "expression : expression PLUS term"
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression MINUS term"
    p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term_times(p):
    "term : term TIMES factor"
    p[0] = p[1] * p[3]


def p_term_div(p):
    "term : term DIVIDE factor"
    p[0] = p[1] / p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ Basic Variables ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
def p_empty(p):
    "empty :"
    p[0] = " "


def p_op(p):
    """op : EQUAL
    | BIGGER_THAN_OR_EQUAL_TO
    | BIGGER_THAN
    | SMALLER_THAN_OR_EQUAL_TO
    | SMALLER_THAN"""
    pass


def p_where(p):
    "where : WHERE condition"

    p[0] = p[2]


def p_where_empty(p):
    "where : empty"
    p[0] = True


def p_condition(p):
    "condition : expression op expression"
    pass


# p[0] = p[1] + p[2] + p[3]


def p_condition_parens(p):
    "condition : LPAREN condition RPAREN"
    p[0] = p[2]


def p_expression(p):
    "expression : expression_term"
    p[0] = p[1]


def p_expression_term(p):
    "expression_term : term"
    p[0] = p[1]


def p_term(p):
    """term : COLUMN_NAME
    | NUMBER
    | STRING"""
    pass


def p_condition_and(p):
    "condition : condition AND condition"
    p[0] = p[1] and p[3]


def p_condition_or(p):
    "condition : condition OR condition"
    p[0] = p[1] or p[3]


def p_condition_not(p):
    "condition : NOT condition"
    p[0] = not p[2]


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ SELECT ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_select(p):
    """select : SELECT column into FROM DATASOURCE where group order limit SIME_COLON
    | empty"""
    print("Select is Done ♠")


# PETL
# if p[4] == p[4].find('.db'):
#     with open(f'{p[4]}', 'r') as f:
#         connection = sqlite3.connect(f'{p[4]}')
#         # p[0] ==> SELECT * FROM example
#         table = etl.fromdb(connection, f'{p[0]}')

# elif p[4] == p[4].find('.csv'):
#     with open(f'{p[4]}', 'r') as f:
#         table = etl.fromcsv(f'{p[4]}')

# elif p[4] == p[4].find('.txt'):
#     with open(f'{p[4]}', 'r') as f:
#         table = etl.fromtext(f'{p[4]}')

# elif p[4] == p[4].find('.xml'):
#     with open(f'{p[4]}', 'r') as f:
#         table = etl.fromxml(f'{p[4]}', 'tr', 'td')

# elif p[4] == p[4].find('.json'):
#     with open(f'{p[4]}', 'r') as f:
#         table = etl.fromjson(f'{p[4]}', header=['foo', 'bar'])

# elif p[4] == p[4].find('.p'):
#     with open(f'{p[4]}', 'r') as f:
#         table = etl.frompickle(f'{p[4]}')
# print(table)


def p_into(p):
    """into : INTO DATASOURCE
    | empty"""


def p_group(p):
    """group : GROUP BY column having
    | empty"""
    pass  # p[0] = " "


def p_having(p):
    """having : HAVING condition
    | empty"""
    pass


def p_order(p):
    """order : ORDER BY orders
    | empty"""
    pass  # p[0] = " "


def p_orders(p):
    """orders : column way
    | orders COMAA orders"""
    pass


def p_way(p):
    """way : ASC
    | DESC
    | empty"""
    pass


def p_limit(p):
    """limit : LIMIT NUMBER"""
    if p[2] < 0:
        p[0] = None
    else:
        p[0] = int(p[2])


def p_limit_empty(p):
    "limit : empty"
    p[0] = None


def p_select_into(p):
    pass


def p_column_all(p):
    "column : TIMES"  # '*'
    p[0] = ["*"]


def p_column_name(p):
    "column : COLUMN_NAME"
    p[0] = [p[1]]


def p_column_number(p):
    "column : COLUMN_NUMBER"
    p[1] = int(p[1][1:-1])
    p[0] = [p[1]]


def p_columns(p):
    """column : column COMAA column
    | empty"""
    p[0] = []
    if type(p[1]) == list:
        p[0].extend(p[1])
    else:
        p[0].append(p[1])
    p[0].append(p[3])


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ INSERT ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_insert(p):
    """insert : INSERT INTO DATASOURCE icolumn VALUES LPAREN value RPAREN SIME_COLON
    | INSERT INTO DATASOURCE icolumn LPAREN select RPAREN SIME_COLON"""
    print("Insert is Done ♠")


# PETL
# if p[3] == p[3].find('.csv'):
#     table1 = [[f'{p[5]}', f'{p[5]}'],
#               [f'{p[9]}', f'{p[9]}'],
#               [f'{p[9]}', f'{p[9]}'],
#               [f'{p[9]}', f'{p[9]}']]
#     with open(f'{p[5]}', 'w') as f:
#         writer = csv.writer(f)
#         writer.writerows(table1)
#     table2 = etl.fromcsv('example.csv')
#     table2


def p_value_string(p):
    "value : STRING"
    pass


def p_value_number(p):
    "value : NUMBER"
    pass


def p_value(p):
    "value : value COMAA value"
    pass


def p_icolumn(p):
    """icolumn : LPAREN COLUMN_NAME RPAREN
    | empty"""
    pass


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ UPDATE ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_update(p):
    "update : UPDATE DATASOURCE SET assigns where SIME_COLON"
    print("Update is Done ♠")


def p_assigns(p):
    """assigns : column EQUAL value
    | assigns COMAA assigns"""
    pass


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ DELETE ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_delete(p):
    "delete : DELETE FROM DATASOURCE where SIME_COLON"
    print("Delete is Done ♠")


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
if __name__ == "__main__":
    while True:
        s = input("The yacc :  ")
        if s == "q":
            break
        if not s:
            continue
        result = parser.parse(s)


# select student into [Country] from [data];
# select student into [Country] from [data] where 3>=4 order by column desc;
# insert into [data source] (values) values (4,3);
# insert into [data source] (column) (select student into [Country] from [data];);
# update [data source] set column1 = "compiler"  where 3>1;
# delete from [data source] where 1<=7;
