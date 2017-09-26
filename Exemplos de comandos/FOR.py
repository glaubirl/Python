## EXEMPLO DE FOR ##

#É um while "enrustido".

#Em for é dado uma variável que vai receber um valor a cada ciclo. Por exemplo,
#se a variável alocada for item e o ciclo 'in' for uma lista de 5 números, então
#a cada ciclo a variável terá um valor em ordem sequencial.

#Os valores 'in' são depositados na variável item (no for)

for item in [1,2,3,4,5]:
    print (item)

#Para realizar os ciclos, pode ser usado palavras (ciclo para cada caracter),
#listas (ciclo para cada elemento) e range (que vai definir o número de ciclos).

#Depois de completo o ciclo o valor da variável será igual ao último.
#Abaixo foi colocado marcador porque ao colocar o \n para pular linha, o número
#aparecia desalinhado na linha.

#Atenção: no print para separar itens é usado vírgula, mas se usar marcador a
#vírgula não é necessária.

print('\n%d' %item)
