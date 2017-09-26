''''MANIPULANDO ARQUIVOS'''

'''Criando o arquivo com o parâmetro W'''
arq = open("manipulando arquivos.txt", "w")

'''Utilizando o método "write" para escrever no arquivo'''
arq.write("EU SEI CRIAR ARQUIVO PORRA!")

arq.write("\n UE")

'''Fazendo que o programa leia o arquivo'''
arq = open("manipulando arquivos.txt", "r")

'''Comando que faz com que o arquivo seja mostrado na tela. É preciso
que o arquivo tenha sido lido antes para ser mostrado na tela'''
print(arq.read())

'''Fechando o arquivo. É necessário para que a programação funcione'''
arq.close()
