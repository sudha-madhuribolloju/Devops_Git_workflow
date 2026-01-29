"""1.A company has a revenue of 45,897,513.
Calculate its profit, assuming profit is 12.7% of the revenue.
Display the result rounded to two decimal places."""
# company revenue
revenue=45897513
#Profit percentage
profit_percentage=12.7/100
#calculate profit
profit= revenue * profit_percentage
print(profit)
#Display result rounded to two decimals
print(round(profit,2))

'''2.Consider the following string declaration which is part of the output of a Linux command.
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
Try to solve the challenge in more than one way.'''
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
mac_address = my_str.split()[-1]
print(mac_address)

#Another method using slicing
start_index = my_str.index('b4')
mac_address_slice = my_str[start_index:]
print(mac_address_slice)

# 3.Display the following Strings literally:
display_str= """It displayed: "You've got an error!"
\\n means a new line.
\\ is known as the escape character.
"""
print(display_str)

"""4.Write a Python script to convert feet (ft) to centimeters (cm).
Conversion: 1 ft = 30.48 cm
Prompt the user to enter a value in feet.
Display the result in centimeters with two decimal places, formatted using an f-string.
"""
#conversion factor
#ft_to_cm=30.48
#prompt user for input
feet=float(input("Enter value in feet: "))
#convert to centimeters
centimeters= feet * 30.48
#display result
print(f"{feet} feet is equal to {centimeters:} centimeters.")

#5.Write a Python script to check if a string is a palindrome.
string_palindrome = "racecar"
palindrome = string_palindrome[::-1]
if string_palindrome == palindrome:
    print(f"{string_palindrome} is a palindrome.")
else:
    print(f"{string_palindrome} is not a palindrome.")

"""6.Change the solution of the previous challenge to ignore whitespace and letter case when
checking if a string is a palindrome."""
string_palindrome = "ra  ce car"
#remove whitespace and convert to lowercase
cleaned_string = string_palindrome.replace(" ", "").lower()
print(cleaned_string[::-1])

"""Write a Python script that extracts the first and last two characters from a user-entered string.
Example:
Input: "'Hello!'"
Output: 'Heo!'"""
input_result = "'Hello!'"
first_two = input_result[0:3]
last_two = input_result[-3:]
result = first_two + last_two
print(result)

"""Write a Python script that replaces all occurrences of the first 
character in a string with '$', except for the first occurrence itself.
Example:
Input: 'mama'
Output: 'ma$a'"""
input_string = "mama"
first_char = input_string[0]#get the first character
#replace all occurrences of first character with '$' except the first one
modified_string = first_char + input_string[1:].replace(first_char, '$')
print(modified_string)

"""Write a Python program to remove the character at the nth index from a non-empty string.
The nth index is provided by the user."""
input_str = "agenticAIengineer"
n = int(input("Enter the index of the character to remove: "))
#remove character at nth index
modified_str = input_str[:n] + input_str[n+1:]
print(modified_str)

#Write a Python script that removes characters at odd index positions from a given string.
input_str = "agenticAIengineer"
print(input_str[::2]) #slicing method
"""Write a Python script that prompts the user for a circle's radius and calculates its area.
Formula: Area = π * r² (π = 3.1415)
Display the area with four decimal places using an f-string.
"""
radius_circle = float(input("Enter the radius of the circle: "))
pi = 3.1415
area_circle = pi * radius_circle ** 2
print(f"The area of the circle with radius {radius_circle} is {area_circle:.2f}.")
#:.2f for 2 decimal places

#Write a Python script that counts the number of occurrences
# of a substring in a given string, ignoring letter case.
string = "Vasudha"
substring = "sudha"
count = string.lower().count(substring.lower())
print("Number of occurrences:", count)

"""Write a Python script to format a number using:
US/UK format: A comma , as the thousands separator
EU format: A period . as the thousands separator
Example:
Input: 1234567
Output: 1,234,567 (US/UK) and 1.234.567 (EU)
"""
number = 1234567
us_uk_format = f"{number:,}"
eu_format = f"{number:,}".replace(",", ".")
print("US/UK format:", us_uk_format)
print("EU format:", eu_format)










