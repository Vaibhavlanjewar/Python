print("-------iterating over the contents of dictionary -------------")
file={"jpg":10,'csv':2,'py':6,'c':5}
for ext in file:
    print(ext)

for i,j in file.items():
    print("There are {} files with the .{} extention".format(j,i))

print("\nkey=",file.keys()) 
print("\nval=",file.values()) 
print()
for val in file.values():
    print(val)
print()

for key in file.keys():
    print(key)
print()

for k,v in file.items():
    print("{} = {}".format(k,v))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
print(wardrobe.update(new_items))

