def fact(n):
    print("Factorial of -",n)
    if n<2:
        print("Returning 1 ")
        return 1 
    result=n*fact(n-1)
    print("result:-",result)
    return result
fact(5)
