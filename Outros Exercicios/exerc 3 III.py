a = 80000
b = 200000
x = 0

while a <= b:
    a = (3 * a) / 100 + a
    b = (1.5 * b) / 100 + b
    x += 1

print('O país A terá mais habitantes que B em %d anos' %x)
