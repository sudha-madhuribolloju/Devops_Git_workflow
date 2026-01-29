#Lambda Expression
#Subtraction
Sub = (lambda a,b : a-b) (9,4)
print(Sub)
#Cube
Cube = lambda a=3:a**3
print(Cube(3))
#sorting
fruits_name = [('Apple',10),('banana',6),('guava',4),('orange',8)]
fruits_name.sort(key=lambda a:a[1])
print(fruits_name)
#length base sorting
fruits_name.sort(key=lambda fruit : len(fruit[0]))
print(fruits_name)
