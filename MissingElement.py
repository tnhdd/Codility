def missing_element():
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))
    number_arr.sort()
    for i in range(1, number_arr[-1]):
        if i not in number_arr:
            print(f"The missing number is {i}")


missing_element()
