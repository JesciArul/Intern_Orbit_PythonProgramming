

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted = tasks.pop(task_no - 1)
                print(f"Task '{deleted}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")
