# Create a list of dictionaries called employees with keys "name" and "department". Write a loop that prints the name of every employee, but only if they work in the "Sales" department
  
employees = [
    {"name": "Ali", "department": "HR"},
    {"name": "Sara", "department": "Sales"},
    {"name": "Ahmed", "department": "Finance"},
    {"name": "Ayesha", "department": "Marketing"},
    {"name": "Usman", "department": "Sales"}
]
for x in employees:
    if x["department"]=="Sales":
        print(x["name"])