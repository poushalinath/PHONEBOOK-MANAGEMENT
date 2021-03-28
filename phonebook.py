numberb_of_entries = int(input(10))
print("Okay , give me name and number respectively for each of them in order")
file = open("phonebook.txt","w")
for i in range (0,10):
    name = input("Name: ")
    number = input("Number: ")
    entry = f"{name}: {number} , "
    file.write(entry)
    if i == 9:
        print("Done!")
    elif i == 8:
        print("Okay next please!")
    elif i == 7:
        print("Okay next please!")
    elif i == 6:
        print("Okay next please!")
    elif i == 5:
        print("Okay next please!")
    elif i == 4:
        print("Okay next please!") 
    elif i == 3:
        print("Okay next please!")
    elif i == 2:
        print("Okay next please!") 
    elif i == 1:
        print("Okay next please!")  
    else:
         print("Okay next please!")
file.close()