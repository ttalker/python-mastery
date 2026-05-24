import sys
import gc

a = [1, 2, 3]   
b = a           
a.append(4)     
print(b)

b.append(99)

print(id(a)) # same id 
print(id(b)) # same id

a = [3, 4, 5]

print(id(a)) # diff id rebinded or rebound (bawal maging rebound)
print(id(b)) # points to same id as before

x = [1, 2, 3] 
y = [1, 2, 3] 
print(x is a)
print(f"x id: {id(x)}, y id: {id(y)}") # different ids
print (x == y) # same values different objects

print(sys.getrefcount(a)) # 2
c = a
print(sys.getrefcount(a)) # 3 after c = a

del c

print(sys.getrefcount(a)) # went back to two


num1 = 5
num2 = 5

print(f"num1 id: {id(num1)}, num2 id: {id(num2)}") # same id

class Node():
    def __init__(self,name):
        self.name = name
        self.ref = None
        
    def __del__(self):
        print(f"deleted {self.name}")
        
a = Node("a")
b = Node("b")

a.ref = b
b.ref = a

print(f"a: {sys.getrefcount(a)}, b: {sys.getrefcount(b)}")
del a
del b

collected = gc.collect()
print(f"gc collected {collected} objects")
