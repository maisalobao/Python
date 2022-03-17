print('-' * 10, 'FEIRA DO MÊS', '-' * 10)
totalcompra = produtos10 = cont = menor = 0
while True:
    nome = str(input('Nome do produto:'))
    preço = float(input('Preço: R$'))
    escolha = ' '
    cont += 1
    totalcompra += preço
    if preço > 10:
        produtos10 += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total da compra: {totalcompra:.2f}')
print(f'{produtos10} custam mais de R$10,00')
print(f'O produto mais barato é {menor:.2f}')