l=[1,2,3,4,5]
l1=[9,8,7,6,0]
d= dict(zip(l,l1))
print(d)

p=[1,2,3,4,5,6,7,8,9]
d=dict.fromkeys(p)
print(d)
d1=dict.fromkeys(p,5) # defualt value 
print(d1)

p1={1:1,2:2,3:3,4:4,5:5}
p2={1:1,2:4,3:9,4:16,5:25}
p1.update(p2)
print(p1)
 
print("delete items ")

print("Dict P- ",p)

print("pop",p.pop())
r=p.pop(1)
print(p,r)

print("p1= ", p1)
r1=p1.popitem()
print(p1,r)

