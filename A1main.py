from linearprobing import hashtable
from record import record1
from doublehashing import doublehashtable

def input record():
    record = record1()
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    record.set_name(name)
    return record.set_number(number)
    ch1 = 0
    while(ch!=3):
        print("1. Linear probing")
        print("2. Double hashing")
        print("3. Exit")
    ch1 = (int(input("Enter a choice: ")))
    if(ch>3):
        print("wrong choice!!!!")
    if ch1 == 1:
        h1 = hashtable()
        ch = 0
        while(ch2!=4):
            print("1. Insert")
            print("2. Search")
            print("3. Display")
            print("4. Exit")
    ch2 = input("Enter a choice: ")
    if ch1>4:
        print("Wrong choice!!!")
    if(ch2==1):
        record = input_record()
        h1.insert(record)
    elif(ch2==2):
        record = input_record()
        position = h1.search(record)
    elif(ch2==3):
        record = input_record()
        h1.display

    elif ch1 == 2:
        h2 = doublehashtable()
        ch2 = 0
        while(ch2!=4):
            print("1. Insert")
            print("2. Search")
            print("3. Display")
            print("4. Exit")
    ch2 = input("Enter a choice: ")
    if ch2>4:
        print("Wrong choice!!!")
    if(ch2==1):
        record = input_record()
        h2.insert(record)
    elif(ch2==2):
        record = input_record()
        position = h2.search(record)
    elif(ch2==3):
        record = input_record()
        h2.display()