x=["all","alt","queen","word","length","size"]
print(type(x))
print("List is Mutable")
print(x)
print(len(x))

print("all" in x)
print("of" in x)
print(x[0])
x.append("zoo")
print(x)

print(x[1:3])

x.insert(0,"Hii")
print(x)
x.insert(10,"10")
print(x)
print("----Remove----")
x.remove("all")
print(x)
x.pop(2)
print(x)
print("change item value")
x[1]="Python"
print(x)
