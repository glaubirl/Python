import random

lista = []

for x in range(10):
    lista.append(random.randint(1, 100))

print(lista)

maior = lista[0]

menor = maior

for i in lista[1:]:
    if i > maior:
        maior = i
    if i < menor:
        menor = x

print('Menor: ', menor)
print('Maior: ', maior)
print(lista)
