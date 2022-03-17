import random
import time
print('-' * 30)
print(' '*4, 'MEGA SENA DA VIRADA')
print('-' * 30)
quantidade = int(input('Quantos jogos deseja sortear?'))
print(f'-'*4, f'Sorteando {quantidade} jogos', '-'*4)
time.sleep(1)
jogo = list()
lista = list()
for q in range(0,quantidade):
    for n in range(1,7):
        num = random.randint(1,61)
        lista.append(num)
    jogo.append(lista[:])
    lista.clear()
for i, l in enumerate(jogo):
    print(f'Jogo {i}: {l}')
