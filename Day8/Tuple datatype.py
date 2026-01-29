# Tuple datatype in Python
# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)
# Tuples are immutable, so we cannot modify elements
# my_tuple[2] = 100  # This will raise a TypeError
#tuple to list conversion
tuple_as_list = list(my_tuple)
print("Tuple converted to List:", tuple_as_list)
print(type(my_tuple))
#list to tuple conversion
list_data = [1, 2, 3, 4, 5]
list_as_tuple = tuple(list_data)
print("List converted to Tuple:", list_as_tuple)
print(type(list_as_tuple))
print(len(my_tuple))
#unpacking tuples
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)
#matrix representation using nested tuples
matrix_tuple = ((1, 2, (3, 4)),
                (4, 5, 6),
                (7, 8, 9))
print(matrix_tuple[1][2])
print(matrix_tuple[0][2][0])
print(len(matrix_tuple))

# Index numbers specification
# Accessing elements using positive and negative indexing
print( my_tuple[0])
print( my_tuple[3])
print( my_tuple[-1])
print( my_tuple[-3])
# my_tuple[2] = 100  # This will raise a TypeError

#Membership testing using 'in' operator
numbers = (1, 2, 3, 4, 5, 3, 2, 1)
print(numbers)
num = 2
if num in numbers:
    print(f"{num} found in the tuple.")
else:
    print(f"{num} not found in the tuple.")

#slicing tuples
print(my_tuple[1:4]) #slicing from index 1 to 3
print(my_tuple[0:5:2]) #slicing with step value 2
print(my_tuple[::-1])#slicing with negative step value (reversing)
