def  sum_positive_numbers(n):
   
    if n<2:
       return 1 
    result=n+ sum_positive_numbers(n-1)
   
    return result


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15