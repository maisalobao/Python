from time import sleep
def contador(i, f, p):
    print('-' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for p in range(i, f+1, p):
        print(p, end=' ')
        sleep(0.5)
    print()

#Programa principal
contador(1, 10, 1)
contador(-10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
if p == 0:
    p = 1

contador(i, f, p)