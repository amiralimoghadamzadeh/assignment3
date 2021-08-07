import random
a = int(input("how many numbers ? "))
L = []
while len(L) < a:
    b = random.randint(1,99)
    if b not in L:
        L.append(b)
print(L)
    