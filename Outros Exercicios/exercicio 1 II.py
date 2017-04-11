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
