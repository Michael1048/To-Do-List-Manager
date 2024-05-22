
#### `main.py`
```python
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

def view_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")
    else:
        print("No tasks available.")

def complete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
