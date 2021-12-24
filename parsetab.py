
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startALL AND ARABIC_DOUBLE_QUOTE AS ASC BIGGER_THAN BIGGER_THAN_OR_EQUAL_TO BY COLUMN_NAME COLUMN_NUMBER COMAA COUNT DATASOURCE DELETE DESC DISTINCT DIVIDE DOT DOUBLE_QUOTE EQUAL FROM GROUP HAVING INNER INSERT INTO JOIN LBRACE LIMIT LPAREN L_SQ_BRACE MINUS NOT NUMBER OR ORDER PERCENT PLUS RBRACE RPAREN R_ARABIC_DOUBLE_QUOTE R_SQ_BRACE SELECT SET SIME_COLON SINGLE_QUOTE SMALLER_THAN SMALLER_THAN_OR_EQUAL_TO STRING SUM TIMES UPDATE VALUES WHEREstart : select\n    | insert\n    | update\n    | deleteexpression : expression PLUS termexpression : expression MINUS termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPARENempty :op : EQUAL\n    | BIGGER_THAN_OR_EQUAL_TO\n    | BIGGER_THAN\n    | SMALLER_THAN_OR_EQUAL_TO\n    | SMALLER_THANwhere : WHERE conditionwhere : emptycondition : expression op expressioncondition : LPAREN condition RPARENexpression : expression_termexpression_term : termterm : COLUMN_NAME\n    | NUMBER\n    | STRINGcondition : condition AND conditioncondition : condition OR conditioncondition : NOT conditionselect : SELECT column FROM data into where order SIME_COLONinto : INTO datainto : emptyhaving : HAVING condition\n    | emptyorder : ORDER BY orders\n    | emptyorders : column way\n    | orders COMAA ordersway : ASC\n    | DESC\n    | emptycolumn : TIMEScolumn : COLUMN_NAMEcolumn : DATASOURCEcolumn : column COMAA column\n    | emptydata : DATASOURCEinsert : INSERT INTO DATASOURCE icolumn VALUES LPAREN value RPAREN SIME_COLON\n    | INSERT INTO DATASOURCE icolumn LPAREN select RPAREN SIME_COLONvalue : STRINGvalue : NUMBERvalue : value COMAA valueicolumn : LPAREN COLUMN_NAME RPAREN\n    | emptyupdate : UPDATE DATASOURCE SET assigns where SIME_COLONassigns : column EQUAL value\n    | assigns COMAA assignsdelete : DELETE FROM DATASOURCE where SIME_COLON'
    
_lr_action_items = {'SELECT':([0,38,],[6,6,]),'INSERT':([0,],[7,]),'UPDATE':([0,],[8,]),'DELETE':([0,],[9,]),'$end':([1,2,3,4,5,43,59,96,99,104,],[0,-1,-2,-3,-4,-58,-55,-30,-49,-48,]),'TIMES':([6,19,21,41,48,50,51,52,53,89,90,92,93,94,95,97,105,],[11,11,11,11,77,-9,-24,-10,-26,77,77,-11,-7,-10,-8,11,11,]),'COLUMN_NAME':([6,19,21,27,32,41,46,47,64,65,66,67,68,69,70,71,72,73,88,97,105,],[12,12,12,39,51,12,51,51,51,51,51,51,51,-13,-14,-15,-16,-17,51,12,12,]),'DATASOURCE':([6,8,15,17,18,19,21,35,41,97,105,],[13,16,20,22,24,13,13,24,13,13,13,]),'FROM':([6,9,10,11,12,13,14,19,25,],[-12,17,18,-42,-43,-44,-46,-12,-45,]),'COMAA':([6,10,11,12,13,14,19,21,25,29,30,41,60,61,62,63,82,97,100,102,103,105,106,107,108,109,110,],[-12,19,-42,-43,-44,-46,-12,-12,19,41,19,-12,41,84,-50,-51,84,-12,84,105,19,-12,-37,-39,-40,-41,105,]),'INTO':([7,23,24,],[15,35,-47,]),'EQUAL':([11,12,13,14,19,21,25,30,41,45,48,49,50,51,52,53,75,89,90,92,93,94,95,],[-42,-43,-44,-46,-12,-12,-45,42,-12,69,-23,-22,-9,-24,-10,-26,69,-5,-6,-11,-7,-10,-8,]),'ASC':([11,12,13,14,19,25,97,103,105,],[-42,-43,-44,-46,-12,-45,-12,107,-12,]),'DESC':([11,12,13,14,19,25,97,103,105,],[-42,-43,-44,-46,-12,-45,-12,108,-12,]),'SIME_COLON':([11,12,13,14,19,22,23,24,25,29,31,33,34,36,40,44,48,49,50,51,52,53,54,55,60,61,62,63,76,79,81,83,85,86,87,89,90,91,92,93,94,95,97,98,100,102,103,105,106,107,108,109,110,],[-42,-43,-44,-46,-12,-12,-12,-47,-45,-12,43,-19,-12,-32,59,-18,-23,-22,-9,-24,-10,-26,-12,-31,-57,-56,-50,-51,-29,96,-36,99,-27,-28,-20,-5,-6,-21,-11,-7,-10,-8,-12,104,-52,-35,-12,-12,-37,-39,-40,-41,-38,]),'SET':([16,],[21,]),'LPAREN':([20,26,28,32,37,46,47,58,64,65,66,67,68,69,70,71,72,73,77,78,88,],[27,38,-54,46,56,46,46,-53,46,46,88,88,88,-13,-14,-15,-16,-17,88,88,88,]),'VALUES':([20,26,28,58,],[-12,37,-54,-53,]),'WHERE':([22,23,24,29,34,36,55,60,61,62,63,100,],[32,-12,-47,32,32,-32,-31,-57,-56,-50,-51,-52,]),'ORDER':([23,24,33,34,36,44,48,49,50,51,52,53,54,55,76,85,86,87,89,90,91,92,93,94,95,],[-12,-47,-19,-12,-32,-18,-23,-22,-9,-24,-10,-26,80,-31,-29,-27,-28,-20,-5,-6,-21,-11,-7,-10,-8,]),'NOT':([32,46,47,64,65,],[47,47,47,47,47,]),'NUMBER':([32,42,46,47,56,64,65,66,67,68,69,70,71,72,73,77,78,84,88,],[52,63,52,52,63,52,52,52,52,52,-13,-14,-15,-16,-17,94,94,63,52,]),'STRING':([32,42,46,47,56,64,65,66,67,68,69,70,71,72,73,84,88,],[53,62,53,53,62,53,53,53,53,53,-13,-14,-15,-16,-17,62,53,]),'RPAREN':([39,48,49,50,51,52,53,57,62,63,74,75,76,82,85,86,87,89,90,91,92,93,94,95,96,100,101,],[58,-23,-22,-9,-24,-10,-26,83,-50,-51,91,92,-29,98,-27,-28,-20,-5,-6,-21,-11,-7,-10,-8,-30,-52,92,]),'AND':([44,48,49,50,51,52,53,74,76,85,86,87,89,90,91,92,93,94,95,],[64,-23,-22,-9,-24,-10,-26,64,64,64,64,-20,-5,-6,-21,-11,-7,-10,-8,]),'OR':([44,48,49,50,51,52,53,74,76,85,86,87,89,90,91,92,93,94,95,],[65,-23,-22,-9,-24,-10,-26,65,65,65,65,-20,-5,-6,-21,-11,-7,-10,-8,]),'PLUS':([45,48,49,50,51,52,53,75,87,89,90,92,93,94,95,101,],[67,-23,-22,-9,-24,-10,-26,67,67,-5,-6,-11,-7,-10,-8,67,]),'MINUS':([45,48,49,50,51,52,53,75,87,89,90,92,93,94,95,101,],[68,-23,-22,-9,-24,-10,-26,68,68,-5,-6,-11,-7,-10,-8,68,]),'BIGGER_THAN_OR_EQUAL_TO':([45,48,49,50,51,52,53,75,89,90,92,93,94,95,],[70,-23,-22,-9,-24,-10,-26,70,-5,-6,-11,-7,-10,-8,]),'BIGGER_THAN':([45,48,49,50,51,52,53,75,89,90,92,93,94,95,],[71,-23,-22,-9,-24,-10,-26,71,-5,-6,-11,-7,-10,-8,]),'SMALLER_THAN_OR_EQUAL_TO':([45,48,49,50,51,52,53,75,89,90,92,93,94,95,],[72,-23,-22,-9,-24,-10,-26,72,-5,-6,-11,-7,-10,-8,]),'SMALLER_THAN':([45,48,49,50,51,52,53,75,89,90,92,93,94,95,],[73,-23,-22,-9,-24,-10,-26,73,-5,-6,-11,-7,-10,-8,]),'DIVIDE':([48,50,51,52,53,89,90,92,93,94,95,],[78,-9,-24,-10,-26,78,78,-11,-7,-10,-8,]),'BY':([80,],[97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'select':([0,38,],[2,57,]),'insert':([0,],[3,]),'update':([0,],[4,]),'delete':([0,],[5,]),'column':([6,19,21,41,97,105,],[10,25,30,30,103,103,]),'empty':([6,19,20,21,22,23,29,34,41,54,97,103,105,],[14,14,28,14,33,36,33,33,14,81,14,109,14,]),'data':([18,35,],[23,55,]),'icolumn':([20,],[26,]),'assigns':([21,41,],[29,60,]),'where':([22,29,34,],[31,40,54,]),'into':([23,],[34,]),'condition':([32,46,47,64,65,],[44,74,76,85,86,]),'expression':([32,46,47,64,65,66,88,],[45,75,45,45,45,87,101,]),'term':([32,46,47,64,65,66,67,68,88,],[48,48,48,48,48,48,89,90,48,]),'expression_term':([32,46,47,64,65,66,88,],[49,49,49,49,49,49,49,]),'factor':([32,46,47,64,65,66,67,68,77,78,88,],[50,50,50,50,50,50,50,50,93,95,50,]),'value':([42,56,84,],[61,82,100,]),'op':([45,75,],[66,66,]),'order':([54,],[79,]),'orders':([97,105,],[102,110,]),'way':([103,],[106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> select','start',1,'p_start','ply_yacc.py',24),
  ('start -> insert','start',1,'p_start','ply_yacc.py',25),
  ('start -> update','start',1,'p_start','ply_yacc.py',26),
  ('start -> delete','start',1,'p_start','ply_yacc.py',27),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','ply_yacc.py',36),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','ply_yacc.py',41),
  ('term -> term TIMES factor','term',3,'p_term_times','ply_yacc.py',51),
  ('term -> term DIVIDE factor','term',3,'p_term_div','ply_yacc.py',56),
  ('term -> factor','term',1,'p_term_factor','ply_yacc.py',61),
  ('factor -> NUMBER','factor',1,'p_factor_num','ply_yacc.py',66),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','ply_yacc.py',71),
  ('empty -> <empty>','empty',0,'p_empty','ply_yacc.py',81),
  ('op -> EQUAL','op',1,'p_op','ply_yacc.py',86),
  ('op -> BIGGER_THAN_OR_EQUAL_TO','op',1,'p_op','ply_yacc.py',87),
  ('op -> BIGGER_THAN','op',1,'p_op','ply_yacc.py',88),
  ('op -> SMALLER_THAN_OR_EQUAL_TO','op',1,'p_op','ply_yacc.py',89),
  ('op -> SMALLER_THAN','op',1,'p_op','ply_yacc.py',90),
  ('where -> WHERE condition','where',2,'p_where','ply_yacc.py',95),
  ('where -> empty','where',1,'p_where_empty','ply_yacc.py',100),
  ('condition -> expression op expression','condition',3,'p_condition','ply_yacc.py',105),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition_parens','ply_yacc.py',110),
  ('expression -> expression_term','expression',1,'p_expression','ply_yacc.py',115),
  ('expression_term -> term','expression_term',1,'p_expression_term','ply_yacc.py',120),
  ('term -> COLUMN_NAME','term',1,'p_term','ply_yacc.py',125),
  ('term -> NUMBER','term',1,'p_term','ply_yacc.py',126),
  ('term -> STRING','term',1,'p_term','ply_yacc.py',127),
  ('condition -> condition AND condition','condition',3,'p_condition_and','ply_yacc.py',132),
  ('condition -> condition OR condition','condition',3,'p_condition_or','ply_yacc.py',137),
  ('condition -> NOT condition','condition',2,'p_condition_not','ply_yacc.py',142),
  ('select -> SELECT column FROM data into where order SIME_COLON','select',8,'p_select','ply_yacc.py',154),
  ('into -> INTO data','into',2,'p_into','ply_yacc.py',199),
  ('into -> empty','into',1,'p_into_empty','ply_yacc.py',204),
  ('having -> HAVING condition','having',2,'p_having','ply_yacc.py',210),
  ('having -> empty','having',1,'p_having','ply_yacc.py',211),
  ('order -> ORDER BY orders','order',3,'p_order','ply_yacc.py',216),
  ('order -> empty','order',1,'p_order','ply_yacc.py',217),
  ('orders -> column way','orders',2,'p_orders','ply_yacc.py',222),
  ('orders -> orders COMAA orders','orders',3,'p_orders','ply_yacc.py',223),
  ('way -> ASC','way',1,'p_way','ply_yacc.py',228),
  ('way -> DESC','way',1,'p_way','ply_yacc.py',229),
  ('way -> empty','way',1,'p_way','ply_yacc.py',230),
  ('column -> TIMES','column',1,'p_column_all','ply_yacc.py',239),
  ('column -> COLUMN_NAME','column',1,'p_column_name','ply_yacc.py',244),
  ('column -> DATASOURCE','column',1,'p_column_number','ply_yacc.py',249),
  ('column -> column COMAA column','column',3,'p_columns','ply_yacc.py',254),
  ('column -> empty','column',1,'p_columns','ply_yacc.py',255),
  ('data -> DATASOURCE','data',1,'p_data','ply_yacc.py',262),
  ('insert -> INSERT INTO DATASOURCE icolumn VALUES LPAREN value RPAREN SIME_COLON','insert',9,'p_insert','ply_yacc.py',274),
  ('insert -> INSERT INTO DATASOURCE icolumn LPAREN select RPAREN SIME_COLON','insert',8,'p_insert','ply_yacc.py',275),
  ('value -> STRING','value',1,'p_value_string','ply_yacc.py',293),
  ('value -> NUMBER','value',1,'p_value_number','ply_yacc.py',298),
  ('value -> value COMAA value','value',3,'p_value','ply_yacc.py',303),
  ('icolumn -> LPAREN COLUMN_NAME RPAREN','icolumn',3,'p_icolumn','ply_yacc.py',308),
  ('icolumn -> empty','icolumn',1,'p_icolumn','ply_yacc.py',309),
  ('update -> UPDATE DATASOURCE SET assigns where SIME_COLON','update',6,'p_update','ply_yacc.py',321),
  ('assigns -> column EQUAL value','assigns',3,'p_assigns','ply_yacc.py',326),
  ('assigns -> assigns COMAA assigns','assigns',3,'p_assigns','ply_yacc.py',327),
  ('delete -> DELETE FROM DATASOURCE where SIME_COLON','delete',5,'p_delete','ply_yacc.py',339),
]
