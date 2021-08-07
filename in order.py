L = []
while True:
    a = input("eter your numbers or enter end to exit")
    if a == "end":
        print("the procces will now begin")
        break
    else:
        L.append(a)

for i in range(1,len(L)):
    if L[i] > L[i - 1]:
        print("your numbers are in order")
        break 
    else:
        print("your numbers are not in order")