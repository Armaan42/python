#student management system
# 1. Add marks of new marks
# 2. Insert the marks at the desired position
# 3. Append list of existing student
# 4. Modify marks of existing student
# 5. Delete marks for left students by its position
# 6. Delete the marks of a left student by its value
# 7. Sort the list of marks obtained in ascending order
# 8. Sort the list of marks obtained in descending order
# 9. Display the final marks list
# 10. Exit


markslist = [10,20,30,40,50,60,70,80,90,100]
choice = 0
while True:
    print("The list 'marklist' contains the marks",len(markslist),"students as: ",markslist)
    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1. Add marks of new marks")
    print("2. Insert the marks at the desired position")
    print("3. Append list of existing student")
    print("4. Modify marks of existing student")
    print("5. Delete marks for left students by its position")
    print("6. Delete the marks of a left student by its value")
    print("7. Sort the list of marks obtained in ascending order")
    print("8. Sort the list of marks obtained in descending order")
    print("9. Display the final marks list")
    print("10. Exit")

    choice = int(input("Enter your choice [1-10]: "))

    if choice == 1:
        element = int(input("Enter the marks to be added: "))
        markslist.append(element)
        print("The marks have been updated")
    
    elif choice == 2:
        element = int(input("Enter the marks to be inserted: "))
        pos = int(input("Enter the position where to insert the marks in markslist: "))
        markslist.insert(pos, element)
        print("The marks have been inserted")
    
    elif choice == 3:
        newList = eval(input("Enter the new list of marks: "))
        markslist.extend(newList)
        print("Markslist have been updated")
    
    elif choice == 4:
        pos = int(input("Enter the position of the marks to be modified: "))
        if pos < len(markslist):
            newMarks = int(input("Enter the new marks of the student: "))
            markslist[pos] = newMarks
            print("Marks have been modified")
        else:
            print("Invalid position.")

    elif choice == 5:
        pos = int(input("Enter the position of the marks to be deleted: "))
        if pos < len(markslist):
            del markslist[pos]
            print("Marks have been deleted")
        else:
            print("Invalid position")
    
    elif choice == 6:
        value = int(input("Enter the value to be deleted: "))
        if value in markslist:
            markslist.remove(value)
            print("Marks have been deleted")
        else:
            print("Marks value not found")

    elif choice == 7:
        markslist.sort()
        print("The markslist have been sorted in ascending order")
    
    elif choice == 8:
        markslist.sort(reverse=True)
        print("The markslist have been sorted in descending order")
    
    elif choice == 9:
        print("The final list of student markslist is: ",markslist)
        print("\n")
    
    elif choice == 10:
        break
    else:
        print("Wrong input.Try again")
        ch = input()
        


