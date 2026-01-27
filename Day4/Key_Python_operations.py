#Augmented Assignment Operators
# 1. Addition Assignment (+=)
x = 5
x += 3  # Equivalent to x = x + 3
print("After += operation, x =", x)
#2. Subtraction Assignment (-=)
y = 10
y -= 4  # Equivalent to y = y - 4
print("After -= operation, y =", y)
#3. Multiplication Assignment (*=)
z = 6
z *= 2  # Equivalent to z = z * 2
print("After *= operation, z =", z)
#4. Division Assignment (/=)
a = 20
a /= 5  # Equivalent to a = a / 5
print("After /= operation, a =", a)

#Comparison Operators
p = 7
q = 7
print("p == q:", p == q)  # True # Equal to (==)
print("p != q:", p != q)  # False # Not equal to (!=)
print("p > q:", p > q)  # False # Greater than (>)
print("p < q:", p < q)  # False # Less than (<)
print("p >= q:", p >= q)  # True # Greater than or equal to (>=)
print("p <= q:", p <= q)  # True # Less than or equal to (<=)
print("p <= q:", p <= q)  # True # Less than or equal to (<=)

#Identity Operators
x=3
print(id(x)) # printing the id of x
x=5
print(id(x)) # The id changes when the value of x is changed,since integers are immutable
list1 = [1, 2, 3]
print(list1)
print("id(list1):",  id(list1))
list1.append(10)
print(list1)
print(id(list1)) # The id remains the same after modification




