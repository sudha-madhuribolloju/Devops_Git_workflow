# String Methods in Python
course = "  Agentic AI is an artificial intelligence system!  "
print("course", course)
#Strip whitespace from both ends
print(course.strip())
# Convert to lowercase
print(course.lower())
# Convert to uppercase
print(course.upper())
# Capitalize the first letter of each word
print(course.capitalize())
#Title case
print(course.title())
#replace a string
New_one=course.replace("AI", "Artificial Intelligence")
print(New_one) #it is not saved to original string
print(course) # Original string remains unchanged
#string counting
Message="Python is great. Python is dynamic. Python is easy to learn."
print(Message.count('python'))
print(Message.lower().count('python'))
# string splitting
print(Message.split('.')) # It converts string to list of strings
# Join a list of strings into a single string
words = ['Python', 'is', 'fun']
print(' '.join(words))
#remove prefix
prefix_text = "unhappiness"
removed_prefix = prefix_text.removeprefix("un")
print("Removed Prefix:", removed_prefix)
# remove suffix
suffix_text = "runningly"
removed_suffix = suffix_text.removesuffix("ly")
print("Removed Suffix:", removed_suffix)
