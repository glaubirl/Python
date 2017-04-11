f1 = 1
f2 = 1
f3 = 0

while f1 < 100:
    f3 = f1 + f2
    f1 = f3 + f2
    f2 = f3 + f1

    print(f3,f1,f2)
