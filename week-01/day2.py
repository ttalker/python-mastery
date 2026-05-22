import math
from itertools import zip_longest
class Vector2d():
    def __init__(self, components):
        self.components = list(components)
        
    def __repr__(self):
        return f'Vector2d({self.components})'
    
    def __abs__(self): 
        return math.hypot(*self)
    
    
    def __iter__(self):
        return iter(self.components)

    def __add__(self, other):
        try:
            pairs = zip_longest(self, other, fillvalue=0.0) 
            return Vector2d(a + b for a, b in pairs)
           
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other):
        if other == 0: #dunno why this works but it does
            return self

        return self + other
    
    def __bool__(self):
        return bool(abs(self))
    
    def __mul__(self, scalar): 
        return Vector2d(n * scalar for n in self) 
    
    def __rmul__(self, scalar): 
        return self * scalar
    
    
    
    
v1 = Vector2d((5,6))
v2 = Vector2d([3, 5])
v3 = 0
print(v1) # repr
print(abs(v1)) # abs
print(bool(v3)) # truthiness dunno what that means
print(v1 *3)
print(2 * v2) # scalar
print(sum([v1,v2]))
