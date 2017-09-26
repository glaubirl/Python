notas = [9, 2, 7, 8, 8]
menor = 10
x = 0

while(x < 5):
    if(notas[x] < menor):
        menor = x

lista.remove(menor)

print(lista)
