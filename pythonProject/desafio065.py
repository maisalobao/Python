num = 0
pergunta = ''
cont = soma = media = 0
lista = []
while pergunta in 'Ss':
    num = int(input('Digite um número:'))
    pergunta = str(input('Deseja digitar mais valores? [S/N]')).upper().strip()[0]
    cont += 1
    soma += num
    media = soma / cont
    lista += [num]
print(f'Você digitou {cont} números. A média foi {media}')
print(f'O maior deles foi', max(lista), 'e o menor foi', min(lista))
