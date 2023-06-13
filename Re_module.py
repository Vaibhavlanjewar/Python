import re
"""
. ---- match with any charecter 
[a-z]  -- it is chare class for small letters 
[a=zA-Z]---cap
[0-9] --digit class 
  math for only single charecter 

+--- alteast once [a-z]
*--- zero or more 

^ -- start of string 
$ -- end of the string 
?-- optional 


""" 
s="ABCDR1234A"

r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]&")
l=re.findall(r,s)
print(l)


print("Check whether Phone no is valid or not")
s1="9049899756"
r1=re.compile("[6-9][0-9]{9}")
l1=re.findall(r1,s1)
print(l1)  

# dd-mm-yyyy

s3="12-05-2018"
r3=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l3=re.findall(r3,s3)
print(l3)  