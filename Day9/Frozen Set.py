#Immutable object and no duplicates allowed - Frozen Set
new_frozenset = frozenset([1, 2, 3, 4, 5, 2, 3])  # Duplicates will be ignored
print(new_frozenset)   # No add operation for frozenset
print(len(new_frozenset))
print(type(new_frozenset))
#examples for frozenset operations
set_a = frozenset([1, 2, 3, 4])
set_b = frozenset([3, 4, 5, 6])
# Union
set_union = set_a.union(set_b)
print(set_union)
