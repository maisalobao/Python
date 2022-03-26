from random import randint
from time import sleep

def sorteia(sorte):
    for c in range(1, 6):
        sorte.append(randint(1, 10))
    print(f'Sorteando os valores da lista:', end=' ')
    for v in sorte:
        print(f'{v}', end=' ')
        sleep(0.3)
    print()


def somaPar(n2):
    soma = 0
    for valor in numeros:
        if valor % 2 ==0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}.')

#Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)
