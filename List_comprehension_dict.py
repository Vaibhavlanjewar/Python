l=[100,200,300,400,500,600]
l1=[]
print(l)
for val in l:
    l1.append(val*val)
print("Square--> ",l1)   

print("By using Comprehension ")

l2=[value*value for value  in l]
print(l2)

