#Nested Dictionaries
company= {
    'employee-1' : {'name': 'sudha','role': 'Developer','age':35},
    'employee-2' : {'name' : 'vasu', 'role': 'Admin','age':40}
}
print(company['employee-2']['age'])
print(company['employee-1']['role'])

#Merging Dictionaries with update()
Employee = {'name': 'sudha','role': 'Developer','age':35}
Details = {'surname' : 'bolloju', 'salary': 50000,'age':37}
Employee.update(Details)
print(Employee)
print(len(Employee))# Duplicate will be taken

#clearing a dictionary
Employee.clear()
print(Employee)
#pop  (pop is Key based not value based)
age = Details.pop('age')
print(age)
print(Details) # pop is going to return value
#Delete
Last_item = Details.popitem()  # Deleted the last item
print(Last_item)
del Details['surname']
print(Details)