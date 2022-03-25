n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
lista = [n1, n2]
menu = 0
print('=' * 5)
while menu < 5:
    menu = int(input('MENU \n [1] Somar \n [2] Multiplicar \n [3] Mairo \n [4] Novos números\n [5] Sair do programa'))
    if menu == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}.')
    if menu == 2:
        print(f'A multiplicação de {n1} * {n2} é {n1*n2}.')
    if menu == 3:
        print(f'Entre {n1} e {n2} o maior é', max(lista))
    if menu == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    if menu == 5:
        print('Até mais!')
    else:
        print('Digite números entre 1 e 5')