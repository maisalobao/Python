from random import randint
from time import sleep
from emoji import emojize
r = 0
num = ''
while num != r:
    num = int(input('Vou pensar em um número entre 0 e 10. Tente advinhar:'))
    r = randint(0,10)
    print('PROCESSANDO...')
    sleep(2)
    if num == r:
        print(emojize('Você venceu! PARABÉNS :red_heart:'))
    else:
        print(emojize(f'Você perdeu! O número certo era {r}. Tente novamente.:thumbs_up:'))
    print('Nos vemos na próxima!')
    print('_' * 10)