preço = float(input("Preço: "))
desconto = float(input("Desconto: "))
desconto_dado = preço * desconto / 100
print ("Desconto dado: %.2f" %desconto_dado)
print ("A pagar: %.2f" %(preço - desconto_dado))
