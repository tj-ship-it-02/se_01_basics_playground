# Abfrage der User Inputs
user_name = input("What's your name?")
habit_gym = input("Have you been to the gym today?")
habit_walk = input ("Have you gone for a walk today?")
habit_meditation = input("How many minutes have you meditated today?")

# Summary Überblick vom User
print("Congrats, " + user_name + " you have been to the gym today, have been outside for a walk AND meditated for " + habit_meditation + " minutes!")

# Next Steps?
user_daily_reflection = input("What's your #1 learning for today?")
user_daily_wrapup = input("What is the #1 Action Item for tomorrow?")

print("Awesome, love your reflection:" + user_daily_reflection + " and knowing that tomorrow you'll " + user_daily_wrapup + " makes you excited, hopefully!")