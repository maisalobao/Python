galera = list()
dados = list()
peso_tot = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg')))
    galera.append(dados[:])
    dados.clear()
    escolha = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if escolha in 'Nn':
        break
print('-' * 20)
print(f'{len(galera)} pessoas foram cadastradas.')
for peso in galera:
    peso_tot.append(peso[1])
print(f'Pesos cadastrados: {peso_tot}')
maiorpeso = max(peso_tot)
menorpeso = min(peso_tot)
print(f'O maior peso foi de {maiorpeso}kg.')
print(f'O menor peso foi de {menorpeso}kg.')
maiornome = list()
menornome = list()
for pes in galera:
    if pes[1] == maiorpeso:
        maiornome.append(pes[0])
    if pes[1] == menorpeso:
        menornome.append(pes[0])
print(f'O maior foi de {maiornome[0]}.')
print(f'O menor foi de {menornome[0]}.')
