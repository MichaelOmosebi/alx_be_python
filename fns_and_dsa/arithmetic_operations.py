# A Python script defining a function that performs basic arithmetic operations.
# This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

# Requirements for arithmetic_operations.py:
# Function Definition:
# Define a function named perform_operation.
# Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
# The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
# For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
# Return the result of the arithmetic operation.

def perform_operation(num1, num2, operation) -> float:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."
    


# if __name__ == "__main__":
#     # Example usage
#     print(perform_operation(10, 5, 'add'))        # Output: 15
#     print(perform_operation(10, 5, 'subtract'))   # Output: 5
#     print(perform_operation(10, 5, 'multiply'))   # Output: 50
#     print(perform_operation(10, 0, 'divide'))     # Output: Error: Division by zero is not allowed.
#     print(perform_operation(10, 5, 'divide'))     # Output: 2.0
#     print(perform_operation(10, 5, 'invalid'))    # Output: Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.