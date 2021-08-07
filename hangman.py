import random 
L = ["yellow","blue","green","white","black"]
a = random.choice(L)
word = []
LIST = []
for i in range(len(a)):
    LIST.append("_")
    word.append(a[i])
print(LIST)

life = len(a)
while life > 0:
    guess = input("enter the word")
    if guess in word:
        LIST.insert(i,guess)
        print(LIST)
    else:
        life -= 1

