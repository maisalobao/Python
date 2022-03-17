matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna = maiorlinha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite o valor da posição [{l},{c}]')))
print('-'*40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^2}]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
print('-'*40)
print(f'A soma dos valores pares é {somapares}.')
for l in range(0,3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}.')
maiorlinha = max(matriz[1])
print(f'O maior valor da segunda linha é {maiorlinha}')
