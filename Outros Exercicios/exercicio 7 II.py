print('\n\nEXERCICIO 7')
print('--------------------------------------')
print('QUANTIDADE DE LATAS(18L) NECESSÁRIAS PARA PINTAR UMA ÁREA EM M² E O VALOR TOTAL.\n')
am2 = int(input('Área em metros quadrados: '))
litros = am2/3
latas = int(litros)/18
if litros % 18 != 0:
    latas += 1
preço = int(latas) * 80
print('Será necessário comprar %d lata(s), que custará(ão) R$%.2f' %(latas, preço))
