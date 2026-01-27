#User Inputs- Prompting user for input:
name = input('Enter Your Name:')
print(name)
age = input('Enter Your Age:')
print(name + ' is ' + age + ' years old.')

# Explicit data type conversion
age_next_year = int(age) + 1
print('Next year, ' + name + ' will be ' + str(age_next_year) + ' years old.')
height = float(input('Enter Your Height in inches:'))
print(name + ' is ' + str(height) + ' inches tall.')
