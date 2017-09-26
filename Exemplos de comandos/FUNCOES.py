'''CRIANDO FUNÇÕES EM PYTHON'''

'''Para criar função é utilizado o def. No def é colocado o nome da função e
a sua entrada para ser usado na função, no caso x.'''
def f(x):
    return x*x 
'''Essa função irá retornar o x*x'''
print(f(5))


'''Tentando fazer o python mandar um Eae'''
def hello(s):
    print("Eae", s)

nome = input("\nNome: ")

hello(nome)

'''Fatorial'''
def fat(n):
    f = 1
    while n > 0:
        f = f*n
        n = n-1
    return f

num = int(input("\nNumero para fatorial: "))

print(fat(num))

'''Embaralhar palavras'''
def embaralhar(s):
    
