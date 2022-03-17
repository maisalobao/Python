from random import randint
n1 = (randint(1,20), randint(1,20), randint(1,20),
      randint(1,20), randint(1,20))
print(n1)
print(f'O menor número sorteado foi', min(n1))
print(f'O maior número sorteado foi', max(n1))