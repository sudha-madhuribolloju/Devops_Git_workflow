file = open('configuration/config.txt', 'rt')
content = file.read()
print(content)
file.close()

with open('configuration/config.txt', 'rt')as file:
    content = file.read(10)
    print(content)
    print(file.closed)
