num = (int(input('Digite o 1º número:')),
        int(input('Digite o 2º número:')),
        int(input('Digite o 3º número:')),
        int(input('Digite o 4º número:')))
print(f'Você digitou os números {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro 3 foi digitado na posição {num.index(3)+1}')
else:
    print('Nenhum número 3 foi digitado')
print('Números pares: ', end= '')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')