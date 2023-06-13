import re
s3="12-05-2018"
r3=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
m=re.search(r3,s3)
print(m)
if m:
    print(m.group())
else:
    print("Pattern Not Found")    

    