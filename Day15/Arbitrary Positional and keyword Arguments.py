def add_numbers(number,*args):
    add = number + sum(args)
    return add
print(add_numbers(2,5,9,5))
print(add_numbers(2))

def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Sudha", "Madhuri", "Aanya")

def greet(*names):
    return ' '.join(names)
print(greet("Sudha","Madhuri","Aanya"))

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Sudha", age=35, city="Hyderabad")
print_kwargs(physics_marks=78,maths_marks=97,science_marks=74)
