tableSize = int(input("Enter the table size:"))
hashTable = list([None, None] for i in range(tableSize))

def display():
    for i, j in hashTable:
        print(i,":",j)
        
def insertl():
    name = input("Enter the name:")
    number = input("Enter the number:")
    position = int(number)%tableSize
    
    if(hashTable[position][0]==None):
        hashTable[position][0]=name
        hashTable[position][1]=number
    
    else:
        print("collision occured")
        while hashTable[position][0] != None:
            position+=1
            if position >= tableSize:
                position = 0
            
        hashTable[position][0] = name
        hashTable[position][1] = number
        
def insertq():
    name = input("Enter the name:")
    number = input("Enter the number:")
    position = int(number)%tableSize
    
    if(hashTable[position][0]==None):
        hashTable[position][0]=name
        hashTable[position][1]=number
    
    else:
        print("collision occured")
        i = 1
        while hashTable[position][0] != None:
            position+= i*i
            i+=1
            if position >= tableSize:
                position = 0
            
        hashTable[position][0] = name
        hashTable[position][1] = number
        
def search():
    count = 0
    name = input("Enter the name:")
    number = input("Enter the number:")
    for i in range(tableSize):
        count +=1
        if name ==hashTable[i][0] and number==hashTable[i][1]:
            print("found")
            print("Comparisions :", count)
            return
    print("Not found")
            
    
if __name__ == "__main__":
    
    run = True
    while run:
        insertl()
        display()
        search()
        if input("Wanna continue...")=="q":
            run = False