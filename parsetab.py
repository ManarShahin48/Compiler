
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startALL AND ARABIC_DOUBLE_QUOTE AS ASC BIGGER_THAN BIGGER_THAN_OR_EQUAL_TO BY COLUMN_NAME COLUMN_NUMBER COMAA COUNT DATASOURCE DELETE DESC DISTINCT DIVIDE DOT DOUBLE_QUOTE EQUAL EQUAL_EQUAL FROM GROUP HAVING INNER INSERT INTO JOIN LBRACE LIMIT LPAREN L_SQ_BRACE MINUS NOT NUMBER OR ORDER PERCENT PLUS RBRACE RPAREN R_ARABIC_DOUBLE_QUOTE R_SQ_BRACE SELECT SET SIME_COLON SINGLE_QUOTE SMALLER_THAN SMALLER_THAN_OR_EQUAL_TO STRING SUM TIMES UPDATE VALUES WHEREstart : select\n    | update\n    | deleteexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPARENempty :where : WHERE conditionwhere : emptycondition : expression op expressioncondition : LPAREN condition RPARENexpression : COLUMN_NAME\n    | NUMBER\n    | stringstring : STRINGop : EQUAL\n    | EQUAL_EQUAL\n    | BIGGER_THAN_OR_EQUAL_TO\n    | BIGGER_THAN\n    | SMALLER_THAN_OR_EQUAL_TO\n    | SMALLER_THANcondition : condition AND conditioncondition : condition OR conditioncondition : NOT conditionselect : SELECT column FROM data into where order SIME_COLONinto : INSERT datainto : emptyorder : ORDER BY ASCorder : emptycolumn : TIMEScolumn : COLUMN_NAMEcolumn : DATASOURCEcolumn : column COMAA column\n    | emptydata : DATASOURCEvalue : STRINGvalue : NUMBERvalue : value COMAA valueicolumn : emptyicolumn : COLUMN_NAMEicolumn : icolumn COMAA icolumnupdate : UPDATE data SET assigns where SIME_COLONassigns : column EQUAL value\n    | assigns COMAA assignsdelete : DELETE FROM data where SIME_COLON'
    
_lr_action_items = {'SELECT':([0,],[5,]),'UPDATE':([0,],[6,]),'DELETE':([0,],[7,]),'$end':([1,2,3,4,33,46,82,],[0,-1,-2,-3,-50,-47,-30,]),'TIMES':([5,17,18,31,38,40,42,75,76,77,79,80,81,],[9,9,9,9,65,-10,-9,65,-10,65,-11,-7,-8,]),'COLUMN_NAME':([5,17,18,25,31,36,37,51,52,53,56,57,58,59,60,61,74,],[10,10,10,39,10,39,39,39,39,39,-21,-22,-23,-24,-25,-26,39,]),'DATASOURCE':([5,6,15,16,17,18,28,31,],[11,14,14,14,11,11,14,11,]),'FROM':([5,7,8,9,10,11,12,17,21,],[-12,15,16,-35,-36,-37,-39,-12,-38,]),'COMAA':([5,8,9,10,11,12,17,18,21,22,23,31,47,48,49,50,84,],[-12,17,-35,-36,-37,-39,-12,-12,17,31,17,-12,31,70,-41,-42,70,]),'EQUAL':([9,10,11,12,17,18,21,23,31,35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[-35,-36,-37,-39,-12,-12,-38,32,-12,56,-6,-17,-10,-19,-9,-20,56,-4,-10,-5,-11,-7,-8,]),'SET':([13,14,],[18,-40,]),'WHERE':([14,19,20,22,27,29,45,47,48,49,50,84,],[-40,25,-12,25,25,-32,-31,-49,-48,-41,-42,-43,]),'SIME_COLON':([14,19,20,22,24,26,27,29,30,34,38,39,40,41,42,43,44,45,47,48,49,50,64,67,69,71,72,73,75,76,77,78,79,80,81,84,86,],[-40,-12,-12,-12,33,-14,-12,-32,46,-13,-6,-17,-10,-19,-9,-20,-12,-31,-49,-48,-41,-42,-29,82,-34,-27,-28,-15,-4,-10,-5,-16,-11,-7,-8,-43,-33,]),'INSERT':([14,20,],[-40,28,]),'ORDER':([14,20,26,27,29,34,38,39,40,41,42,43,44,45,64,71,72,73,75,76,77,78,79,80,81,],[-40,-12,-14,-12,-32,-13,-6,-17,-10,-19,-9,-20,68,-31,-29,-27,-28,-15,-4,-10,-5,-16,-11,-7,-8,]),'LPAREN':([25,36,37,51,52,53,54,55,56,57,58,59,60,61,65,66,74,],[36,36,36,36,36,74,74,74,-21,-22,-23,-24,-25,-26,74,74,74,]),'NOT':([25,36,37,51,52,],[37,37,37,37,37,]),'NUMBER':([25,32,36,37,51,52,53,54,55,56,57,58,59,60,61,65,66,70,74,],[40,50,40,40,40,40,40,76,76,-21,-22,-23,-24,-25,-26,76,76,50,40,]),'STRING':([25,32,36,37,51,52,53,56,57,58,59,60,61,70,74,],[43,49,43,43,43,43,43,-21,-22,-23,-24,-25,-26,49,43,]),'AND':([34,38,39,40,41,42,43,62,64,71,72,73,75,76,77,78,79,80,81,],[51,-6,-17,-10,-19,-9,-20,51,51,51,51,-15,-4,-10,-5,-16,-11,-7,-8,]),'OR':([34,38,39,40,41,42,43,62,64,71,72,73,75,76,77,78,79,80,81,],[52,-6,-17,-10,-19,-9,-20,52,52,52,52,-15,-4,-10,-5,-16,-11,-7,-8,]),'PLUS':([35,38,39,40,41,42,43,63,73,75,76,77,79,80,81,85,],[54,-6,-17,-10,-19,-9,-20,54,54,-4,-10,-5,-11,-7,-8,54,]),'MINUS':([35,38,39,40,41,42,43,63,73,75,76,77,79,80,81,85,],[55,-6,-17,-10,-19,-9,-20,55,55,-4,-10,-5,-11,-7,-8,55,]),'EQUAL_EQUAL':([35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[57,-6,-17,-10,-19,-9,-20,57,-4,-10,-5,-11,-7,-8,]),'BIGGER_THAN_OR_EQUAL_TO':([35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[58,-6,-17,-10,-19,-9,-20,58,-4,-10,-5,-11,-7,-8,]),'BIGGER_THAN':([35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[59,-6,-17,-10,-19,-9,-20,59,-4,-10,-5,-11,-7,-8,]),'SMALLER_THAN_OR_EQUAL_TO':([35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[60,-6,-17,-10,-19,-9,-20,60,-4,-10,-5,-11,-7,-8,]),'SMALLER_THAN':([35,38,39,40,41,42,43,63,75,76,77,79,80,81,],[61,-6,-17,-10,-19,-9,-20,61,-4,-10,-5,-11,-7,-8,]),'RPAREN':([38,39,40,41,42,43,62,63,64,71,72,73,75,76,77,78,79,80,81,85,],[-6,-17,-10,-19,-9,-20,78,79,-29,-27,-28,-15,-4,-10,-5,-16,-11,-7,-8,79,]),'DIVIDE':([38,40,42,75,76,77,79,80,81,],[66,-10,-9,66,-10,66,-11,-7,-8,]),'BY':([68,],[83,]),'ASC':([83,],[86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'select':([0,],[2,]),'update':([0,],[3,]),'delete':([0,],[4,]),'column':([5,17,18,31,],[8,21,23,23,]),'empty':([5,17,18,19,20,22,27,31,44,],[12,12,12,26,29,26,26,12,69,]),'data':([6,15,16,28,],[13,19,20,45,]),'assigns':([18,31,],[22,47,]),'where':([19,22,27,],[24,30,44,]),'into':([20,],[27,]),'condition':([25,36,37,51,52,],[34,62,64,71,72,]),'expression':([25,36,37,51,52,53,74,],[35,63,35,35,35,73,85,]),'term':([25,36,37,51,52,53,54,55,74,],[38,38,38,38,38,38,75,77,38,]),'string':([25,36,37,51,52,53,74,],[41,41,41,41,41,41,41,]),'factor':([25,36,37,51,52,53,54,55,65,66,74,],[42,42,42,42,42,42,42,42,80,81,42,]),'value':([32,70,],[48,84,]),'op':([35,63,],[53,53,]),'order':([44,],[67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> select','start',1,'p_start','ply_yacc.py',28),
  ('start -> update','start',1,'p_start','ply_yacc.py',29),
  ('start -> delete','start',1,'p_start','ply_yacc.py',30),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','ply_yacc.py',39),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','ply_yacc.py',44),
  ('expression -> term','expression',1,'p_expression_term','ply_yacc.py',49),
  ('term -> term TIMES factor','term',3,'p_term_times','ply_yacc.py',54),
  ('term -> term DIVIDE factor','term',3,'p_term_div','ply_yacc.py',59),
  ('term -> factor','term',1,'p_term_factor','ply_yacc.py',64),
  ('factor -> NUMBER','factor',1,'p_factor_num','ply_yacc.py',69),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','ply_yacc.py',74),
  ('empty -> <empty>','empty',0,'p_empty','ply_yacc.py',84),
  ('where -> WHERE condition','where',2,'p_where','ply_yacc.py',89),
  ('where -> empty','where',1,'p_where_empty','ply_yacc.py',94),
  ('condition -> expression op expression','condition',3,'p_condition','ply_yacc.py',99),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition_parens','ply_yacc.py',104),
  ('expression -> COLUMN_NAME','expression',1,'p_expression','ply_yacc.py',109),
  ('expression -> NUMBER','expression',1,'p_expression','ply_yacc.py',110),
  ('expression -> string','expression',1,'p_expression','ply_yacc.py',111),
  ('string -> STRING','string',1,'p_string','ply_yacc.py',116),
  ('op -> EQUAL','op',1,'p_op','ply_yacc.py',121),
  ('op -> EQUAL_EQUAL','op',1,'p_op','ply_yacc.py',122),
  ('op -> BIGGER_THAN_OR_EQUAL_TO','op',1,'p_op','ply_yacc.py',123),
  ('op -> BIGGER_THAN','op',1,'p_op','ply_yacc.py',124),
  ('op -> SMALLER_THAN_OR_EQUAL_TO','op',1,'p_op','ply_yacc.py',125),
  ('op -> SMALLER_THAN','op',1,'p_op','ply_yacc.py',126),
  ('condition -> condition AND condition','condition',3,'p_condition_and','ply_yacc.py',131),
  ('condition -> condition OR condition','condition',3,'p_condition_or','ply_yacc.py',136),
  ('condition -> NOT condition','condition',2,'p_condition_not','ply_yacc.py',141),
  ('select -> SELECT column FROM data into where order SIME_COLON','select',8,'p_select','ply_yacc.py',153),
  ('into -> INSERT data','into',2,'p_into','ply_yacc.py',232),
  ('into -> empty','into',1,'p_into_empty','ply_yacc.py',237),
  ('order -> ORDER BY ASC','order',3,'p_order_asc','ply_yacc.py',243),
  ('order -> empty','order',1,'p_order_empty','ply_yacc.py',248),
  ('column -> TIMES','column',1,'p_column_all','ply_yacc.py',292),
  ('column -> COLUMN_NAME','column',1,'p_column_name','ply_yacc.py',297),
  ('column -> DATASOURCE','column',1,'p_column_number','ply_yacc.py',302),
  ('column -> column COMAA column','column',3,'p_columns','ply_yacc.py',307),
  ('column -> empty','column',1,'p_columns','ply_yacc.py',308),
  ('data -> DATASOURCE','data',1,'p_data','ply_yacc.py',315),
  ('value -> STRING','value',1,'p_value_string','ply_yacc.py',355),
  ('value -> NUMBER','value',1,'p_value_number','ply_yacc.py',360),
  ('value -> value COMAA value','value',3,'p_value','ply_yacc.py',365),
  ('icolumn -> empty','icolumn',1,'p_icolumn_empty','ply_yacc.py',370),
  ('icolumn -> COLUMN_NAME','icolumn',1,'p_icolumn_name','ply_yacc.py',375),
  ('icolumn -> icolumn COMAA icolumn','icolumn',3,'p_icolumns','ply_yacc.py',380),
  ('update -> UPDATE data SET assigns where SIME_COLON','update',6,'p_update','ply_yacc.py',394),
  ('assigns -> column EQUAL value','assigns',3,'p_assigns','ply_yacc.py',399),
  ('assigns -> assigns COMAA assigns','assigns',3,'p_assigns','ply_yacc.py',400),
  ('delete -> DELETE FROM data where SIME_COLON','delete',5,'p_delete','ply_yacc.py',412),
]
