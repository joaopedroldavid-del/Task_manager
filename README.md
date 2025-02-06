# Task Manager

## 📌 Description
A simple command-line Task Manager built in Python that allows users to add, view, update, complete, and delete tasks. It provides a straightforward way to keep track of tasks and their completion status.

## 🚀 Features
- Add new tasks
- View all tasks
- Update task names
- Mark tasks as completed
- Delete completed tasks
- User-friendly interactive menu

## 🛠️ Installation & Setup
### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

### Running the Application
1. Clone this repository:
```sh
git clone <repository_url>
```
2. Navigate to the project directory:
```sh
cd task_manager
```
3. Run the script:
```sh
python task_manager.py
```

## 📖 Usage
Once the script is running, follow the interactive menu to manage tasks:
```
Task List Manager Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Complete Task
5. Delete Completed Tasks
6. Exit
```

### Example Usage
1. **Adding a Task**
   - Select option `1`
   - Enter the task name
   - The task is added successfully

2. **Viewing Tasks**
   - Select option `2`
   - Displays a numbered list of tasks with completion status

3. **Updating a Task**
   - Select option `3`
   - Choose a task by number
   - Enter the new task name
   - Task name is updated

4. **Completing a Task**
   - Select option `4`
   - Choose a task by number
   - Task is marked as completed

5. **Deleting a Completed Task**
   - Select option `5`
   - Choose a completed task by number
   - Task is deleted

6. **Exiting the Program**
   - Select option `6`
   - Program terminates

## 🔧 Code Structure
- `add_task(tasks, task_name)`: Adds a new task
- `see_task(tasks)`: Displays the list of tasks
- `update_task_name(tasks, index, new_task_name)`: Updates an existing task's name
- `complete_task(tasks, index)`: Marks a task as completed
- `delete_task(tasks, index)`: Deletes a completed task
