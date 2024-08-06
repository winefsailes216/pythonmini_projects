# calculator_functions.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Optional: Testing the functions if this file is run directly
if __name__ == "__main__":
    print("Testing functions:")
    print("Add 1 + 2 =", add(1, 2))  # Expected output: 3
    print("Subtract 5 - 3 =", subtract(5, 3))  # Expected output: 2
    print("Multiply 4 * 2 =", multiply(4, 2))  # Expected output: 8
    print("Divide 8 / 2 =", divide(8, 2))  # Expected output: 4.0
