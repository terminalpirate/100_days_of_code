import os

def load_tasks (filename="tasks.txt") :
    if not os.path.exists("tasks.txt") :
        return []
    else:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in  f.readlines()]

def save_tasks (tasks, filename = "tasks.txt") :
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")



def tasks_function () :
    tasks  = load_tasks("tasks.txt")

    while True :
        print("What would you like to do? \n"
            "1. Add a task\n"
            "2. View tasks\n"
            "3. Quit\n"
            "4. Remove a task")

        command = input("Enter command: " )

        if command == "1" :
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!\n")
        
        elif command == "2" :
            print("Your tasks:")
            if not tasks:
                print("No tasks yet!\n")
            else :
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        
        elif command == "3" :
            save_tasks(tasks, "tasks.txt")
            print("Goodbye!")
            break
        
        elif command == "4" :
            if not tasks:
                print("No tasks yet!\n")
            else :
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                
                try:
                    task_num = int(input("Enter task number to remove: ")) 
                    if 1 <= task_num <= len(tasks) :
                        removed = tasks.pop(task_num - 1)
                        print(f"Task '{removed}' removed!")
                    else:
                        print("Invalid task number!\n")
                except ValueError:
                    print("Please enter a valid task number!\n")

        
        else :
            print("Invalid command entered\n")

tasks_function()