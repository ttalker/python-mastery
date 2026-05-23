a = [1, 2, 3]   
b = a           
a.append(4)     
print(b)

b.append(99)

print(id(a)) # 1761505730624
print(id(b)) # 1761505730624

a = [3, 4, 5]

print(id(a)) # 2156674708544 diff id rebinded or rebound (bawal maging rebound)
print(id(b)) # 2156672802880 same id 

x = [1, 2, 3]
y = [1, 2, 3]
print(x is a)
print (x == y)

