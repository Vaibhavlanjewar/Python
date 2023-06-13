def con_sec(sec):
    hr=sec//3600
    min=(sec-hr*3600)//60
    rem_sec=sec-hr*3600-min*60
    return hr,min,rem_sec
result=con_sec(500)
print(result)
print(type(result))

win=["c","c++","python","java"]
for i,j in enumerate(win):
    print("{} - {}".format(i+1,j))