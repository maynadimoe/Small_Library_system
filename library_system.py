menu = "list"
print("My library")
list=[]

while menu != "quit":
    print("-"*20)
    print("#list")
    print("#search")
    print("#register")
    print("#delete")
    print("#quit")
    print("-"*20)

    menu = input("Please select a menu: ")

    while menu != "list" and menu !="search" and menu != "register" and menu != "delete" and menu !="quit":
        menu = input("Please select a menu: ")

    if menu == "list":
        if len(list) != 0:
            for i in range(0 ,len(list),1):
                print('['+str(i+1)+']'+list[i])
        else:
            print("There is no book register in the list yet")
                

    if menu == "register":
        while True:
            register = input("Enter the book name to register. If you are done, just press the Enter key to go back to menu: ")
            if register in list:
                print("!!! This book is already in the list !!!")
            elif register == "":
                break
            else:
                list.append(register)

    if menu == "search":
        search = input("Enter the book name to search: ")
        for i in list:
            if search.lower() in i.lower():
                j = int(list.index(i))
                j += 1
                print('['+str(j)+']',list[list.index(i)])
        if i in list and search.lower() not in i.lower():
            print("no book is found")

    if menu == "delete":
        delete = input("Enter the book number or its full name to delete: ")
        if delete.isdecimal():
            i = int(delete)
            ask = input("please comfirm to delete "+list[i-1]+" (y): ")
            if ask != "y":
                print("canceled")
            else:
                print(list[i-1],"has been successfully deleted from the list")
                list.remove(list[i-1])
        elif delete in list:
            i = list.index(delete)
            ask = input("please comfirm to delete "+list[i]+" (y): ")
            if ask != "y":
                print("canceled")
            else:
                print(list[i],"has been successfully deleted from the list")
                list.remove(list[i])
        else:
            print("wrong input")
            
        
        
    
            
    


