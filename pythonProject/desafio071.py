print('-'*10, 'CAIXA ELETRÔNICO', '-'*10)
valor = int(input('Qual o valor a ser sacado?'))
total = valor
cedula = 50
totcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
print('-'*20)
print('Volte sempre!')

