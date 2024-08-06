# todo_list.py is our main program
from tasks import display_tasks, add_task, delete_task, edit_task, load_tasks

def exit_program():
    """Exit the program."""
    print("Quitting...")
    exit()

def main():
    """Main function to run the To-do list App."""
    tasks = load_tasks()  # Load tasks from the file
    
    # Dictionary to map menu choices to functions
    menu_actions = {
        "1": lambda: display_tasks(tasks),
        "2": lambda: add_task(tasks),
        "3": lambda: delete_task(tasks),
        "4": lambda: edit_task(tasks),
        "5": lambda: exit_program()
    }
    
    while True:
        print("To-Do List Menu.")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Delete a Task")
        print("4. Edit a Task")
        print("5. Exit")
        
        try:
            choice = input("Choose an option (1 - 5): ")
            action = menu_actions.get(choice)
            if action:
                action()  # Execute the corresponding function
            else:
                print("Invalid choice. Please choose a number between 1 and 5.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
