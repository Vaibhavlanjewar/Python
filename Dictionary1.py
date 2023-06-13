"""
Dictionaries only:
are unordered sets;

have keys that can be a variety of data types, including strings, integers, floats, tuples;.

can access dictionary values by keys;

use square brackets inside curly brackets { [ ] };

use colons between the key and the value(s);

use commas to separate each key group and each value within a key group;

make it quicker and easier for a Python interpreter to find specific elements, as compared to a list.

"""
x={}
print(type(x))

file={"jpg":10,'csv':2,'py':6,'c':5}
print(file)
print("Key-value")
print()
print("csv:",file["csv"])

print("jpg in file:","jpg" in file)
print("Add key and value in dict")
file[".vnbl"]=40
print(file)
file["csv"]=6
print(file)
print("Del")

del file["csv"]
print(file)



print()
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for valu in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += valu
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
