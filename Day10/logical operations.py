#Get all the Keys,Values,Items
Employee = {'name': 'sudha','role': 'Developer','age':35}
Details = {'surname' : 'bolloju', 'salary': 50000,'age':37,'role': 'admin'}
print(Employee.keys())
print(Employee.values())
print(Employee.items())

#testing membership using in
print('name' in Employee.keys())
print(35 in Details.values())
print(('name','sudha') in Employee.items())

# find common keys between two dictionaries using logical AND
Common_keys = Employee.keys() & Details.keys()
print(Common_keys)

#Merging dictionaries using Logical OR
merged_dict = Employee|Details
print(merged_dict)