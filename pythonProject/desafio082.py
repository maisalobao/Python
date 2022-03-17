num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor:')))
    escolha = str(input('Deseja continuar?')).upper().strip()[0]
    if escolha in 'N':
        break
print(f'Os valores da lista são: {num}')
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Apenas os pares: {pares}')
print(f'Apenas os ímpares: {impares}')