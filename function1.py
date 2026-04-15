# Write a function called greet_user that takes a name and a time_of_day (e.g., "morning", "evening"). Use keyword arguments so that if no time_of_day is provided, it defaults to "day".
def greet_user(name,time_of_day="day"):
    print(f"Good {time_of_day} {name} ")
greet_user("moiz")
greet_user("moiz ","evening")