import shlex

print('Please Enter Your Statement: ')
statement = input()

print('\nBefore Spilting into Tokens: \n', repr(statement))
print('\nAfter Spilting into Tokens: ')
lexer = shlex.shlex(statement)

TokenList = []
for Token in lexer:
    TokenList.append(Token)

coun =  0
for Token in TokenList:
    coun += 1
    result = 'Tokin ' + str(coun) + ' is ' + repr(Token)
    print(result)
    
print('\nMission is DONE ✅')
