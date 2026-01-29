#Set and Dictionary Comprehensions
#Set comprehensions
student_names = {'sudha','aanya','lalitha','swaroop','kumar','aanya'}
capital = {name.capitalize() for name in student_names}
print(type(capital)) # Set is unordered and no duplicates
print(capital)

#Dictionary comprehensions
names_fruits= {'apple': 6,'mango': 9,'banana': 5,'orange':3,'kiwi':5}
#create a new dictionary where all values are doubled
new_names_fruits = {key:val *2 for key,val in names_fruits.items()}
print(new_names_fruits)
#create a set of keys(in uppercase) where values are greater than 0.2
