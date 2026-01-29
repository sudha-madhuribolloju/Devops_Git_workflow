#list basics in python
#Creating a list with different data types
my_list = [10, 3.14, 'Hello', True, [1, 2, 3]]
print("Original List:", my_list)
#creating empty list
empty_list = []
print("Empty List:", empty_list)
#Accessing elements using positive indexing
# if we want specific element use index numbers
print("First Element (Positive Indexing):", my_list[0])
print("Third Element (Positive Indexing):", my_list[2])
#Accessing elements using negative indexing
print("Last Element (Negative Indexing):", my_list[-1])
print("Second Last Element (Negative Indexing):", my_list[-2])
#Checking the id of the list before and after modification
print(id(my_list)) #printing the id of original list
#Modifying elements in the list
my_list[2] = 'World'
print(id(my_list)) #printing the id after modification of element
#appending elements to the list
my_list.append("New")
my_list.append("Old")
print(my_list)
#Getting the length of the list
print("Length of the List:", len(my_list))
#Nested list access
print("Nested List:", my_list[2])
#matrix representation using nested lists
matrix = [[1, 2, [3, 4]],
          [4, 5, 6],
          [7, 8, 9]]
print("Matrix:", matrix)
print(len(matrix))
print("Element at Row 2, Column 3:", matrix[1][2])
print("Element at Row 3, Column 1:", matrix[0][2][0])