def missing_int():
    # Read input from user
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))
    positive_number = set(x for x in number_arr if x > 0)
    smallest_missing = 1
    while smallest_missing in positive_number:
        smallest_missing += 1
    print(smallest_missing)


missing_int()