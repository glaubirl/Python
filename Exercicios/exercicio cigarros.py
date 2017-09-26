''' Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pegunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida a
cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias. '''

dia = int(input("Quantidade média de cigarros por dia: "))
anos = int(input("Por quantos anos fuma?: "))

total = ((dia * (anos * 366)) * 10) / 60

print(total/24)

#RESOLUÇÃO DO PROFESSOR:

'''
cigarros = int(input("Cigarros: "))
anos = int
vida_perdida = cigarros * anos * 365 
'''
