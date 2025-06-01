# This script provides a simple reminder system based on user input, demonstrating the use of control flow with Match Case and conditional statements.
# It allows the user to input a single task and its attributes, then generates a customized reminder based on the priority and time sensitivity of the task.

# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

# Simple Daily Reminder System using Match Case and Conditional Statements

task = input("Enter your task: ").lower().title()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# match priority:
#     case 'high':
#         reminder = f"'{task}' is a High priority task."
#         if time_bound == 'yes':
#             reminder += " that requires immediate attention today!"
#         else:
#             reminder += " Please complete it as soon as possible."
#     case 'medium':
#         reminder = f"'{task}' is a medium priority task."
#         if time_bound == 'yes':
#             reminder += " This should be addressed today."
#         else:
#             reminder += " You can complete it later this week."
#     case 'low':
#         reminder = f"'{task}' is a low priority task."
#         if time_bound == 'yes':
#             reminder += " It would be good to finish it today, but it's not urgent."
#         else:
#             reminder += " Consider completing it when you have free time."

#     case _:
#         reminder = "Invalid priority level. Please enter high, medium, or low."

# print(reminder)


match priority:
    case 'high':
        reminder = f"'{task}' is a {priority} priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please complete it as soon as possible."
    case 'medium':
        reminder = f"'{task}' is a {priority} priority task"
        if time_bound == 'yes':
            reminder += ". This should be addressed today."
        else:
            reminder += ". You can complete it later this week."
    case 'low':
        reminder = f"'{task}' is a {priority} priority task"
        if time_bound == 'yes':
            reminder += ". It would be good to finish it today, but it's not urgent."
        else:
            reminder += ". Consider completing it when you have free time."

    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

print(reminder)
