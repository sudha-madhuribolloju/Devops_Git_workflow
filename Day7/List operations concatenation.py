#List operations concatenation
L1=[8,9]
print(L1,id(L1))
#creates a new list concatenation
L1=L1+[4,5] # memory id will change
print(L1,id(L1))
L1+=[7,8] # memory id will not change
print(L1,id(L1))
#extend
L1.extend([10,11]) # memory id will not change
print(L1,id(L1))
#append
L1.append([12,13]) # memory id will not change
print(L1,id(L1))
