# Using the same students list from Question 7, write a loop that finds the student named "Bob" and updates his GPA to 3.5. Print the list afterward to verify the change.   
students=[
    {"name": "Alice", "cgpa": 3.1},
    {"name": "Bob", "cgpa": 2.8},
    {"name": "Charlie", "cgpa": 3.1}
]  
for x in students:
    if x["name"]=="Bob":
        x.update({"cgpa": 3.5})
        print(x)