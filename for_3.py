def all_numbers(minimum, maximum):
    return_string = ""  # Initializes variable as an empty string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for i in range(minimum, maximum + 1):
        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(i) + " "

    # This .strip command will remove the final space at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2, 6))  # Should be "2 3 4 5 6"
print(all_numbers(3, 10))  # Should be "3 4 5 6 7 8 9 10"
print(all_numbers(-1, 1))  # Should be "-1 0 1"
print(all_numbers(0, 5))  # Should be "0 1 2 3 4 5"
print(all_numbers(0, 0))  # Should be "0"


