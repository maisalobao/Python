palavras = ('cafe', 'açucar', 'pao', 'queijo')
for item in palavras:
    print(f'\nNa palavra {item} temos = ', end='')
    if 'a' in item:
       print('a', end=' ')
    if 'e' in item:
        print('e', end=' ')
    if 'i' in item:
        print('i', end=' ')
    if 'o' in item:
        print('o', end=' ')
    if 'u' in item:
        print('u')