import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

print(original is shallow)        # False — different outer list
print(original[0] is shallow[0])  # True — SAME inner list
print(id(shallow))
print(id(original))

original[0].append(99)
print(original)   # [[1, 2, 99], [3, 4]]
print(shallow)    # [[1, 2, 99], [3, 4]] 

deep = copy.deepcopy(original)

original[0].append(88)
print(original)  # [[1, 2, 99, 88], [3, 4]]
print(deep)      # [[1, 2, 99], [3, 4]] 