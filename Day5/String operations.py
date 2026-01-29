#string operations
#Index based string operations
Quotation = "Nothing is Impossible!"
# Accessing characters using positive indexing
first_char = Quotation[0]
fifth_char = Quotation[4]
print("First Character (Positive Indexing):", first_char)
print("Fifth Character (Positive Indexing):", fifth_char)
# Accessing characters using negative indexing
last_char = Quotation[-1]
second_last_char = Quotation[-2]
print("Last Character (Negative Indexing):", last_char)
print("Second Last Character (Negative Indexing):", second_last_char)
string1 = "Hello"
string2 = "How is it going"
concatenated_string = string1 + ", " + string2 + "!"
print("Concatenated String:", concatenated_string) # only strings concatenate
print('Version' + str('3.14.5')) # converting number to string to concatenate
# String repetition
repeated_string = string1 * 3
print("Repeated String:", repeated_string)