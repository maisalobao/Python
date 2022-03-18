def area(l, c):
     area = l * c
     print(f'A área de um terreno {l}x{c} é de {area}m²')


#Programa Princial
print('CONTROLE DE TERRENOS')
print('-' * 30)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m):'))
area(l, c)
