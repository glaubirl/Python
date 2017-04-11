nota = 11

while nota < 0 or nota > 10:
  print ('O número é inválido, insira outro valor.')
  nota = int(input('Digite um número entre zero e dez: '))

print ('O número %d é válido.' %nota)
