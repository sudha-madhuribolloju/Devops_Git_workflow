#Dictionary packing and unpacking
#Function demonstrating dictionary packing using **kwargs

def profile(**info):
    print(f'profile information:{info}')
profile(name = "Sudha", age = 40, location = "Hyderabad")
profile(name = "vasu", age=45, location = "pune")

def student(name, age, grade):
    print(f'Details of student: name:{name}, age: {age}, grade:{grade}')

data = {"name": "pradyu", "age": 20, "grade": "A"}

student(**data)