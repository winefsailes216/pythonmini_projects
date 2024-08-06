#This are functions for task management and utilities for file handling
import os

TODO_FILE = "to-do-list.txt"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TODO_FILE):  # Check if the file exists
        with open(TODO_FILE, "r") as file:  # Open the file in read mode
            tasks = file.readlines()  # Read all lines from the file
    else:
        tasks = []  # Initialize an empty list if the file does not exist
    return [task.strip() for task in tasks]  # Remove leading/trailing whitespace from each task

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:  # Open the file in write mode
        for task in tasks:  # Iterate over the list of tasks
            file.write(task + "\n")  # Write each task to the file, followed by a newline

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")  # Print a message if no tasks are present
    else:
        print("\nYour To-Do List.")  # Print the header for the task list
        for index, task in enumerate(tasks, start=1):  # Iterate over tasks with index starting from 1
            print(f"{index}. {task}")  # Print each task with its index
    print()  # Print a blank line for readability

def add_task(tasks):
    """Add a new task."""
    try:
        task = input("Enter the task: ")  # Get the new task from user input
        if task.strip() == "":  # Check if the input is empty or just whitespace
            print("Task cannot be empty.\n")  # Print a message if the task is empty
            return  # Exit the function without adding the task
        tasks.append(task)  # Add the new task to the list
        save_tasks(tasks)  # Save the updated list to the file
        print("Task added.\n")  # Print a confirmation message
    except Exception as e:  # Catch any exceptions that occur
        print(f"An error occurred: {e}\n")  # Print an error message

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)  # Show the current list of tasks
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1  # Get the task number from user input
        if 0 <= index < len(tasks):  # Check if the index is valid
            tasks.pop(index)  # Remove the task at the specified index
            save_tasks(tasks)  # Save the updated list to the file
            print("Task deleted.\n")  # Print a confirmation message
        else:
            print("Invalid task number.\n")  # Print an error message if the index is invalid
    except ValueError:  # Catch errors from invalid integer input
        print("Invalid input. Please enter a number.\n")  # Print an error message
    except Exception as e:  # Catch any other exceptions
        print(f"An error occurred: {e}\n")  # Print an error message

def edit_task(tasks):
    """Edit an existing task."""
    display_tasks(tasks)  # Show the current list of tasks
    try:
        index = int(input("Enter the number of the task to edit: ")) - 1  # Get the task number from user input
        if 0 <= index < len(tasks):  # Check if the index is valid
            new_task = input("Enter the new task description: ")  # Get the new task description from user input
            if new_task.strip() == "":  # Check if the new task description is empty
                print("Task description cannot be empty.\n")  # Print an error message if empty
                return  # Exit the function without updating the task
            tasks[index] = new_task  # Update the task at the specified index
            save_tasks(tasks)  # Save the updated list to the file
            print("Task updated.\n")  # Print a confirmation message
        else:
            print("Invalid task number.\n")  # Print an error message if the index is invalid
    except ValueError:  # Catch errors from invalid integer input
        print("Invalid input. Please enter a number.\n")  # Print an error message
    except Exception as e:  # Catch any other exceptions
        print(f"An error occurred: {e}\n")  # Print an error message
