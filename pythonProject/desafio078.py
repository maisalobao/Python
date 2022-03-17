lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
print(f'O maior valor foi {max(lista)} nas posições', end=' ')
for i,v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor valor foi {min(lista)} na posições', end=' ')
for i,v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
