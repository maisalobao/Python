time = []
jogo = {}
gols = []
num = total = 0
while True:
    jogo.clear()
    jogo['nome'] = str(input('Nome do Jogador:'))
    partidas = int(input(f'Quantas partidas {jogo["nome"]} jogou?'))
    gols.clear()
    for c in range(0,partidas):
        num = int(input(f'Quantos gols na partida {c}:'))
        gols.append(num)
    jogo['gols'] = gols[:]
    jogo['total'] = sum(gols)
    time.append(jogo.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Erro! Responda S ou N.')
    if escolha == 'N':
        break
print('-' * 40)
print(f'{"Cod.":<5}{"Nome":<12}{"Gols":<12}{"Total":<6}')
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<12} ', end='')
    print()
print('-'* 40)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para)'))
    if jogador == 999:
        break
    if jogador > len(time):
        print('Erro! Esse jogador não existe. Tente novamente.')
    if jogador < len(time):
        print(f'Levantamento do jogador {time[jogador]["nome"]}:')
        for i, v in enumerate(time[jogador]['gols']):
                print(f'No jogo {i} fez {v} gols')
    print('-'* 40)
print('VOLTE SEMPRE')
