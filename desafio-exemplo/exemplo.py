total18 = totalmulher20 = homens = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'{total18} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'E {totalmulher20} mulheres têm menos de 20 anos.')
