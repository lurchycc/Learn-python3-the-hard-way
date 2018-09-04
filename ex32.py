the_count=[1,2,3,4,5]
friuts = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#the first kind of for_loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for friut in friuts:
    print(f"A friut of type:{friut}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in  change:
    print(f"I got {i}")
#we can also build lists first start with an empty one
elements=[]

#then use the range function to go 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #appending is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Elenment was :{i}")