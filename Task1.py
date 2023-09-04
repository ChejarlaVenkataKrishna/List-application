import json
import os
from datetime import datetime

# Define the task list as an empty list
task_list = []

# Define the filename for storing tasks
data_file = "tasks.json"

# Check if the data file exists and load tasks
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        task_list = json.load(file)

def save_tasks():
    # Save tasks to the data file
    with open(data_file, "w") as file:
        json.dump(task_list, file)

def add_task():
    task = {}
    task["title"] = input("Enter task title: ")
    task["priority"] = input("Enter task priority (high, medium, low): ").lower()
    task["due_date"] = input("Enter due date (YYYY-MM-DD): ")
    task["completed"] = False
    task_list.append(task)
    save_tasks()
    print("Task added successfully!")

def remove_task():
    print_task_list()
    try:
        task_index = int(input("Enter the index of the task to remove: "))
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            save_tasks()
            print(f"Task '{removed_task['title']}' removed successfully!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def mark_completed():
    print_task_list()
    try:
        task_index = int(input("Enter the index of the completed task: "))
        if 0 <= task_index < len(task_list):
            task_list[task_index]["completed"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def print_task_list():
    print("\nTask List:")
    for index, task in enumerate(task_list):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. [{status}] {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print_task_list()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("Goodbye!")

