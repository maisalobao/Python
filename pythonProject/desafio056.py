#Desafio: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

lista_idade = []
maior_idade_homem = 0
nome_velho = ''
mulheres20 = 0
for c in range(1,5):
    nome = str(input(f'Nome da {c}ª pessoa:')).strip()
    idade = int(input(f'Idade da {c}ª pessoa:'))
    sexo = str(input(f'Sexo da {c}ª pessoa:')).strip()
    lista_idade += [idade]
    soma = sum(lista_idade)
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
print(f'A média de idade entre eles é {soma/4}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres20} mulheres com menos de 20 anos.')
