
import os

tableSize = int(input("Enter the size of Hash Table:"))
hashTable = list(None for i in range(tableSize))

 # to clear terminal after every iteration
def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")


def menu1():
    print("\n=======Menu========")
    print("1. Linear probing")
    print("2. Quadratic probing")
    print("3. Exit")
    _ = int(input("Select a Collision Handeling method:"))
    return _


def menu2():
    print("\n=======Menu========")
    print("1. Insert an element")
    print("2. Search an element")
    print("3. Display the Table")
    print("4. Change collision handeling method")
    _ = int(input("Enter your Choice:"))
    return _


# Functions for Linear probing

def insertL():
    name = input("Enter the name:")
    number = input("Ente the Number:")
    row = name + " : " + number
    position = int(number)%tableSize
    
    if(hashTable[position]==None):
        hashTable[position] = row
    else:
        # Here collision occured
        print(f"Collision occured for {name}")
        while hashTable[position]!=None:
            position+=1
            if position>=tableSize:
                position = 0

        hashTable[position] = row

def insertQ():
    name = input("Enter the name:")
    number = input("Ente the Number:")
    row = name + " : " + number
    position = int(number)%tableSize
    
    if(hashTable[position]==None):
        hashTable[position] = row
    else:
        # Here collision occured
        i = 1
        print(f"Collision occured for {name}")
        while hashTable[position]!=None:
            position+=(i*i)
            if position>=tableSize:
                position = 0
            i+=1

        hashTable[position] = row
        
        
def search():
    _ = [range(tableSize)]
    name = input("Enter the name:")
    number = input("Enter the number:")
    count = 0
    for i in range(tableSize):
        count +=1
        if hashTable[i] is not None:
            _ = hashTable[i].split(":")
            if _[0] == name and _[1] == number:   
                print(f"{name} found at {i} and Comparisons required are {count}")
                return
    else:
        print("Not found")
        
        
def display():
    # _ = [range(len(hashTable))]
    print("Name : Number")
    for i in hashTable:
        if i is None:
            print("None : None")
        else:
            _ = i.strip(":")
            print(f"{_[0]} : {_[1]}")
        
        
if __name__ == "__main__":
    run = True
    choice1 = 0
    while run:
        choice1 = menu1()
       
        if choice1 == 1:
            clear()
            on = True
            choice2 = 0
            # Initialize the hash table with null elements
            while on:
                choice2 = menu2()
                if choice2 == 1:
                    insertL()
                elif choice2 == 2:
                    search()
                elif choice2 == 3:
                    display()
                elif choice2 == 4:
                    on = False
                else:
                    print("Invalid Choice")
                    continue

        elif choice1 == 2:
            clear()
            on = True
            choice2 = 0
            while on:
                choice2 = menu2()
                if choice2 == 1:
                    insertQ()
                elif choice2 == 2:
                    search()
                elif choice2 == 3:
                    display()
                elif choice2 == 4:
                    on = False
                else:
                    print("Invalid Choice")
                    continue
        elif choice1 == 3:
            run = False
            exit(0)
        else:
            print("Invalid choice!")
            continue
