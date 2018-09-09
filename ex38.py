ten_things="Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

#while len(stuff)!=10:
for i in range(1000):
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    if len(stuff)==10:
        break

print("There we go:")

print("Let's go some things with stuff.")

print(stuff[1])
print(stuff[-1])#wha!fancy
print(stuff.pop())
print(' '.join(stuff))#waht cool!
print('#'.join(stuff[3:5]))#super stellar