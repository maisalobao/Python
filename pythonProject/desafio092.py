from datetime import date
atual = date.today().year
ficha = {}
ficha['nome'] = str(input('Nome:'))
ano = int(input('Ano de nascimento:'))
ficha['idade'] = atual - ano
ficha['ctps'] = int(input('CTPS (0 p/ não tem):'))
if ficha['ctps'] > 0:
    ficha['contratação'] = int(input('Ano de contratação:'))
    ficha['salario'] = float(input('Salário:'))
    ano_aposentadoria = ficha['contratação'] + 35
    ficha['aposentadoria'] = ano_aposentadoria - ano
for k, v in ficha.items():
    print(f'{k}: {v}')

