#Returning Values From Functions single value
def square(num):
    return num * num

result = square(4)
print(result)
#A function with no return statement
def greet(name):
    """Placeholder function does nothing"""
value = greet("sudha")
print(value)
#Returns multiple values
def myfunc(x):
    """Returns multiple values"""
    return x,x**2,x**3,x**4
result=myfunc(9)
print(result)