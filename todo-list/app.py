import os  # Import the os module for file operations

# File to store the to-do list
TODO_FILE = "todo-list.txt"

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
    if not tasks:  # Check if the task list is empty
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

def exit_program():
    """Exit the program."""
    print("Quitting...")  # Print a quitting message
    exit()  # Exit the program

def main():
    """Main function to run the To-do list App."""
    tasks = load_tasks()  # Load tasks from the file
    
    # Dictionary to map menu choices to functions
    menu_actions = {
        "1": lambda: display_tasks(tasks),  # Map option "1" to display tasks
        "2": lambda: add_task(tasks),  # Map option "2" to add a task
        "3": lambda: delete_task(tasks),  # Map option "3" to delete a task
        "4": lambda: edit_task(tasks),  # Map option "4" to edit a task
        "5": lambda: exit_program()  # Map option "5" to exit the program
    }
    
    while True:
        print("To-Do List Menu.")  # Print the menu header
        print("1. View Tasks")  # Option to view tasks
        print("2. Add a Task")  # Option to add a task
        print("3. Delete a Task")  # Option to delete a task
        print("4. Edit a Task")  # Option to edit a task
        print("5. Exit")  # Option to exit the program
        
        try:
            choice = input("Choose an option (1 - 5): ")  # Get the user's menu choice
            action = menu_actions.get(choice)  # Retrieve the corresponding function from the dictionary
            if action:
                action()  # Execute the corresponding function
            else:
                print("Invalid choice. Please choose a number between 1 and 5.\n")  # Print an error message for invalid choices
        except Exception as e:  # Catch any other exceptions
            print(f"An error occurred: {e}\n")  # Print an error message

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
