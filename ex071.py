notaCinquenta = notaDez = notaUm = 0

saque = int(input('Qual valor você quer sacar? R$'))
saqueTot = saque
cedula = 50
totCedula = 0
while True:
    if saqueTot >= cedula:
        saqueTot -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if saqueTot == 0:
            break
