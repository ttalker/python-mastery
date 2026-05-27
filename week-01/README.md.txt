This document will be to summarize what I learned this week together with some small projects

Dunder methods are magic methods.
In, python everything is an object and when you call a function it is actually running those magic methods

Trying to run len(x), in python it actually calls, x.__len__() or actually type(x).__len__(x)
__repr__ controls the print(), and repr(). This controls how objects are printed, if not specified in a class it will print the memory address shi
__add__ controls the addition, implementing it like a + b actually calls a.__add__(b), specifying it in ur class controls how objects will behave when adding it
__radd__ is when the __add__ fucntion returns something like NotImplemented or it is missing, then it will call b.__radd__(a)
    -> __radd__ is called when __add__ returns NotImplemented and when the left operand cannot handle the operation
__iter__ controls the iteration of object like for x in obj: Python calls iter(obj), then it will call obj.__iter__()
__next__ controls the iteration state next(iterator)
    -> it must return the next value and at one point it must raise StopIteration
__eq__ controls the '=='. Without implementing this it compares each object's identity which usually returns false unless they point to the same memory object
    -> tells when two objects are equal
    -> implementing this breaks the __hash__, because python cannot guarantee hash correctness so python automatically disables it. 
__hash__ tells whether an object can be used as a dictionary key or set. 
    -> the object must be hashable to be able to be used as a dict key

Important Concepts
