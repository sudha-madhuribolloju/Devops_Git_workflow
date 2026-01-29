#Examples for List comprehension in Python
from Day6.List_Basics import my_list

Students_names = ['sudha', 'madhuri', 'vasu', 'aanya', 'pradyumna']
names_capitalized = [name.capitalize() for name in Students_names]
print(names_capitalized) #list comprehension to string operation

nums_list = [1,6,18,19,21,36,9]
new_list = [num for num in nums_list if num % 6 == 0]
print(new_list) #list comprehension with a condition

nums1 = [2,3,4,5,6]
nums2 = [8,9,4,6,2]
common_elements = [num for num in nums1 if num in nums2]
print(common_elements)

names1 = ['ram', 'shyam', 'hari', 'gita']
names2 = ['gita', 'sita', 'ram', 'laxman']
common_names = [name.capitalize() for name in names1 if name in names2]
print(common_names) #list comprehension to find common elements between two lists

my_list = [5, 12, 17, 18, 24, 29, 33, 40]
new_items = [num *2 for num in my_list if num %3== 0]
print(new_items)
new_items1 = [num for num in my_list if num > 25]
print(new_items1)
