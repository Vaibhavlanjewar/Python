print( "big" > "small")
def exam_grade(score):
    if score>95:
        grade = "Top Score"
    elif score>=60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65)) # Should print Pass
print(exam_grade(55)) # Should print Fail
print(exam_grade(60)) # Should print Pass
print(exam_grade(95)) # Should print Pass
print(exam_grade(100)) # Should print Top Score
print(exam_grade(0)) # Should print Fail

print("\n")
test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)


print()
def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        IP_description = "Network router"
    elif IP_address == "8.8.8.8" or IP_address == "8.8.4.4":
        IP_description = "Google DNS server"
    elif IP_address == "142.250.191.46":
        IP_description = "Google.com"
    else:
        IP_description = "unknown"
    return IP_description


print(identify_IP("8.8.4.4")) # Should print 'Google DNS server'
print(identify_IP("142.250.191.46")) # Should print 'Google.com'
print(identify_IP("192.168.1.1")) # Should print 'Network router'
print(identify_IP("8.8.8.8")) # Should print 'Google DNS server'
print(identify_IP("10.10.10.10")) # Should print 'unknown'
print(identify_IP("")) # Should Should print 'unknown'    

print("\n")

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

print("Comparision--",((10 >= 5*2) and (10 <= 5*2)))


print("\n Fractional")
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient 
    if denominator == 0 or numerator==0 or numerator==denominator :
        part = 0
    else:
        part = (numerator / denominator) % 1
    return part


print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 3)) # Should print 0.66...
print(fractional_part(5, 2)) # Should print 0.5
print(fractional_part(5, 0)) # Should print 0
print(fractional_part(0, 5)) # Should print 0


