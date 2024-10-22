nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {} a média do aluno é {}.'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está \033[1:31mREPROVADO!\033[m')
elif 5 <= media < 7:
    print('O aluno está em \033[1:33mRECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está \033[1:32mAPROVADO!')
