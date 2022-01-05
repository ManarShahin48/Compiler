# The name "yacc" stands for "Yet Another Compiler Compiler"
# pass ==> make the function without body
from pickle import NONE
from petl.io.csv import appendcsv
from petl.io.db import appenddb
from petl.io.pickle import appendpickle, frompickle
import ply.yacc as yacc
import petl as etl
import csv
import sqlite3
import pandas as pd
from petl import fromcsv
from petl import look
from petl import tocsv, look
from petl import fromxml
import time
import pymysql

start_time = time.time()
# Get the token map from the lexer.
from ply_lex import tokens


start = "start"


def p_start(p):
    """start : select
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


def p_where(p):
    "where : WHERE condition"
    p[0] = p[2]


def p_where_empty(p):
    "where : empty"
    p[0] = None


def p_condition(p):
    "condition : expression op expression"
    p[0] = (p[1], p[2], p[3])  # =====> TUPLE


def p_condition_parens(p):
    "condition : LPAREN condition RPAREN"
    p[0] = p[2]


def p_expression(p):
    """expression : COLUMN_NAME
    | NUMBER
    | string"""
    p[0] = p[1]


def p_string(p):
    "string : STRING"
    p[0] = p[1][1:-1]  # ===========> delete " , "


def p_op(p):
    """op : EQUAL
    | EQUAL_EQUAL
    | BIGGER_THAN_OR_EQUAL_TO
    | BIGGER_THAN
    | SMALLER_THAN_OR_EQUAL_TO
    | SMALLER_THAN"""
    p[0] = p[1]


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
    """select : SELECT column FROM data into where order SIME_COLON"""
    # ================= EXTRACT ================= #
    testFile = None
    if ".csv" in p[4]:
        testFile = fromcsv(p[4])
    elif ".db" in p[4]:
        Connection = sqlite3.connect(p[4])
        testFile = etl.fromdb(Connection, "SELECT * FROM table3m")
    # elif ".db" in p[4]:
    #     connection = pymysql.connect(password='moonpie', database='thangs')
    #     table = etl.fromdb(connection, 'SELECT * FROM example')
    elif ".p" in p[4]:
        testFile = etl.frompickle(p[4])
    elif ".json" in p[4]:
        testFile = etl.fromjson(p[4])
    elif ".xml" in p[4]:
        testFile = etl.fromxml(p[4], "tr", "td")

    # ================= TRANSFORM ================= #
    if p[6] != None:  # ===> where a == csv
        if p[6][1] == "=":
            testFile = etl.select(
                testFile, lambda ele: ele[p[6][0]] == p[6][2]
            )  # ===> done
        if p[6][1] == ">":
            testFile = etl.select(testFile, lambda ele: ele[p[6][0]] > p[6][2])
        if p[6][1] == "<":
            testFile = etl.select(testFile, lambda ele: ele[p[6][0]] < p[6][2])
    if p[2] != "*":
        testFile = etl.cut(testFile, p[2])  # Select by column number ===> bug
    else:
        testFile = etl.cutout(testFile)

    if p[7] != None:
        testFile = etl.sort(testFile)
    # ================= LOAD ================= #
    if p[5] == "console":
        print(testFile)
        print("--- %s seconds ---" % (time.time() - start_time))

    elif ".csv" in p[5]:
        appendcsv(testFile, p[5])
        print(testFile)

    elif ".p" in p[5]:
        appendpickle(testFile, p[5])
        print(frompickle(p[5]))
        print("Success")
    elif ".db" in p[5]:
        Connection = sqlite3.connect(p[5])
        appenddb(testFile, Connection, "table1")
        print(testFile)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif ".json" in p[5]:
        etl.tojsonarrays(testFile, p[5])
        print(open(p[5]).read())
        print("--- %s seconds ---" % (time.time() - start_time))
    elif ".html" in p[5]:
        etl.tohtml(testFile, p[5], caption="example Table HTML")
        print("Success")
        print(testFile)

    # p[0] = (
    #     f"from app import petl\n"
    #     f"\n"
    #     f"data = etl.extract('{p[4]}')\n"
    #     f"data = etl.transform(\n"
    #     f"   data,\n"
    #     f"   {{\n"
    #     f"        'COLUMNS':  {p[2]},\n"
    #     f"        'ORDER':    {p[7]},\n"
    #     f"    }}\n"
    #     f")\n"
    #     f"etl.load(data, '{p[5]}')\n"
    # )
    # print(p[0])


def p_into(p):
    "into : INSERT data"
    p[0] = p[2]


def p_into_empty(p):
    "into : empty"
    p[0] = "console"
    # p[0] = None


def p_order_asc(p):
    "order : ORDER BY ASC"
    p[0] = p[1]  # p[0] = " "


def p_order_empty(p):
    "order : empty"
    p[0] = None  # p[0] = " "


# def p_way(p):
#     """way : ASC
#     | DESC"""
#     p[0] = p[1]


# def p_way(p):
#     "way : empty"
#     p[0] = p[1]


# def p_order(p):
#     """order : ORDER BY orders
#     | empty"""
#     p[0] = p[3]  # p[0] = " "


# def p_order(p):
#     """order : empty"""
#     p[0] = p[1]  # p[0] = " "


# def p_orders(p):
#     """orders : column way
#     | orders COMAA orders"""
#     p[0] = (p[1], p[2])


# def p_way(p):
#     """way : ASC
#     | DESC
#     | empty"""
#     p[0] = p[1]


def p_select_into(p):
    pass


def p_column_all(p):
    "column : TIMES"  # '*'
    p[0] = "*"


def p_column_name(p):
    "column : COLUMN_NAME"
    p[0] = [p[1]]


def p_column_number(p):
    "column : DATASOURCE"
    p[0] = [int(p[1][1:-1])]


def p_columns(p):
    """column : column COMAA column
    | empty"""
    p[0] = []
    p[0].extend(p[1])
    p[0].extend(p[3])


def p_data(p):
    "data : DATASOURCE"
    p[0] = p[1][1:-1]


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ INSERT ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# def p_insert(p):
#     """insert : INSERT INTO data LPAREN icolumn RPAREN VALUES LPAREN value RPAREN SIME_COLON
#     | INSERT INTO data LPAREN icolumn RPAREN LPAREN select RPAREN SIME_COLON"""

#     testFile = p[3]
#     if ".csv" in p[3]:
#         appendcsv(p[9], testFile)
#         print("Success")
#         print(testFile)  # ============> ERROR
#     elif ".p" in p[3]:
#         appendpickle(p[9], testFile)
#         print(frompickle(testFile))
#     elif ".db" in p[3]:
#         Connection = sqlite3.connect(testFile)
#         appenddb(p[9], Connection, "table1")
#         print("Success")
#     elif ".json" in p[3]:
#         etl.tojsonarrays(p[9], testFile)
#         print(open(testFile).read())
#     elif ".html" in p[3]:
#         etl.tohtml(p[9], testFile, caption="example Table HTML")
#     # if ".csv" in p[3]:
#     #     testFile = etl.tocsv(p[9], p[3])
#     #     print("testFile")
#     #     print(open(p[3]).read())


# insert into [example copy.csv] (a,b) values (insert,insert);
def p_value_string(p):
    "value : STRING"
    p[0] = p[1]


def p_value_number(p):
    "value : NUMBER"
    p[0] = p[1]


def p_value(p):
    "value : value COMAA value"
    p[0] = (p[1], p[2], p[3])


def p_icolumn_empty(p):
    "icolumn : empty"
    p[0] = p[1]


def p_icolumn_name(p):
    "icolumn : COLUMN_NAME"
    p[0] = p[1]


def p_icolumns(p):
    """icolumn : icolumn COMAA icolumn"""
    p[0] = []
    p[0].extend(p[1])
    p[0].extend(p[3])


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ UPDATE ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_update(p):
    "update : UPDATE data SET assigns where SIME_COLON"
    print("Update is Done ♠")


def p_assigns(p):
    """assigns : column EQUAL value
    | assigns COMAA assigns"""
    pass


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# ♦♦♦♦♦♦♦ DELETE ♦♦♦♦♦♦♦
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


def p_delete(p):
    "delete : DELETE FROM data where SIME_COLON"
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

# select * from [example copy.csv] where b = "manara";
# select * from [example copy.csv] order;
# select into == order == where
