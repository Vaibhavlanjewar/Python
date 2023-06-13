l=[10,20,30,40,50,60,70,80,90]

key=7
"""
Binary Search Algorithm 
--no of ele=9
mid=9/2=4
[60,70,80,90]
mid =4/2=2
800==700
[600,700]

mid=2/2=1
700==700 return 2

"""
print(l)

print("Binary Search ")
def binary_search(l,key):
    if len(l)==0:
        return False 
    else:

        mid=len(l)//2
        if l[mid]==key:
           return True
        elif key<l[mid]:
             return True
        elif key<l[mid]:
             return binary_search(l[:mid],key)
        else:
            return binary_search(l[mid+1:],key)
    


r= binary_search(l,key)
print(r)

