'''Supondo que a população de um país A seja da ordem de  80000
habitantes com uma taxa anual de crescimento de 3% e que a população de
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento'''

A = 80000
B = 200000
cont = 0

while(True):
    A = A + (3/100 * A)
    B = B + (1.5/100 * B)

    cont += 1
    
    if(A > B):
        print('A população do país A será maior que a de B em %d anos' %cont)
        break

''' DO PROFESSOR
A = 80000
B = 200000
anos = 0
while A <= B:
    A = A + A * 0.03
    B = B + B * 0.015
    anos = anos + 1
print (anos)
'''
