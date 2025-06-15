# Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

# Division by Zero: Use a try-except block to catch ZeroDivisionError.
# Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
# Return appropriate messages for errors or the result for successful division.

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float and perform division
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only"
    except Exception as e:
        return f"An unexpected error occurred: {e}"