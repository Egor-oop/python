i = 3481561
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)
