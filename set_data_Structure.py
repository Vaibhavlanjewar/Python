#Set
""" 
Sets Are Mutable 
All elements shouls be Unique 
Immutable Elements in the Set - int float tuple str 
unorderd 

"""
s={10,20,30,100}
print(s)
s.add(101)
print("Add 101 to set\n",s)

s1={10,20,30,40,50}
s2={10,40,60,80,30}
s3=s1.union(s2)
print("s1 -",s1,"\ns2 -",s2)
print("Union of s1 and s2 = ",s3)

s4=s1.difference(s2)
print("difference s1-s2 ",s4)

s5=s1.symmetric_difference(s2)
print("symmetric_difference i.e common element not part of output \n ",s5)

print("Update operation of sets ")
print("before update s1 and s2  ",s1,"\n",s2)
s1.update(s2)
print(s1)

a1={1,2,3,4,5,6}
a2={1,2,8,9,0,4}
print("a1",a1)
print("a2",a2)

a1.symmetric_difference_update(a2)
print("symmetric_difference_update a1=",a1)

b1={1,2,3,4,5,6,7,8,9}
b2={1,2,3,4}
print("b1=",b1)
print("b2=",b2)
print("Is b2 is subset of b1---",b2.issubset(b1))

b2.add(64)
print("b2-",b2)
print("Is b2 is subset of b1---",b2.issubset(b1))

print("b1 is supperset of b2 ",b1.issuperset(b2))


print("Typecasting of list to set ")
l1=[100,200,300,400]
l2=[50,100,150,200]

s3=set(l1)
s4=set(l2)
print("list-->set ",s3,s4)

s5=s3.union(s4)
print("s3 union s4 = ",s5)
s6=sorted(s3)
print("Sorted -",s6)

l3=list(s3)
l4=list(s4)
print("set to list -->",l3,l4)


print("delete operation \n-pop\n-remove\n-discard\n-clear\ndel")

k={1,2,3,4,5,6,7,7,8}
print("k=",k)
rt=k.pop()
print("Pop ",k, "poped elem =",rt)

k.remove(5)
print("remove 5--",k)

k.discard(7)
print("discard 7 --",k)

k.clear()
print("clear ", k)