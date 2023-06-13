#function to reuse code ,modularity ,


def value_reverse(value):
    if type(value)==list or type(value)==str:
       rev=value[::-1]
       print(rev)
    else:
        temp=str(value)
        rev=temp[::-1]
        print(rev)   
    return rev


s="python,html,css"
print(s.index("html"))
r=value_reverse(s)
print(r)

l=[100,200,300,400]
a=value_reverse(l)
print(a)