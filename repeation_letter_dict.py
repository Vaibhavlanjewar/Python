def count_let(text):
    res={}
    for letter in text:
        if letter not in res:
          res[letter]=0
        res[letter] +=1
    return res
print(count_let("aaaaaaaa"))         
print(count_let("Vaibhguygvvaiibbhhvvav"))
 