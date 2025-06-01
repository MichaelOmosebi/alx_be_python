# Simple Pattern Drawing using While Loop and For Loop

# This code prompts the user for the size of a square pattern and prints a square made of asterisks (*).
# The while loop iterates through each row, and the for loop prints the asterisks in that row.


# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Print a newline character after completing the row
    print()
    # Increment the row counter
    row += 1
