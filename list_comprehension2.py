multiple=[]
for i in range(1,11):
    multiple.append(i*7)
print(multiple)

print("List comprehension")
l=["python","c","c++","java"]
length=[len(l) for l in l]
print(length)
l1=[]
print("no divisible by 3")
a=[l1 for l1 in range(0,101) if l1%3==0]
print(a)

