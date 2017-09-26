'''BRINCANDO COM STRINGS'''

'''Declarando uma string'''
texto = 'Tá saindo da jaula o monstro'
print('Frase: ', texto)

'''Calcular o tamanho da frase, incluindo os espaços em branco'''
print('Tamanho da frase: ', len(texto))

'''Trocar partes de uma string por outra'''
texto = texto.replace('monstro', 'Luís')
print('Novo texto, após o replace: ', texto)

'''Contar quantas vezes um caractér aparece na frase'''
count = texto.count(' ')
print('Número de espaços em branco na frase: ', count)

'''Há como fazer uma pesquisa de algum carácter ou até mesmo um conjunto
de carácter e encontrar sua posíção'''
posicao = texto.find('Luís')
print('Posição do Luís: ', posicao)
print('O carácter da posição 21 é o ', texto[21])

'''É possível separar as palavras usando o método split. O método sem
parâmetros irá separar entre os espaços em branco'''
separado = texto.split()
print('Texto separado: ', separado)

separado2 = texto.split('a')
print('Texto separado: ', separado2)

'''Verificar strings'''

'''Verificar se o começo do texto é igual à "Há"'''
texto.startswith('Há')

'''Verificar se o final do texto é igual à "posição"'''
arquivo.endswith('posição')

'''É possível juntar palavras, mas somente se estes estiverem dentro de uma lista'''
juntar = ' '.join(separado2)
'''Esta instrução esta dizendo que os elementos da lista separado2 serão grudados
por um espaço (' ')'''
print('Join: ', juntar)
