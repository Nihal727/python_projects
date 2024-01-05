#simple command line todo list with add, remove and display todo list which saves list in a json file
#coded by Muhammed Nihal
import os
import json

# File to store the to-do list
TODO_FILE = "todo_list.json"
#Function to load todo list
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}
#Function to save todo list
def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=2)
#Function to display todo list
def display_todo_list(todo_list):
    if not todo_list["tasks"]:
        print("No tasks in the to-do list.")
    else:
        for index, task in enumerate(todo_list["tasks"], start=1):
            print(f"{index}. {task}")
#Function to add task to todo list
def add_task(todo_list, task):
    todo_list["tasks"].append(task)
    save_todo_list(todo_list)
    print(f"Task '{task}' added to the to-do list.")
#Function to remove task from todo list
def remove_task(todo_list, index):
    if 1 <= index <= len(todo_list["tasks"]):
        removed_task = todo_list["tasks"].pop(index - 1)
        save_todo_list(todo_list)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")
#Showing Menu and taking input from user
def main():
    todo_list = load_todo_list()

    while True:
        print("\n== To-Do List Menu ==")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == "0":
            print("Exiting To-Do List application. Goodbye!")
            break
        elif choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, index)
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")

if __name__ == "__main__":
    main()
