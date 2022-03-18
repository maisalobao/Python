jogo = {}
gols = []
total = 0
jogo['nome'] = str(input('Nome do Jogador:'))
partidas = int(input(f'Quantas partidas {jogo["nome"]} jogou?'))
if partidas > 0:
    for c in range(0,partidas):
        num = int(input(f'Quantos gols na partida {c}:'))
        gols.append(num)
        jogo['gols'] = gols
        total += num
        jogo['total'] = total
print('-' * 30)
print(jogo)
print('-' * 30)
for k, v in jogo.items():
    print(f'O campo {k} tem valor {v}')
print('-' * 30)
print(f'O jogador {jogo["nome"]} jogou {partidas} partidas')
for i,v in enumerate(jogo['gols']):
    print(f'Na partida {i}, fez {v} gols')
