# Refactor Monday's code into a reusable function get_honor_students(student_list).

student_list=[
     {"name": "Ali", "cgpa": 2.8},
     {"name": "Ahmad", "cgpa": 3.8},
     {"name": "Azeem", "cgpa": 3.2},
     {"name": "Sheroz", "cgpa": 2.5},
     {"name": "Haider", "cgpa": 3.5}
    ]

def get_honor_students(student_list):
    for student in student_list:
        if student["cgpa"]>3:
            print(student["name"])
get_honor_students(student_list)
    