# creating a Dictionary
example_dictionary = {'student_name': 'sudha', 'age': 30, 'pi': '3.14',
                      'parameters': '124B',(3,4): 1.9,True:'active', 10:'Ten'}
print(example_dictionary)   # Dictionaries are key based accessing
print(type(example_dictionary))   # List and tuple are index based accessing
print(len(example_dictionary))
print(example_dictionary['age'])
print(example_dictionary['parameters'])

#Exception handling : get Function
print(example_dictionary.get('course'))

#New Key-Value Pair
(example_dictionary['age'])= 36
print(example_dictionary)
(example_dictionary['student_name']) = 'Vasu'
print(example_dictionary)
(example_dictionary[True]) = 'active'
print(example_dictionary)

