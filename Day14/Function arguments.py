def subtract(a, b):
    return a - b

print(subtract(10, 5))
print(subtract(5, 10))

def student_info(name, age, course):
    print(name, age, course)

student_info("Sudha", 30, "Python")

def employee(name, salary, department):
    print(name, salary, department)

employee(department="Dev", salary=50000, name="Sudha")

#Mixing positional and keyword arguments
def add(a, b, c):
    print(a + b + c)

add(5, b=10, c=15)

def student(name, course="Python", duration=30):
    print(name, course, duration)

student("Sudha")
student("Madhuri",course="Java",duration=60)
student("vasu")
