#Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

# Finance Calculator
def calculate_savings():
    # Ask the user for their monthly savings amount
    monthly_income = float(input("Enter your monthly income: "))

    monthly_expenses = float(input("Enter your total monthly expenses: "))
        
    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Ask the user for the number of years they plan to save
    #years = int(input("For how many years do you plan to save? ")) #instruction says to assume 1 year
    years = 1  # Assuming the user plans to save for 1 year as per instructions

    #Calculate the projected savings after one year, incorporating an interest rate of 5%
    interest_rate = 0.05
    total_months = years * 12
    total_savings = monthly_savings * total_months * (1 + interest_rate)
    
    # Display the result
    # print(f"If you save ${monthly_savings:.2f} each month for {years} years, "
    #       f"you will have saved a total of ${total_savings:.2f}.")
    print(f"Your monthly savings are ${monthly_savings}.")
    print(f"Projected savings after one year, with interest, is: ${total_savings}.")

# Run the savings calculation
if __name__ == "__main__":
    calculate_savings()