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
