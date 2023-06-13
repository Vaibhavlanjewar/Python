# varible length positional argument 

l=[100,200]
l.append(300)
print(l)

print("We have to creat a function in which we add more parameter at a time \n")

def add_val(*args):
    l=[200]
    for i in args:
        l.append(i)
    return l    
    
res=add_val(400,500,600)
print(res)



print("-------------------------------")
print("Variable length Keyword Argument ")
#name,rmail,co_no,dob=

def get_details(**kewargs):
    print(kewargs)

get_details(name="abc",email="abc@gmail.com",contact=1234567890,dob="6-06-2023")

 