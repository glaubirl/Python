print('\n\nEXERCICIO 3')
print('--------------------------------------')
print('CALCULAR SE HÁ EXCESSO DE PESO NA PESCARIA E SE HOUVER CALCULAR O VALOR DA MULTA.\n')
peso = int(input('Digite o peso da pesca: '))

multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print('Peso:%d \nExcesso:%d  \nMulta: R$%.2f' %(peso, excesso, multa))
