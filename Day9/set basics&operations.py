#Set basics and operations
set_ids = {101, 102, 103, 104, 102, 101}  # Duplicates will be ignored
print("Set with Duplicates Ignored:", set_ids)
print(len(set_ids))
# Creating an empty set
emptyset = {}  # This creates an empty dictionary, not a set
print(type(emptyset))  # Output: <class 'dict'>
empty_set = set() #calling set() function to create empty set
print(empty_set)
print(type(empty_set))
names = ['Sudha Madhuri', 'Vasu srinu', 'Ravi kumar', 'pradyu bolloju', 'Aanya venkata']
print(names)
unique_names = set(names)  # Converting list to set to get unique names
print(unique_names)
#adding elements to a set
unique_names.add('Anjali kumar')
print(unique_names) # No insert and append methods for set
unique_ids = {1,3,4,5,8}
immutable_element = tuple([6,8,9]) # Creating a tuple to add as an immutable element
unique_ids.add(immutable_element) # we can add list and tuple to set
print(unique_ids)
#unique_ids[3]=10  # 'set' object does not support item assignment

