import sys

lst = [1,2,3]

for x in lst:
    print(x)

for x in lst:
    print(x)

it = iter([1,2,3])

for x in it:
    print(x)

for x in it: # prints nothing
    print(x)





# build an iterator class 
# Build ArithmeticProgression(start, step, stop) as a class with __iter__ and __next__
# It must raise StopIteration when the sequence is complete
# Prove it is consumed: loop over it twice, show the second loop produces nothing
# Print the sequence for AP(0, 2, 10) — should give 0 2 4 6 8

class ArithmeticProgression:

    def __init__(self, start, step, stop):
        self.current = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.stop:
            raise StopIteration

        value = self.current

        self.current += self.step

        return value

ap = ArithmeticProgression(0, 2, 10)

for x in ap:
    print(x)
else:
    print("done first loop")
# next loop 

for  x in ap:
    print(x)

else:
    print("done second loop")
    
# generators

lst = [x for x in range(100000)]

gen = (x for x in range(100000))

print(sys.getsizeof(lst)) 
print(sys.getsizeof(gen)) 