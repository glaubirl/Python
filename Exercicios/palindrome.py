'''DEFINIR SE A PALAVRA É PALÍNDROME'''

palavra = input('Palavra: ')
if palavra == palavra[::-1]:
    print('%s é palíndrome' %palavra)
else:
    print('%s não é palíndrome' %palavra)
