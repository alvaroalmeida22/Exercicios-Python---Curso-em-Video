frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece na posição {} pela primeira vez'.format(frase.find('A')+1))
print('A letra A aparece na posição {} pela ultima vez'.format(frase.rfind('A')+1))
