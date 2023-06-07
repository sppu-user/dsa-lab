# Function containing menu
# Returns a integer choice
def menu():
    print(""" 
=============================          
        [0] Exit
        [1] Add
        [2] Remove
        [3] Search
        [4] Length
        [5] Union    
        [6] Intersection
        [7] Difference
        [8] Subset
        [9] Display
=============================          
    """)
    return int(input("Enter your choice (0-9) : "))


def menu1():
    print("""   
=============================          
        [1] Set A
        [2] Set B
=============================          
    """)
    return int(input("Select the set to perform the operation (1-2) : "))

# to clear the terminal


def clear():
    try:
        import os
        try:
            os.system("cls")
        except:
            os.system("clear")
    except ModuleNotFoundError:
        print("Error in loading module")


# Main Function
if __name__ == "__main__":

    # take set size and create the sets
    listSize = int(input("Enter the list size:"))
    a = set([int(input(f"Enter element {i} in set a:")) for i in range(listSize)])
    b = set([int(input(f"Enter element {i} in set b:")) for i in range(listSize)])

    on = True

    # looping condition to repeatedly display the menu
    while on:
        
        choice = menu()

        if choice == 1:
            clear()
            choice1 = menu1()
            if choice1 == 1:
                a.add(int(input("Enter new element in set A : ")))
            elif choice1 == 2:
                b.add(int(input("Enter new element in set B : ")))
            clear() 

        elif choice == 2:
            clear()
            choice1 = menu1()
            if choice1 == 1:
                _ = int(input("Enter element to remove from set A : "))
                if _ in a:
                    a.remove(_)
                else:
                    print("Number not present")
            elif choice1 == 2:
                _ = int(input("Enter element to remove from set A : "))
                if _ in a:
                    a.remove(_)
                else:
                    print("Number not present")
            clear() 
        
        elif choice == 3:
            clear()
            choice1 = menu1()
            if choice1 == 1:
                _ = int(input("Enter the element to search : "))
                print(f"Element {_} present in Set A : {_ in a}")
            elif choice1 == 2:
                _ = int(input("Enter the element to search : "))
                print(f"Element {_} present in Set B : {_ in a}")
            clear() 
        
        elif choice == 4:
            clear()
            choice1 = menu1()
            if choice1 == 1:
                print(f"Length of Set A is {len(a)}")
            elif choice1 == 2:
                print(f"Length of Set B is {len(b)}")
        
        elif choice == 5:
            clear()
            print(f"Union of sets A and B is {a|b}")
            
        elif choice == 6:
            clear()
            print(f"Intersection of sets A and B is {a&b}")
            
        elif choice == 7:
            clear()
            print(f"Difference of sets A-B is {a-b}")
            print(f"Difference of sets B-A is {b-a}")
            
        elif choice == 8:
            clear()
            print(f"Set A subset of Set B {bool(a^b)}")
            print(f"Set B subset of Set A {bool(b^a)}")
        
        elif choice == 9:
            clear()
            print(f"Set A : {a}")
            print(f"Set B : {b}")
            
        elif choice == 0:
            on = False
            break
        else:
            clear()
            print("Invalid Choice")
            continue
