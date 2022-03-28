#Desafio: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha in 'Nn':
        break
print('-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":<7}')
print('-' * 30)
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>6}')
print('-' * 30)
while True:
    notas = int(input('Deseja ver a nota de qual aluno? (999 interrompe)'))
    if notas == 999:
        break
    for i,v in enumerate(lista):
        if i == notas:
            print(f'As notas de {v[0]} são {v[1]}.')
print('VOLTE SEMPRE')
