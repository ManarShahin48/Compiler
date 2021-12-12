import ply.lex as lex
from ply.lex import TOKEN


# class Lexer(object):

# ♦♦♦♦♦♦♦♦♦♦ Reseverd Words Definiatons ♦♦♦♦♦♦♦♦♦♦
reseverd_words = {
    "select": "SELECT",
    "from": "FROM",
    "into": "INTO",
    "where": "WHERE",
    "insert": "INSERT",
    "values": "VALUES",
    "delete": "DELETE",
    "update": "UPDATE",
    "set": "SET",
    "distinct": "DISTINCT",
    "count": "COUNT",
    "sum": "SUM",
    "as": "AS",
    "group": "GROUP",
    "order": "ORDER",
    "by": "BY",
    "having": "HAVING",
    "join": "JOIN",
    "inner": "INNER",
    "asc": "ASC",
    "desc": "DESC",
    "limit": "LIMIT",
}

tokens = [
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "COLUMN_NAME",
    "COLUMN_NUMBER",
    "STRING",
    "EQUAL",
    "BIGGER_THAN_OR_EQUAL_TO",
    "BIGGER_THAN",
    "SMALLER_THAN_OR_EQUAL_TO",
    "SMALLER_THAN",
    "SIME_COLON",
    "COMAA",
    "LPAREN",
    "RPAREN",
    "SINGLE_QUOTE",
    "DOUBLE_QUOTE",
    "ARABIC_DOUBLE_QUOTE",
    "R_ARABIC_DOUBLE_QUOTE",
    "ALL",
    "AND",
    "OR",
    "NOT",
    "LBRACE",
    "RBRACE",
    "L_SQ_BRACE",
    "R_SQ_BRACE",
    "DATASOURCE",
    "PERCENT",
    "DOT",
] + list(reseverd_words.values())

# Regular expression rules for simple tokens
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_EQUAL = r"="
t_BIGGER_THAN_OR_EQUAL_TO = r">="
t_BIGGER_THAN = r">"
t_SMALLER_THAN_OR_EQUAL_TO = r"<="
t_SMALLER_THAN = r"<"
t_SIME_COLON = r";"
t_COMAA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SINGLE_QUOTE = r"\'"
t_DOUBLE_QUOTE = r"\""
t_ARABIC_DOUBLE_QUOTE = r"\”"
t_R_ARABIC_DOUBLE_QUOTE = r"\“"
t_AND = r"\&"
t_OR = r"\|"
t_NOT = r"\!"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_L_SQ_BRACE = r"\["
t_R_SQ_BRACE = r"\]"
t_DATASOURCE = r"\[[^,\]\[]+\]"
t_COLUMN_NUMBER = r"\[\d+\]"
t_PERCENT = r"\%"
t_DOT = r"\."
t_STRING = r'"([^"\n])*"'
# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"
t_ignore_COMMENT = r"\#.*"

digit = r"([0-9])"
nondigit = r"([_A-Za-z])"
# r'[a-zA-Z_][a-zA-Z_0-9]*'
identifier = r"(" + nondigit + r"(" + digit + r"|" + nondigit + r")*)"
identifier = identifier + r"|" + r"\[" + digit + r"+\]"


def __init__(self, **kwargs):
    self.lexer = lex.lex(module=self, **kwargs)


# Check for reserved words


@TOKEN(identifier)
def t_COLUMN_NAME(t):
    t.type = reseverd_words.get(t.value, "COLUMN_NAME")
    return t


# A regular expression rule with some action code


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling rule


def t_error(t):
    print("Illegal Charcter '%s'" % t.value[0])
    t.lexer.skip(1)


# def tokenize(data):
#     test.input(data)
#     print('♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
#     print('The SQL Statement Tokens: ')
#     while True:
#         my_token = test.token()
#         if not my_token:
#             break
#         print("♦♦♦ ", my_token.value, " ======> ",
#               my_token.type, )  # , sep=""


# # ♦♦♦♦♦♦♦♦♦♦ Build The Lexer ♦♦♦♦♦♦♦♦♦♦
# test = lex.lex()

# if __name__ == '__main__':
#     while(True):
#         print('♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
#         q = input('Enter Query, Q to Exit: ')
#         q = q.lower()
#         if q == 'q':
#             break
#         test.tokenize(q)

lexer = lex.lex()

if __name__ == "__main__":
    while True:
        s = input("lex> ")
        if not s:
            break
        s = s.lower()
        lexer.input(s)
        print("=======Tokens=======")
        while True:
            tok = lexer.token()
            if not tok:
                break
            print("\t", tok.value, "\t:\t", tok.type, sep="")
        print("====================")
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# env\Scripts\activate
# python ply_lex.py

# INSERT INTO Customers (CustomerName, ContactName, Country)VALUES('Cardinal', 'Tom B. Erichsen','Skagen 21', 'Stavanger', '4006', 'Norway')
# delete from  Customers where CustomerName = 'Alfreds Futterkiste';
# update Customers set ContactName = 'Alfred Schmidt', City = 'Frankfurt' where CustomerID = 1
# SELECT Count(*) AS DistinctCountries FROM(SELECT DISTINCT Country FROM Customers)
# SELECT SUM(column_name) FROM table_name WHERE  CONDITION GROUP BY column_name HAVING {arithematic function condition]; %%
