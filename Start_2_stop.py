def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start != stop:
            return_string += str(start) + ","
            start -= 1
    else:
        return_string = "Counting up: "
        while start != stop:
            return_string += str(start) + ","
            start += 1
    return_string += str(stop)
    return return_string

print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"
