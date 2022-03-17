print('-'*10, 'TABUADA', '-'*10)
n = 0
while True:
    num = int(input('Digite um número:'))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
print('Programa Tabuada encerrado. Até mais!')
