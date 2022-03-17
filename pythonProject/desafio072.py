tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 0
while True:
    num = int(input('Digite um número de 0 a 20:'))
    if 0 <= num <= 20:
        break
print(f'Você escolheu o número {tupla[num]}')