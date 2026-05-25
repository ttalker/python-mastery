import time
import tracemalloc

l1 = [3, [ 66,55, 44 ], (7, 8, 9)] 
l2 = list(l1)       
l1.append(100)      
l1[1].remove(55)    
print('l1:', l1) 
print('l2:', l2) 
l2[1] += [33, 22]   
l2[2] += (10, 11)   
print('l1:', l1) 
print('l2:', l2)

def ex(mylist=[]):
    mylist.append('hi')
    print(mylist)

# mylist persisting

ex()
ex()
ex()

def ey(mylist=None):
    if mylist == None:
        mylist = []
    
    mylist.append("X")
    print(mylist)

# mylist not persisting creating a new list everytime 
ey()
ey()

# despite being immutable mutating a list inside a tuple is possible

tup : tuple = ('Hello', ['X', 'Y'], "world")

print(tup)
tup[1].append("HELLO!")
print(tup)

# d = {tup: " Value"} has errors

new_tup = (1,2,3)

new_d = {new_tup:"Value"} # no errors



# time of +=

start = time.perf_counter()
result = ""
for i in range(10000):
    result += str(i)  

end = time.perf_counter()
plus_equal = end- start
print((plus_equal) *1000)


start = time.perf_counter()

parts = []
for i in range(10000):
    parts.append(str(i))
result = "".join(parts) 

end = time.perf_counter()
join = end- start
print((join) *1000)

speedup = plus_equal / join

print(f"The join was {speedup} times faster")

# testing memory


class CoordDict:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class CoordSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        

tracemalloc.start()

objs = [
    CoordDict(i, i, i)
    for i in range(100_000)
]

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

mb = peak / 1024 / 1024

print(f"CoordDict: {mb:.2f} MB")

tracemalloc.start()

objs = [
    CoordSlots(i, i, i)
    for i in range(100_000)
]

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

mb = peak / 1024 / 1024

print(f"CoordSlots: {mb:.2f} MB")