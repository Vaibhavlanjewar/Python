l=[100,200,300,400,500]
print(sum(l))

print(max(l))
print(min(l))

num=25.2555
print(round(num))
print(num,2)

#print(dir(__builtins__))

#help(__builtins__)

import math 
l1=[0.1]*10
print(l1)
print(sum(l1))

n1=15.5559
print(math.floor(15.5559),math.ceil(15.5559))

print(math.sqrt(25))
print(math.factorial(5))

n2=45.5556
print(math.modf(n2))

d , i=math.modf(n2)
print(d, i)

print(math.pow(10,2))
print(math.log(10,2))

print(math.log10(2))
print(math.log2(10))

print(math.sin(0))
print(math.sin(30))
print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))

#help(nath)
print("\n\nRANDOM ")
import random
print(random.random())

l5=[1,2,3,4,5,6]
print(random.choice(l5))

print("Raaandom num from given range ")
print(random.randint(10,100))

print(random.randrange(10,100)) # 100 is not inclusive

print(random.uniform(10,20))
