numeros = list()
while True:
    n = (int(input('Digite um valor:')))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado!')
    escolha = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if escolha in 'N':
        break
numeros.sort()
print(f'Você digitou {numeros}')