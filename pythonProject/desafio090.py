aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input('Média:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
for i, v in aluno.items():
    print(f'{i} = {v}')
