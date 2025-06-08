# Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

# Task Description:
# Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

# Requirements:
# Define Global Conversion Factors:

# At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
# Implement Conversion Functions:

# Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
# Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
# Inside each function, use the respective global conversion factor to perform the conversion.
# User Interaction:

# Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
# Based on the user’s input, call the appropriate conversion function and display the converted temperature.
# If gthe user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
# Guidance:
# Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
# Use input validation to ensure that the user enters a valid temperature and unit.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # global FAHRENHEIT_TO_CELSIUS_FACTOR
    try:
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # global CELSIUS_TO_FAHRENHEIT_FACTOR
    try:
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

temperature = input("Enter the temperature to convert: ").strip()


# while type(temperature) == float:
while True:
    try:
        temperature = float(temperature)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value and continue.")
        temperature = input("Enter the temperature to convert: ").strip()
        continue
    # temperature = float(temperature)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    match unit:
            
        case 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.2f}°F")
            break
        case 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")
            break
        case _:
            print("Invalid operation selected. Please choose from C or F and continue")

# def main():
#     print("Temperature Conversion Tool")
#     temp = input("Enter the temperature (e.g., 100C or 212F): ").strip()
    
#     if temp[-1].upper() == 'C':
#         try:
#             celsius = float(temp[:-1])
#             fahrenheit = convert_to_fahrenheit(celsius)
#             print(f"{celsius}°C is {fahrenheit:.2f}°F")
#         except ValueError as e:
#             print(e)
#     elif temp[-1].upper() == 'F':
#         try:
#             fahrenheit = float(temp[:-1])
#             celsius = convert_to_celsius(fahrenheit)
#             print(f"{fahrenheit}°F is {celsius:.2f}°C")
#         except ValueError as e:
#             print(e)
#     else:
#         print("Invalid input. Please enter a temperature ending with 'C' or 'F'.")


# if __name__ == "__main__":
#     main()
# This script serves as a temperature conversion tool, allowing users to convert temperatures between Celsius and Fahrenheit.
# It uses global variables to store conversion factors and demonstrates basic error handling for user input.