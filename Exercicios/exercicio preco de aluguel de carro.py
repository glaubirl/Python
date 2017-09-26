'''
Programa que calcula através de km e dias o preço do Aluguel de um carro.
'''

km = int(input("Quantidade de km percorridos pelo carro alugado: "))
dias = int(input("Quantidade de dias que o carro foi usado: "))

print("R$: %.2f" %(km * 0.15 + dias * 60))
