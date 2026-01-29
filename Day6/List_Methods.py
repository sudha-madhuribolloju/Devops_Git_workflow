#CRUD operations using List Methods in Python
list_data = [10, 3.14, 'Sudha', True]
print("Original List:", list_data)
#append() - Adding an element to the end of the list
print(list_data.append([1, 2, 3]))  # Appending a nested list
print("After append:", list_data)
#extend() - Extending the list by adding elements from another iterable
list_data.extend(['Agentic', 'AI'])
print("After extend:", list_data)
#insert() - Inserting an element at a specific index
list_data.insert(3, 'Madhuri')
print(len(list_data))
print("After insert:", list_data)
#remove() - Removing the first occurrence of a specific element
list_data.remove(3.14)
print("After remove:", list_data)
#clear() - Removing all elements from the list
list_data.clear()
print(len(list_data))
#pop() - Removing and returning an element at a specific index
list_data1 = [10, 20,30,40]
print("Popped Element:", list_data1.pop(2))  # Removing element at index 2
print("After pop:", list_data1)
