## LISTAS ##

#É possível colocar vários elementos em uma só variável, criando assim uma lista.
#Por exemplo, se em westeros existem várias famílias é possível criar uma lista 
#'westeros' e inserir nela o nome de todas famílias, pois fazem parte do mesmo
#grupo.

westeros = ['Stark', 'Targaryen', 'Lannister', 'Bolton', 'Tully']
print(westeros,'\n')

#Para acessar à uma família em específico da lista, é preciso usar índice para
#informar a posição do elemento na lista e assim acessá-lo.

print('Segunda família: %s' %westeros[1],'\n')

#Lembrando que o primeiro elemento é zero(0).

#É possível acessar também usando fatiamento.

print(westeros[1:4],'\n')

#Para adicionar mais um elemento à lista é usado o método '.append', sua sintaxe é
#o_nome_da_lista.append('elemento a ser adicionado')

westeros.append('Greyjoy')
print(westeros)
print('\nQuinta família: %s' %westeros[4], '\n')

#É possível criar uma lista vazia e adicionar elementos depois.

lista = []
entrada = input('Digite qualquer coisa: ')
lista.append(entrada)
print('Lista -> ', lista, '\n')

#Mudar o valor de um elemento
westeros[3] = 'Tyrell'
print(westeros[3])
print(westeros, '\n')

'''É possível remover algum item da lista utilizando o método remove e o
conteúdo ou o índice do conteúdo como método'''
westeros.remove('Lannister') print(westeros)
westeros.remove(westeros[3]) print(westeros)

#Printar cada posição em linhas diferentes
for x in westeros: print(x)

#O westeros[::2] faz com que as posições printadas seja a cada duas posições.
print(westeros[::2]
