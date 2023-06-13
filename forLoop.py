#for n in range(x, y, z):
#    print(n)

for n in range(0,11,2):
    print(n)


print()
for n in range(1, 10, 2):  
    print(n)
print()

for x in range(2, -2, -1):
    print(x)    

print("---------------------------Nested Loops----------------------------------------")

for left in range(7):
    for right in range(left,7):
        print("["+str(left)+"|"+str(right)+"]",end="")
    print() 

print("\n============================================================")
team=['C','C++','Java','Python','C#']
for home_team in team:
    for any_team in team:
        if home_team != any_team:
            print(home_team," vs ",any_team)

print("\n--------------")
for n in range(6,18+1,3):
    print(n*2)
print(" for loops will print all even numbers from 0 to 18")
for n in range(19):
    if n % 2 == 0:
        print(n)

print("-----------")
for n in range(0,18+1,2):
    print(n*2)
print("\n Cube ")    
for i in range(1,11):
  print(i**3)

print("-----------Multiple Of Seven----------")  
for i in range(0,100,7): 
    print(i)