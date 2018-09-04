numbers=[]

def whiles(c,m):
    i=0
    while i<c:
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=m
        print("Numbers now:",numbers)
        print(f"At the bottom i is {i}")
whiles(int(input("Maxed:")),int(input("step:")))
print("The numbers:")
for num in numbers:
    print(num)