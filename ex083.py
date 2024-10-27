expressao = []
abreParentesis = 0
fechaParentesis = 0

resposta = str(input('Digite uma expressão: '))

for r in resposta:
    expressao.append(r)

    if r == '(':
        abreParentesis += 1 
    elif r == ')':
        fechaParentesis += 1


print(expressao)

if abreParentesis != fechaParentesis:
    print('Sua expressão está inválida!')
else:
    print('Sua expressão está válida!')