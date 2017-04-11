print('\n\nEXERCICIO 1')
print('--------------------------------------')
print('INSIRA DOIS VALORES PARA SOMÁ-LOS.\n')
valor_1 = int(input ('Insira um valor: '))
valor_2 = int(input ('Insira outro valor: '))
print ('SOMA:', valor_1 + valor_2)


print('\n\nEXERCICIO 2')
print('--------------------------------------')
print('CONVERTA METROS PARA MILÍMETROS.\n')
metro_1 = int(input ('insira um valor em metros para transformar em milimetros: '))
print (metro_1 * 1000, 'milimetros')


print('\n\nEXERCICIO 3')
print('--------------------------------------')
print('INSIRA OS DADOS DE UM DIA PARA ENCONTRAR O TOTAL DE SEGUNDOS.\n')
dia = int(input ('Dia(s): '))
hora = int(input ('Hora(s): '))
minuto = int(input ('Minuto(s): '))
segundos = int(input ('Segundo(s)' ))
print ((dia * 24 * 3600) + (hora * 3600) + (minuto * 60) + (segundos))


print('\n\nEXERCICIO 4')
print('--------------------------------------')
print('CALCULE O VALOR DO SALÁRIO COM O AUMENTO.\n')
salario = int(input ('Digite o valor do salário: '))
aumento = int(input ('Digite em porcentagem o valor do aumento: '))
novo_salario = salario * aumento/100 + salario
print ('R$%.2f' %novo_salario)


print('\n\nEXERCICIO 5')
print('--------------------------------------')
print('CALCULE O VALOR DA MERCADORIA COM O DESCONTO.\n')
mercadoria = int(input ('Digite o valor da mercadoria: '))
desconto = int(input ('Digite em porcentagem o valor do desconto: '))
nova_mercadoria = mercadoria - mercadoria * (desconto/100)
print ('R$%.2f' %nova_mercadoria)


print('\n\nEXERCICIO 6')
print('--------------------------------------')
print('CALCULE O TEMPO DE UMA VIAGEM DE CARRO.\n')
distancia = int(input('Distância a ser percorrida: '))
velocidade_media = int(input('Velocidade média: '))
print ('O carro demorará ', distancia * velocidade_media)


print('\n\nEXERCICIO 7')
print('--------------------------------------')
print('CONVERTA CELSIUS PARA FAHRENHEIT.\n')
c = float(input('Insira a temperatura: '))
f = 9 * c / 5 + 32
print('%.2f F' %f)


print('\n\nEXERCICIO 8')
print('--------------------------------------')
print('CONVERTA FAHRENHEIT PARA CELSIUS.\n')
f = float(input('Insira a temperatura: '))
c = (f - 32) / 1.8
print('%.2f C' %c)


print('\n\nEXERCICIO 9')
print('--------------------------------------')
print('CALCULE O VALOR DO ALUGUEL DO CARRO.\n')
km_percorridos = int(input('Kilômetros percorridos: '))
dias = int(input('Quantidade de dias em que o carro foi utilizado: '))
pagar = 60 * dias + km_percorridos * 0.15
print('O aluguel do carro custou R$%.2f' %pagar)


print('\n\nEXERCICIO 10')
print('--------------------------------------')
print('CALCULE A QUANTIDADE DE TEMPO QUE UM FUMANTE PERDE DE VIDA.\n')
c = float(input('Total de cigarros: '))
d = float(input('Tempo(em dias) que fuma: '))
tp = (c*10)/60 /24
print ("\nPerdeu %f de dias de vida :(" %tp)


print ('\n\nEXERCICIO 11')
print('--------------------------------------')
print('QUANTIDADE DE DIGITOS QUE 2 ELEVADO À 1.000.000 TEM.\n')
numero = str(2 ** 1000000)
print (len(numero))
