lista = []
while True:
    lista.append(int(input('Digite um número:')))
    escolha = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if escolha in 'N':
        break
print(f'A lista tem {len(lista)} elementos')
lista.sort(reverse=True)
print(f'De forma decrescente: {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado e não está na lista.')