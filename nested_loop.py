for outer_loop in range(2, 6+1):
    print("initial Val of outer loop- ",outer_loop)
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)
    