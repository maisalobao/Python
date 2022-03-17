numeros = [[], []]
valores = 0
for v in range(1,8):
    valores = int(input(f'Digite o {v}º valor:'))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
numeros[0].sort()
numeros[1].sort()
print(f'Apenas os pares: {numeros[0]}')
print(f'Apenas os ímpares: {numeros[1]}')
