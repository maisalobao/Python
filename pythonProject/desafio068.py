from random import randint
print('VAMOS JOGAR!')
jogador = computador = vitoria = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 11)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    print('-' * 20)
    print(f'Você jogou {jogador} e o PC {computador}. Total {soma}.')
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU')
            vitoria += 1
        else:
            print('Você PERDEU')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU')
            vitoria += 1
        else:
            print('Você PERDEU')
            break
    print('-' * 20)
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {vitoria} vezes')