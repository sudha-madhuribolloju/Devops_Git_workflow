#Absolute path
file= open("E:\\Mypythonprojects\\Day16\\configuration\\config.txt", "rt")
content= file.read()
print(content)
file.close()
#Relative path
file = open('configuration/config.txt', 'rt')
content = file.read()
print(content)
file.close()

#Reading files into a list
with open('configuration/config.txt') as file:
    content= file.read().splitlines()
    print(content)
    print(type(content))
    print(content[6])
