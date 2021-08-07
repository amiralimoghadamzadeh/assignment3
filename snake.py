a = int(input("enter the length of snake"))
if a % 2 == 0:
    b = int(a / 2)
    print("*#" * b)
else:
    c = int((a-1) / 2 )
    print("*#" * c ,"*") 