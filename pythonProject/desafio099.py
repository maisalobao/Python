from time import sleep
def maior(*num):
    cont = maior = 0
    print('-' * 45)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print('Foram os valores informados')
    print(f'O maior valor informado foi {maior}')
    

#Programa principal
maior(2, 9, 3, 4, 6)
maior(4, 7, 2, 1)
maior(8, 9)