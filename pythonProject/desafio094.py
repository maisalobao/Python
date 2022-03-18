lista = list()
dicionario = dict()
soma = media = 0
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome:'))
    while True:
        dicionario['sexo'] = str(input('Sexo:')).strip().upper()[0]
        if dicionario['sexo'] in 'MF':
            break
        print('Erro! Digite M ou F.')
    dicionario['idade'] = int(input('Idade:'))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Erro! Digite S ou N.')
    if escolha == 'N':
        break
print(lista)
print('-' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
media = soma / len(lista)
print(f'A média de idade é {media}.')
print(f'Mulheres cadastradas:', end=' ')
for dicionario in lista:
    if dicionario['sexo'] == 'F':
        print(f'{dicionario["nome"]}', end=' ')
print('\nLista das pessoas que estão acima da média:')
for dicionario in lista:
    if dicionario['idade'] > media:
        print(f'nome = {dicionario["nome"]}; sexo = {dicionario["sexo"]}; idade = {dicionario["idade"]};')
print('-' * 30)
print('<< ENCERRADO >>')
