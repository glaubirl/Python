## BREAK ##

#Serve para forçar a pausa de um ciclo.

x = 0
while(x<10):
    x+=1
    #Quando o valor de x é igual à 5 a mensagem de interropção é mostrado e o
    #'break' faz com que o loop do 'while' acabe.
    if(x==5):
        print("Interrompendo a execução da repetição.")
        break
    print(x)
print('Último valor de x: %d' %x, '\n')

#Se não tivesse o break, o ciclo seria realizado 10 vezes e o valor do x seria 10.


## CONTINUE ##

#'continue' faz com que as intruções sejam interrompidas, porém os ciclos continuam.

#Por exemplo:

#x é igual à zero
x = 0

#Se x menor e igual à 10 então...
while(x <= 10):

    #x = x + 1
    x+=1

    #Se o valor de 'x' não for divisível por 2, então as instruções continuarão e
    #'x' será mostrado na tela. Caso não seja divisível por 2, o 'continue' fará com
    #que as instruções deste bloco parem, porém o ciclo começará de novo e o 'x'
    #voltará com um novo valor até que não seja mais menor e igual a dez.
    if(x % 2== 0):
        continue
    print(x)

#Outro exemplo:

#Insere linha em branco
print()
print("inicio")
i = 0
while(i<10):
    i += 1
    #Se o número for divisível por 2, então a execução será cessada e o ciclo
    #retornará sendo que o 'i' terá um valor diferente.
    if(i%2==0):
        continue
    #Se o número for maior que 5 então a repetição para devido o 'break'.
    if(i>5):
        break
    print(i)
#O 'else' não será executado porque faz parte da repetição que é interrompida pelo
#'break'
else:
    print("else")
print("fim")
print()
