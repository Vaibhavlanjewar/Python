#positional argument 

def linear_search(List,Key):
    for val in List:
        if Key==val:
            return True
    else:
        return False        
        
l=[100,200,300,400,500,600]
key=400
result=linear_search(l,key)
print(result)

print("Default Argument\n")

print("WE have to generate pass ")
""" 
8char
1 upp
1 lower
1 special char 
5 digits 


"""
print("ASCII--a to z " ,ord('a'),ord('z') )
print("ASCII--A to Z " ,ord('A'),ord('Z') )

import random

def gen_pass(leng=8):
    l1=['@','!','#','$','&']
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l1)
    digit=random.randint(10000,99999)
    password=upper+lower+special+str(digit)
    l6=random.sample(password,leng)
    password=("").join(l6)

    return password

r=gen_pass(5)
print(r)

print("\n\nKeyword\n")

def validate(username,password):
    if username=="ABC" and password=="abc123":
       print("Valid Password")
    else:
        print("Invalid Password")

validate("ABC","abc123")
validate(password="abc123",username="ABC")

print(100,200,sep=",",end=" ")
print("Hii ")
