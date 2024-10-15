def odd_occurrences_in_array():
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))
    count = {}
    for number in number_arr:
        count[number] = number_arr.count(number)
        if count[number] % 2 != 0:
            print(f"Left out number is {number}")


odd_occurrences_in_array()
