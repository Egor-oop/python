a = 2
b = 3

while True:
    a *= 1.1
    a = int(a * 100) / 100
    print(a)
    if a >= b:
        break
