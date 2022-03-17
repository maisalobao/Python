feira = ('Pão', 2, 'Sorda', 4, 'Queijo', 12.75)
print('_' * 40)
print(' '*10, 'FEIRA NA PADARIA', ' '*10)
print('-' * 40)
for pos in range(0, len(feira)):
    if pos % 2 == 0:
        print(f'{feira[pos]:.<30}', end='')
    else:
        print(f'R${feira[pos]}')
print('_' * 40)
