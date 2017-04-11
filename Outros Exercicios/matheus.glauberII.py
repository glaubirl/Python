print('\n\nEXERCICIO 1')
print('--------------------------------------')
print('DESCUBRA O TIPO DO TRIÂNGULO.\n')
lado_1 = int(input('Insira o primeiro lado: '))
lado_2 = int(input('Insira o segundo lado: '))
lado_3 = int(input('Insira o terceiro lado: '))

if (lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2):
    print('É possível formar um triângulo')
    if (lado_1 == lado_2 == lado_3):
        print('O triângulo é equilátero')
    elif (lado_1 == lado_2 != lado_3 or lado_3 == lado_1 != lado_2 or lado_2 == lado_3 != lado_1):
        print('O triângulo é isósceles')
    elif (lado_1 != lado_2 != lado_3):
        print('O triângulo é escaleno')
else:
    print('Não é possível formar um triângulo')

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

print('\n\nEXERCICIO 4')
print('--------------------------------------')
print('INSIRA TRÊS VALORES PARA QUE APAREÇA O DE MAIOR VALOR.\n')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
elif n3 >= n1 and n3 >= n2:
    print(n3)

print('\n\nEXERCICIO 5')
print('--------------------------------------')
print('INSIRA TRÊS VALORES PARA QUE SEJA MOSTRADO O DE MENOR VALOR.\n')

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))

if n1>= n2 and n1 >= n3:
    print('Maior valor: ', n1)
elif n2 >= n1 and n2 >= n3:
    print('Maior valor: ', n2)
elif n3>= n1 and n3 >= n2:
    print('Maior valor: ', n3)

if n1 <= n2 and n1 <= n3:
    print('Menor valor: ', n1)
elif n2 <= n1 and n2 <= n3:
    print('Menor valor: ', n2)
elif n3 <= n1 and n3 <= n2:
    print('Menor valor: ', n3)

print('\n\nEXERCICIO 6')
print('--------------------------------------')
print('CALCULE O SALÁRIO BRUTO E O SALÁRIO LÍQUIDO.\n')
ghr = int(input('Ganho por hora: '))
hrs = int(input('Horas trabalhadas: '))
sbruto = ghr * hrs
desconto = (11/100 * sbruto) + (8/100 * sbruto) + (5/100 * sbruto)
sliquido = sbruto - desconto
print('Salário Bruto: %.2f \nSalário Líquido: %.2f' %(sbruto, sliquido))

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
