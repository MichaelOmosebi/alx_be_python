# This code collects a list of numbers from the user, calculates their total, and prints the result.
# The user is prompted to enter numbers separated by spaces, which are then split into a list.# The total is calculated by converting each number from string to integer and summing them up.

total = 0

nums = list(input("Enter a list of numbers separated by spaces: ").split(","))

#print("The numbers you entered are:", nums)
for num in nums:
    total += int(num)

print("The total of the numbers is:", total)
