#Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

# Simple Calculator using Match Case
# This program performs basic arithmetic operations based on user input.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")


match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
    case '/':
        if num2 == 0:
            print("Cannot divvide by zero.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    case _:
        print("Invalid operation selected. Please choose from +, -, *, or /.")