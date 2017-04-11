n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

resto = [n1, n2]
n, x, y = 1, 0, 1

while n != 0:
    n = resto[x] % resto[y]
    resto.append(n)
    x += 1
    y += 1

print('O MDC de %d e %d é: %d' %(n1, n2, resto[x]))
