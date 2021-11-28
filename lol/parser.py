from lexer import lexer
import ply.yacc as yacc


def flatten_list(nested_list):
    ''' Converts a nested list to a flat list '''
    if not nested_list or not isinstance(nested_list, list):
        return nested_list

    flat_list = []
    # Iterate over all the elements in given list
    for elem in nested_list:
        # Check if type of element is list
        if isinstance(elem, list):
            # Extend the flat list by adding contents of this element (list)
            flat_list.extend(flatten_list(elem))
        else:
            # Append the element to the list
            flat_list.append(elem)
    return flat_list


class parser():

    tokens = lexer.tokens

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'NOT'),
        ('left', '=', 'NE', '<', '>', 'LE', 'GE'),
        ('left', '*'),
    )

    def p_statements_list(self, p):
        '''
        statement_list : statement
                        |  statement_list ';' statement

        '''

        if len(p) == 2:
            p[0] = flatten_list(p[1])
        else:
            p[0] = flatten_list([flatten_list(p[1]), flatten_list(p[3])])

    def p_statement(self, p):
        '''
        statement : select_statement
                    | insert_statement
                    | update_statement
                    | delete_statement
        '''

        if len(p) == 2:
            p[0] = [p[1]]

    def p_select_statement(self, p):
        '''
        select_statement : SELECT columns_list FROM ds conditions group order limit offset
                        | SELECT columns_list INTO ds FROM ds conditions limit offset
                        | SELECT columns_list FROM ds joins conditions group order

        '''

        if len(p) == 10 and p[3] == 'from':
            p[0] = (flatten_list(p[2]), flatten_list(p[4]), flatten_list(
                p[5]), flatten_list(p[6]), flatten_list(p[7]), flatten_list(p[8]), flatten_list(p[9]))
        elif len(p) == 10 and p[3] == 'into':
            p[0] = (flatten_list(p[2]), flatten_list(p[4]), flatten_list(
                p[6]), flatten_list(p[7]), flatten_list(p[8]), flatten_list(p[9]))
        elif len(p) == 9:
            p[0] = (flatten_list(p[2]), flatten_list(p[4]), flatten_list(
                p[5]), flatten_list(p[6]), flatten_list(p[7]), flatten_list(p[8]))

    def p_insert_statement(self, p):
        '''
        insert_statement : INSERT INTO ds '(' columns_list ')' VALUES rows
                        | INSERT INTO ds VALUES rows
                        | INSERT INTO ds '(' columns_list ')' select_statement
                        | INSERT INTO ds select_statement
        '''

        if len(p) == 9:
            p[0] = (flatten_list(p[3]), flatten_list(p[5]), flatten_list(p[8]))
        elif len(p) == 6:
            p[0] = (flatten_list(p[3]), flatten_list(p[5]))
        elif len(p) == 8:
            p[0] = (flatten_list(p[3]), flatten_list(p[5]), flatten_list(p[7]))
        elif len(p) == 5:
            p[0] = (flatten_list(p[3]), flatten_list(p[4]))

    def p_update_statement(self, p):
        '''
        update_statement : UPDATE ds SET rec_set conditions

        '''

        p[0] = (flatten_list(p[2]), flatten_list(p[4]), flatten_list(p[5]))

    def p_rec_set(self, p):
        '''
        rec_set : column '=' value
                | rec_set ',' column '=' value

        '''
        if len(p) == 4:
            p[0] = [(p[1], p[3])]
        elif len(p) == 6 and p[2] == ',':
            p[0] = [p[1], (p[3], p[5])]

    def p_delete_statement(self, p):
        '''
        delete_statement : DELETE FROM ds conditions

        '''

        p[0] = (flatten_list(p[3]), flatten_list(p[4]))

    def p_joins(self, p):
        '''
        joins : join_type ds ON conditions
                | joins join_type ds ON conditions

        '''

        if len(p) == 5:
            p[0] = (p[1], p[2], flatten_list(p[4]))
        elif len(p) == 6:
            p[0] = [flatten_list(p[1]), (p[2], p[3], flatten_list(p[5]))]

    def p_join_type(self, p):
        '''
        join_type : JOIN
                | INNER JOIN
                | LEFT JOIN
                | RIGHT JOIN
                | FULL JOIN

        '''

        if len(p) == 2:
            p[0] = ('inner', p[1])
        elif len(p) == 3:
            p[0] = (p[1], p[2])

    def p_rows(self, p):
        '''
        rows : '(' rec_values ')'
                |  '(' rec_values ')' ',' rows

        rec_values : value
                    | rec_values ',' value
        '''

        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4 and p[2] != ',':
            p[0] = p[2]
        elif len(p) == 4 and p[2] == ',':
            p[0] = [p[1], p[3]]
        elif len(p) == 6:
            p[0] = [p[1], p[4]]

        # print("val", p[0])

    def p_columns_list(self, p):
        '''
        columns_list : '*'
                     | rec_columns
        rec_columns : column
                    | rec_columns ',' column

        '''

        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = [p[1], p[3]]

    def p_ds(self, p):
        '''
            ds : select_statement
                | src
                | src AS NAME
            src : NAME
                | DATASOURCE
        '''

        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = (p[1], p[3])

    def p_limit(self, p):
        '''
            limit : LIMIT NUMBER
                    | empty
        '''

        if len(p) == 3:
            p[0] = p[2]

    def p_offset(self, p):
        '''
            offset : OFFSET NUMBER
                    | empty
        '''

        if len(p) == 3:
            p[0] = p[2]

    def p_conditions(self, p):
        '''
        conditions : WHERE rec_conditions
                    | rec_conditions
                    | empty
        rec_conditions : column op value
                        | rec_conditions AND column op value
                        | rec_conditions OR column op value
        '''

        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 3:
            p[0] = [p[2]]
        elif len(p) == 4:
            p[0] = (p[1], p[2], p[3])
        elif len(p) == 6:
            p[0] = [p[1], (p[2], p[3], p[4], p[5])]

    def p_value(self, p):
        '''
        value : NAME
                | STRING
                | FLOAT
                | NUMBER
                | column
        '''
        if len(p) == 2:
            p[0] = p[1]

    def p_column(self, p):
        '''
        column : NAME
                | INDEX
        '''
        p[0] = p[1]

    def p_empty(self, p):
        'empty :'
        pass

    def p_op(self, p):
        '''
        op : '>'
            | '<'
            | '='
            | LE
            | GE
            | NE
            | LIKE
        '''

        p[0] = p[1]

    def p_group(self, p):
        '''
        group : GROUP BY columns_list
            | empty
        '''
        if len(p) == 4:
            p[0] = [p[3]]

    def p_order(self, p):
        '''
        order : ORDER BY ord
            | empty
        ord : column sort_type
            | ord ',' column sort_type
        '''
        if len(p) == 4:
            p[0] = p[3]
        elif len(p) == 3:
            if not p[2]:
                p[0] = [(p[1], 'asc')]
            else:
                p[0] = [(p[1], p[2])]
        elif len(p) == 5:
            if not p[4]:
                p[0] = [p[1], (p[3], 'asc')]
            else:
                p[0] = [p[1], (p[3], p[4])]

    def p_sort_type(self, p):
        '''
        sort_type : ASC
                | DESC
                | empty
        '''

        p[0] = p[1]

    def p_error(self, p):
        print('error while parsing your sql', p)

    def __init__(self):
        self.lexer = lexer()
        self.parser = yacc.yacc(module=self)


x = parser()


with open('test.sql') as f:
    v = x.parser.parse(f.read())

    for k in v:
        print("statement: ")
        print("\t", k)
