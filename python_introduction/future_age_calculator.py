#script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

# Future Age Calculator
def calculate_future_age():
    # Ask the user for their current age
    current_age = int(input("How old are you? "))
    
    # Ask the user for a future year
    future_year = 2050  # You can change this to any year you want to calculate for
    
    # Get the current year
    #from datetime import datetime #instructions says to use current year as 2023
    current_year = 2023 #datetime.now().year
    
    # Calculate the user's age in the future year
    future_age = current_age + (future_year - current_year)
    
    # Display the result
    print(f"In {future_year}, you will be {future_age} years old.")

# Run the function
if __name__ == "__main__":
    calculate_future_age()