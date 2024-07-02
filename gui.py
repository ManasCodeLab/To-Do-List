import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE = 'tasks.json'

def load_tasks():
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    with open(FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = simpledialog.askstring("Input", "Enter the task:")
    if task:
        tasks = load_tasks()
        date_added = datetime.today().strftime('%Y-%m-%d')
        tasks[task] = {"done": False, "date_added": date_added}
        save_tasks(tasks)
        messagebox.showinfo("Info", f"Task '{task}' added on {date_added}.")
        list_tasks()

def remove_task():
    task = simpledialog.askstring("Input", "Enter the task to remove:")
    if task:
        tasks = load_tasks()
        if task in tasks:
            del tasks[task]
            save_tasks(tasks)
            messagebox.showinfo("Info", f"Task '{task}' removed.")
            list_tasks()
        else:
            messagebox.showerror("Error", f"Task '{task}' not found.")

def mark_done():
    task = simpledialog.askstring("Input", "Enter the task to mark as done:")
    if task:
        tasks = load_tasks()
        if task in tasks:
            tasks[task]["done"] = True
            save_tasks(tasks)
            messagebox.showinfo("Info", f"Task '{task}' marked as done.")
            list_tasks()
        else:
            messagebox.showerror("Error", f"Task '{task}' not found.")

def list_tasks():
    tasks = load_tasks()
    task_listbox.delete(0, tk.END)
    if not tasks:
        task_listbox.insert(tk.END, "No tasks found.")
    else:
        for task, details in tasks.items():
            status_str = "Done" if details["done"] else "Not done"
            task_listbox.insert(tk.END, f"{task}: {status_str} (Added on: {details['date_added']})")

# GUI Setup
root = tk.Tk()
root.title("Simple To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=20)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

mark_done_button = tk.Button(frame, text="Mark Task as Done", command=mark_done)
mark_done_button.pack(side=tk.LEFT, padx=10)

list_button = tk.Button(frame, text="List All Tasks", command=list_tasks)
list_button.pack(side=tk.LEFT, padx=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=20)

# Initialize the task list
list_tasks()

root.mainloop()
