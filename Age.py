from datetime import date

name=input("Enter your name: ")
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))
birth_time = input("Enter birth time (optional): ")

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day, birth_time):
    age -= 1

print (f"{name}, your age is: {age} years")

