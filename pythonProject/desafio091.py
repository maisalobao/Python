import random
import time
from operator import itemgetter
print('-' * 30)
print(' '*5, 'JOGO DO DADO')
print('-' * 30)
jogo = dict()
jogo = {'jogador 1': random.randint(1,6),
        'jogador 2': random.randint(1,6),
        'jogador 3': random.randint(1,6),
        'jogador 4': random.randint(1,6)}
for k,v in jogo.items():
    print(f'{k}: tirou {v}')
    time.sleep(1)
print('-' * 30)
print('Ranking dos jogadores:')
ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1))
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)

