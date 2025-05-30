tasks=[]
def addTask(task):
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        count=0
        for item in tasks:
            print(f"{count+1}: {item}")
            count+=1

def delete_tasks(number):
    if number>=1 and number<=len(tasks):
        del tasks[number-1]
    
    else:
        print("Invalid task")

while True:
    print("\nOptions")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Quit")

    choice=int(input("Enter your choice: "))

    if choice == 1:
        task=input("Enter the task to be added")
        addTask(task)
    elif choice == 2:
        print("\n Here are are your tasks")
        view_tasks()
    elif choice == 3:
        index=int(input("Enter the index number to be deleted: "))
        delete_tasks(index)
    elif choice == 4:
        break
