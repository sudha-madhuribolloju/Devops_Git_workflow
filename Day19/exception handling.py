#Exception handling using try, except,else, finally
from logging import exception

try:
    with open('sudha.txt','r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnf_error:
    print("The file was not found. Please check the file path:{fnf_error}")
else:
    print("No exceptions occurred. File read successfully.")
finally:
    print("Exception handling block has been executed.")

#How to handle specific type of exception in Python?
while True:
    try:
        number = int(input("Enter a number: "))
        reciprocal = 1 / number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The reciprocal of {number} is {reciprocal}")
        break
    finally:
        print("Attempt to compute reciprocal completed.")





#Raise or custom exception
try:
    age = 4
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
         print("Minor.")
    else:
         print("Adult")
except exception as e:
    print(f"An error occurred: {e}")
