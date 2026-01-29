#Dictionary methods and operations
#Deep copy
dict1={'a':2,'b':9,'c':5,'d':7}
shared_dict1 = dict1
print(shared_dict1)
print(dict1)
dict1['b']=10
print(dict1)
print(shared_dict1)
shared_dict1['d']=12
print(dict1)
print(shared_dict1)
#Shallow copy
new_dict1 = dict1.copy()
print(new_dict1)
print(dict1)
new_dict1['e']=15
print(new_dict1)
print(dict1)

#Iterating over Keys,Values & Items
students = {'name': 'Aanya','age':11,'class':4}
for key in students.keys():

    print(f'key =>{key}')

    for val in students.values():
        print(f'Value => {val}')

    for dict_key, dict_val in students.items():
        print(f'{dict_key} => {dict_val}')

for dict_key,dict_val in students.items():
    print(f'{dict_key}=>{dict_val}')


