def add_task(tasks, task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"\nThe task '{task_name}' has been added successfully.")
    return

def see_task(tasks):
    print("\nTask List:")
    if not tasks:
        print("\nNo tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else " "
        task_name = task["name"]
        print(f"{index}. [{status}] {task_name}")

def update_task_name(tasks, index, new_task_name):
    if 0 <= index < len(tasks):
        old_name = tasks[index]["name"]
        tasks[index]["name"] = new_task_name
        print(f"\nThe task '{old_name}' has been updated to '{new_task_name}'.")
    else:
        print("\n[404] Task index not found.")
        return

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"\nThe task '{tasks[index]["name"]}' has been completed'.")
    else:
        print("\n[404] Task index not found.")
    return

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index) 
        print(f"\nThe task '{deleted_task['name']}' has been deleted.")
    else:
        print("\nComplete the task before deleting")
    return

tasks = []

while True:
    print("\nTask List Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Completed Tasks")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nInvalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        task_name = input("\nEnter the task name: ")
        add_task(tasks, task_name)
    elif choice == 2:
        see_task(tasks)
    elif choice == 3:
        see_task(tasks)
        index = int(input("\nEnter the task number: ")) - 1
        new_task_name = input("\nEnter the new task name: ")
        update_task_name(tasks, index, new_task_name)
    elif choice == 4:
        see_task(tasks)
        index = int(input("\nEnter the task number: ")) - 1
        complete_task(tasks, index)
    elif choice == 5:
        see_task(tasks)
        index = int(input("\nEnter the task number: ")) - 1
        delete_task(tasks, index)
    elif choice == 6:
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

print("\nProgram terminated.")