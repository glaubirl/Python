'''GERAR UMA LISTA COM 15 ELEMENTOS NÃO REPETIDOS'''

'''
import random

lista = []

for k in range(15):
    num = random.randint(1, 20)
    while(True):
        if num not in lista:
            lista.append(num)
            continue

print(lista)
'''

'''Q bonito acertei uma sintaxe que inventei de primeira :')'''
'''Não não acertei não, precisa do while'''

'''Feito pelo professor'''
import random

lista = []

while len(lista) < 15: #O ciclo continuará enquanto a lista for menor que 15
    x = random.randint(1, 20)
    if x not in lista:
        lista.append(x) #A lista só aumentará de tamanho quando for adicionado
        #elemento, e o elemento só é adicionado quando verificado que ele não
        #existe na lista.

lista.sort()
print(lista)
