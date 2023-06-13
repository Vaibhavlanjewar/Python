#funvtion call itself 

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial((n-1))


num=5
result=factorial(num)
print("Factorial of ",num,"=",result)

"""
Execution

factorial (5) -- 5*fact(4)=5*4*3*2*1=120
                    4*fact(3)=4*3*2*1=24
                       3*fact(2) =3*2*1=6
                           2*fact(1) =2*1=2
                                  1

                                  """
