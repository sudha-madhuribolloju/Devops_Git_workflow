#List operations Slicing in Python
my_list = [5, 10, 15, 20, 25]
print(my_list[1:5]) #slicing from index 1 to 4
# I want the output as [5,15,25]
print(my_list[0:5:2]) #slicing with step value 2
# I want the output as [5,10,15]
print(my_list[:3]) #slicing from start to index 2
#Reversing the list using slicing
print(my_list[::-2])# slicing with negative step value
#Reversing the list using reverse() method
my_list.reverse() #reversing the original list
print(my_list)
'''For Reversing we use both slicing and reverse() method'''
#Sorting the list using sort() method
my_list.sort() #sorting the original list in ascending order (by default)
print(my_list)
my_list.sort(reverse=True) #sorting the original list in descending order
print(my_list)
#Using sorted() function to sort without modifying the original list
new_list = [30, 10, 20, 50, 40]
sorted_list = sorted(new_list) #returns a new sorted list in ascending order
print(new_list)
print(sorted_list)
#Using sorted() function to sort in descending order
sorted_list_desc = sorted(new_list, reverse=True)
print(sorted_list_desc)


