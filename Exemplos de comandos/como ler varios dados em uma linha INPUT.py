#INTERESSANTE ESSA FITA DE PEGAR VÁRIOS VALORES EM UMA LINHA

'''A, B = [float(ue) for ue in input().split()]

print(A)
print(B)'''

'''A, B = [int(x) for x in input().split(" ")]

print(A)
print(B)'''

'''
entrada = input("Digite três números") # lendo os números
# quebrando a entrada em tokens separados por espaço (poderia ser outro separador)
numerosComoString = entrada.split(" ")
# criando uma nova lista com a conversão para float de cada número
numeros = [float(numero) for numero in numerosComoString] 

# atribuindo cada posição da lista a uma variável
a, b, c = numeros
triangulo = (a * c) / 2
print("TRIANGULO:", ("%.3f" % triangulo))
circulo = (3.14159 * c**2 )
print("CIRCULO:", ("%.3f" % circulo))
trapezio = ((a + b) * c) / 2
print ("TRAPEZIO:", ("%.3f" % trapezio))
quadrado = b * b
print ("QUADRADO:", ("%.3f" % quadrado))
retangulo = a * b

print ("RETANGULO:", ("%.3f" % retangulo))
'''
