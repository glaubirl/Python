print('\n\nEXERCICIO 2')
print('--------------------------------------')
print('DESCUBRA SE O ANO É BISSEXTO.\n')
ano = int(input('Insira um ano para saber se é bissexto: '))

ano4 = ano % 4
ano100 = ano % 100
ano400 = ano % 400

if ano4 == 0 and ano100 != 0 or ano4 != 0 and ano400 == 0:
    print('O ano %d é bissexto' %ano)

else:
    print('O ano %d não é bissexto' %ano)
