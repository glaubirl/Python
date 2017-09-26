'''Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e
100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores. Imprima os três vetores'''

import random

principal = []
lista1 = []
lista2 = []

for x in range(10):
    lista1.append(random.randint(1,100))
    lista2.append(random.randint(1,100))
    principal.append(lista1[x])
    principal.append(lista2[x])

print('Lista 1: ', lista1)
print('Lista 2: ', lista2)
print('Lista Principal: ', principal)
