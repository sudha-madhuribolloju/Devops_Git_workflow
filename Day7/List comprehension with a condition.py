#list comprehension syntax
#syntax: [expression for item in iterable if condition]
list=[3,4,5,6,7,8]
new_list=[num*3 for num in list if num>6]
print(new_list)
#list comprehension with a condition
new_list=[num for num in list if num%2!=0] #list comprehension.
print(new_list)
#set comprehension.It does not follow order and no duplicates
new_list={num for num in list if num%2==0} #set comprehension.
print(new_list)