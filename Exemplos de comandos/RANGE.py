## RANGE ##

#Comando que faz com que seja alocado na memória uma sequência de números
#determinado por parenteses. Há três formas de montar uma sequência.

#Dá para fazer uma range colocando apenas o limite do intervalo da sequência,
#nesse caso a sequência começa no zero e vai até 9, totalizando 10 números.
a = list(range(10))

#Outra forma é colocando dois valores no range para que o valor à esquerda seja o
#início e o da direita o final da sequência.
b = list(range(2,10))

#Outra maneira é colocando três valores, a regra das duas primeiras é a mesma da
#anterior, o que muda é o terceiro valor que faz os números pularem de 2 em 2.
c = list(range(0,10, 2))

print("%s \n\n%s \n\n%s" %(a, b, c))
