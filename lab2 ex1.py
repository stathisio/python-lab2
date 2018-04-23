print("1. insert a new task (a string of text)")
print("2. remove a task (by typing its content, exactly)")
print("3. show all existing tasks, sorted in alphabetic order")
print("4. close the program.")

todo=[]
choice=int(input("Make a choice: "))

while (choice!=4):
    if(choice==1):
        task=input("Insert a new task: ")
        todo.append(task)
    if(choice==2):
        task=input("Insert a task to be deleted: ")
        todo.remove(task)
    if(choice==3):
        print (sorted(todo))
    choice=int(input("Make a new choice: "))
