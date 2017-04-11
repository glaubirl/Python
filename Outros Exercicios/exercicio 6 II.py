print('\n\nEXERCICIO 6')
print('--------------------------------------')
print('CALCULE O SALÁRIO BRUTO E O SALÁRIO LÍQUIDO.\n')
ghr = int(input('Ganho por hora: '))
hrs = int(input('Horas trabalhadas: '))
sbruto = ghr * hrs
desconto = (11/100 * sbruto) + (8/100 * sbruto) + (5/100 * sbruto)
sliquido = sbruto - desconto
print('Salário Bruto: %.2f \nSalário Líquido: %.2f' %(sbruto, sliquido))
