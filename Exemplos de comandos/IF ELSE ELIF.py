# IF, ELSE, ELIF #

#Comandos em que só é realizado as instruções se a condição for respeitadas.

#Nas instruções abaixo é dado uma variável de valor 'a' igual à 2.
#A condição 'if'(se) faz com que as instruções identadas à ela sejam só executadas
#se 'a' for menor que 3, senão as instruções não são executadas, como é o caso do
#segundo 'if' que contém uma condição falsa, então sua instrução não será executada.

a = 2

if a < 3:
    print(a, '\n')

if 3 < 2:
    print('Impossível')

b = int(input('Digite um valor e compare com 5: '))

if b < 5:
    print("O número inserido é menor que 5.\n")

#O else faz com que as outras condições possíveis sejam consideradas e executa
#as instruções somente se as condições do 'if' forem falsas.
else:
    print("O número não é menor que 5, é maior ou igual.\n")

#As linhas de comando abaixo é importante, pois mostram a importância do 'elif'.

#Nas instruções C o 'elif' não é usado, então quando é colocado o else, ele só
#considera o 'if' anterior, o que faz com que o outro if seja considerado nas
#condições do else, fazendo com que suas instruções também sejam executadas.
#Na instrução D é usado o elif, fazendo com que o 'else' entenda que os outros
#'if' não fazem parte das condições restantes.

#O 'elif' é uma junção do 'if' e 'else'.

#Instruções C
c = int(input("Insira um valor e compare com 10: "))

if c < 10:
    print('É menor que 10.\n')
if c == 10:
    print("É igual à 10.\n")
else:
    print("É maior que 10.\n")

#Instruções D
d = int(input("Insira um valor e compare com 10: "))

if d < 10:
    print('É menor que 10.\n')
elif d == 10:
    print("É igual à 10.\n")
else:
    print("É maior que 10.\n")

letras = []
i = 1
while i <= 10:
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    #O not in faz com que as letras 'aeiou' sejam desconsideradas, realizando o
    #ciclo somente se a letra for diferente de uma delas.
    if letras[i] not in 'aeiou':
        cont += 1
    i += 1
print("Foram lidos %d consoantes" %cont)
