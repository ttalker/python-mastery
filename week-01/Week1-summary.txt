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
Iterable vs. iterator
    Iterables produces new Iterators 
    It is reusable
    Iterators are consumed once
    It maintains iteration state
Example:
    lst = [1,2,3] this is an iterable
    it = iter(lst) this is an iterator

Generators
    consumes less memory
    need the yield keyword

    yield
        - > turns a function into a lazy iterator
    Without generators:
        all data loads immediately
    With generators:
        values produced one at a time

Mutability
    Mutable objects can change -> list, dict, set
    Immutable object cannot be changed -> tuple, str, int

    The tuple is immutable but if it contains a mutable obj you can change it
    Note that this kind of tuple cannot be used as a dictionary key while the others are safe

Default argument trap
    def add(x, lst=[]):
    this kind of list will persist throughout the program
    def add(x, lst=None): this will create a new list everytime 
        if lst is None:
            lst = []

How objects store attributes
    Normal objects are stored in __dict__, it is dynamic but memory heavy
    __slots__ remove per instance dictionary