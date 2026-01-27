#List operations Iterations and membership testing in Python
my_list = [2, 4, 6, 8, 10]
#Iterating through the list using for loop
for item in my_list:
    print(item)
    print(id(item))
# In list (my_list) take each element and assign to item one by one
#Membership testing using 'in' operator
target_element = 6
for item in my_list:
    if target_element in my_list:
        print(f"{target_element} found in the list.")
    else:
        print(f"{target_element} not found in the list.")

#same reference from one list to another
list_x=[3,4,5]
list_y=list_x  # both list_x and list_y point to same memory location
print(list_y)
#appending an element to list_y
list_y.append(6)
print(list_y,id(list_y)) #list_x will also reflect the change
print(list_x,id(list_x)) #list_x will also reflect the change
#To avoid this we can create a copy of the list
list_a=[1,2,3]  #shallow copy
list_b=list_a.copy() # list_b is a copy of list_a
print(list_b,id(list_b))
#appending an element to list_b
list_c=list_a.copy() # create another copy of list_a
list_c.append(7) #deep copy
print(list_c,id(list_c))
print(list_b,id(list_b))
print(list_a,id(list_a))






