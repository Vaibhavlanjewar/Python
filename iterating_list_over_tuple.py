def full_email(people):
    res = []
    for email,name in people:
        res.append("{} <{}>".format(name,email))
    return res

print(full_email([("vnl@gmail,com","cnl@gmail.com"),
                   ("pnl@gmial.com","sd@gamil.com")]))
    

def group_list(group, users):
  members =", ".join(users) 
  return(" {}: {}".format(group, members)) 

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"