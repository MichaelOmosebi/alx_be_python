# This code collects four adjectives from the user and uses them to create a fun story about a zoo visit.
# The story is printed out with the user's input integrated into it.
print("Welcome to the Mad Libs game!")

adjective1 = input("Enter an adjective [describing the day's weather just as you like it]: ")
adjective2 = input("Enter an adjective [describing the monkey's behavior]: ")
adjective3 = input("Enter an adjective [describing the lion's appearance]: ")
adjective4 = input("Enter an adjective [describing a typical overall zoo experience]: ")


text = f"On a beautiful {adjective1} day, I went to the zoo.I saw a funny {adjective2} monkey swinging from the trees. Then, I spotted a majestic {adjective3} lion lounging in the sun. What a wild and {adjective4} experience!"

print(text)
print("Thank you for playing the Mad Libs game!")