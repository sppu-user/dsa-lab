s1=[]
s2=[]
def accept():
    n=(int(input("Enter no. of elements: ")))
    for i in range(n):
        s1.append(int(input("Enter element: ")))
    return s1

def size(s1):
    cnt=0
    for i in s1:
        cnt+=1
    return cnt

def remove_ele(s1,element):
    for i in s1:
        if(i==element):
            s1.remove(element)
    return s1

def search(s1,element):
    for i in s1:
        if(i==element):
            print(f"{i} is present in the set")

def iterate(s1):
    iterator=iter(s1)
    print("Elements in the set: ")
    for i in range(len(s1)):
        print(next(iterator))

def intersection(s1,s2):
    inter=[]
    for i in s1:
        for j in s2:
            if(i==j):
                inter.append(i)
    print("Intersection of sets: ",inter)

def union(s1,s2):
    uni=[]
    uni.extend(s1)
    for i in s2:
        if i not in s1:
            uni.append(i)
    print("Union of sets: ",uni)

def difference(s1,s2):
    diff=[]
    for i in s1:
        if i not in s2:
            diff.append(i)
    print("Difference s1-s2: ",diff)

def subset(s1,s2):
    subset=True
    for i in s2:
        if i not in s1:
            subset=False
    if(subset==False):
        print("s2 is not a subset")
    else:
        print("s2 is a subset")

while True:
    print("\n---------MENU----------")
    print("\n1. Accept\n2. Size\n3. Remove\n4. Contains\n5. Iterate\n6. Set operations\n7. Exit")
    ch=int(input("Enter your choice: "))

    if(ch==1):
        s1=accept()
        print("Set: ",s1)
        
    elif(ch==2):
        cnt=size(s1)
        print("Size: ",cnt)
        
    elif(ch==3):
        element=int(input("Enter the element to delete: "))
        s1=remove_ele(s1,element)
        print("updated set: ",s1)
        
    elif(ch==4):
        element=int(input("Enter the element to search: "))
        s1=search(s1,element)
        
    elif(ch==5):
        iterate(s1)

    elif(ch==6):    
        m=int(input("Enter the no. of elements in s2: "))
        for i in range(m):
            s2.append(int(input("Enter element: ")))
        for i in range(5):
            print("***Set Operations:**** ")
            print("1) Intersection of Sets")
            print("2) Union of Sets")
            print("3) Difference of Sets")
            print("4) Subset of a Set")
            print("5) Exit")
            choice=int(input("Enter your choice: "))
            while True:
                if choice==1:
                    intersection(s1,s2)
                    break
                elif choice ==2:
                    union(s1,s2)
                    break
                elif choice ==3:
                    difference(s1,s2)
                    break
                elif choice==4:
                    subset(s1,s2)
                    break
                else:
                    print("Exit")
                    break
    else:
        print("-----EXIT-----")
        break
    

        