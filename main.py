import json
from datetime import datetime
import time
import os

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

def add_task(task):
    tasks = load_tasks()
    date_added = datetime.today().strftime('%Y-%m-%d')
    tasks[task] = {"done": False, "date_added": date_added}
    save_tasks(tasks)
    print(f"Task '{task}' added on {date_added}.")

def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        del tasks[task]
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def mark_done(task):
    tasks = load_tasks()
    if task in tasks:
        tasks[task]["done"] = True
        save_tasks(tasks)
        print(f"Task '{task}' marked as done.")
    else:
        print(f"Task '{task}' not found.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task, details in tasks.items():
            status_str = "Done" if details["done"] else "Not done"
            print(f"{task}: {status_str} (Added on: {details['date_added']})")

def main():
    while True:
        print("\nSimple To-Do List App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. List All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            time.sleep(0.5)
            os.system("cls")
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            time.sleep(0.5)
            os.system("cls")
            list_tasks()
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            time.sleep(1)
            os.system("cls")
            list_tasks()
            task = input("Enter the task to mark as done: ")
            mark_done(task)
        elif choice == '4':
            time.sleep(0.5)
            os.system("cls")
            list_tasks()
        elif choice == '5':
            time.sleep(1)
            os.system("cls")
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)
            os.system("cls")

if __name__ == "__main__":
    main()
