from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)



v = 0

for el in cycle("12345"):
    if v > 30:
        break
    print(el)
    v += 1
