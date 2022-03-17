brasileirao = ('Palmeiras', 'Flamengo', 'Internacional',
               'Grêmio', 'São Paulo', 'Atlético', 'Athletico',
               'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense',
               'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport',
               'América', 'Vitoria', 'Paraná')
print(f'Os primeiros 5 são: {brasileirao[:5]}')
print(f'Os últimos 4 são: {brasileirao[15:]}')
print(f'Em ordem alfabética: {sorted(brasileirao)}')
print(f'O chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.')
