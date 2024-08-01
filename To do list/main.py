import os

# File to store tasks
TASKS_FILE = 'todo.txt'

def read_tasks():
    """Read tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def write_tasks(tasks):
    """Write tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    """Add a new task."""
    tasks = read_tasks()
    tasks.append(f"[ ] {task}")
    write_tasks(tasks)
    print("Task added successfully.")

def view_tasks():
    """View all tasks."""
    tasks = read_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def update_task(index, new_task):
    """Update an existing task."""
    tasks = read_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1] = f"[ ] {new_task}"
        write_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(index):
    """Delete a task."""
    tasks = read_tasks()
    if 0 < index <= len(tasks):
        tasks.pop(index - 1)
        write_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def mark_task_completed(index):
    """Mark a task as completed."""
    tasks = read_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1] = tasks[index - 1].replace("[ ]", "[x]")
        write_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    """Main function to interact with the user."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            index = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(index, new_task)
        elif choice == '4':
            view_tasks()
            index = int(input("Enter the task number to delete: "))
            delete_task(index)
        elif choice == '5':
            view_tasks()
            index = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(index)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
