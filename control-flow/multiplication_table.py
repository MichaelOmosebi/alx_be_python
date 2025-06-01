# Simple Multiplication Table using For Loop
# This program generates a multiplication table for a user-specified number.

# This code prompts the user for a number and prints its multiplication table from 1 to 10.
# The for loop iterates through the range from 1 to 10, calculating and printing the product for each iteration.

# Objective: Use a for loop to generate and print the multiplication table for a given number.

num = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    product = num * i
    print(f"{num} * {i} = {product}")
