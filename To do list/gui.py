import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def read_tasks():
    """Read tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def write_tasks(tasks):
    """Write tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = read_tasks()
    tasks.append({"task": task, "completed": False})
    write_tasks(tasks)

def update_task(index, new_task):
    """Update an existing task."""
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        write_tasks(tasks)

def delete_task(index):
    """Delete a task."""
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        write_tasks(tasks)

def mark_task_completed(index):
    """Mark a task as completed."""
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        write_tasks(tasks)

def refresh_tasks():
    """Refresh the task list display."""
    for widget in frame_tasks.winfo_children():
        widget.destroy()

    tasks = read_tasks()
    for index, task in enumerate(tasks):
        task_text = task["task"]
        if task["completed"]:
            task_text += " (Completed)"
        label = tk.Label(frame_tasks, text=task_text, pady=5)
        label.grid(row=index, column=0, sticky="w")
        btn_edit = tk.Button(frame_tasks, text="Edit", command=lambda i=index: edit_task(i))
        btn_edit.grid(row=index, column=1)
        btn_delete = tk.Button(frame_tasks, text="Delete", command=lambda i=index: delete_task(i) or refresh_tasks())
        btn_delete.grid(row=index, column=2)
        btn_complete = tk.Button(frame_tasks, text="Complete", command=lambda i=index: mark_task_completed(i) or refresh_tasks())
        btn_complete.grid(row=index, column=3)

def edit_task(index):
    """Edit an existing task."""
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        task_text.set(tasks[index]["task"])
        task_index.set(index)

def save_task():
    """Save the current task (add or update)."""
    task = entry_task.get()
    index = task_index.get()
    if task:
        if index == -1:
            add_task(task)
        else:
            update_task(index, task)
        task_text.set("")
        task_index.set(-1)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

# Initialize main window
root = tk.Tk()
root.title("To-Do List Application")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

task_text = tk.StringVar()
task_index = tk.IntVar(value=-1)

entry_task = tk.Entry(frame_input, textvariable=task_text, width=50)
entry_task.grid(row=0, column=0, padx=5)

btn_save = tk.Button(frame_input, text="Save Task", command=save_task)
btn_save.grid(row=0, column=1, padx=5)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

refresh_tasks()

root.mainloop()
