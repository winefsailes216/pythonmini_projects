from calculator_functions import add, subtract, multiply, divide

# Dictionary to map operation symbols to function calls
operations = {
        '+': add,           # Maps '+' to the add function
        '-': subtract,      # Maps '-' to the subtract function
        '*': multiply,      # Maps '*' to the multiply function
        '/': divide         # Maps '/' to the divide function
}

    
def main():
    while True:
        # Prompt the user to continue or quit
        user_input = input("Enter 'quit' to exit or any key to continue: ")
        if user_input.lower() == "quit":
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Get numbers from the user
            num1 = float(input("Enter first number: "))  # Convert input to float
            num2 = float(input("Enter second number: ")) # Convert input to float
            # Get the desired operation from the user
            operation = input("Choose operation (+, -, *, /): ")

            # Use the dictionary to call the corresponding function
            if operation in operations:
                func = operations[operation]  # Retrieve the function from the dictionary
                result = func(num1, num2)     # Call the function with user inputs
                print(f"Result: {result}")    # Display the result
            else:
                print("Invalid operation. Please try again.")  # Handle invalid operations
        except ValueError as ve:
            # Handle errors related to invalid number inputs
            print(f"Invalid input: {ve}. Please enter numbers only.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {e}.")


if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly
