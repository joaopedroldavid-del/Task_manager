def add_task(tasks, task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"\nThe task {task_name} was added successfully")
    return

def see_task(tasks):
    print("\nTask list:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else " "
        task_name = task["name"]
        print(f"{i}. [{status}] {task_name}")


tasks = []

while True:
    print("\n Task List Manager Menu: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Completed Tasks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task_name = input("\nWhat's the task name?")
        add_task(tasks, task_name)
    elif choice == 2:
        see_task(tasks)
    elif choice == 6:
        break

print("Program completed")