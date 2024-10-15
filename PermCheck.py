def perm_check():
    # Read input from user
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))
    number_arr.sort()  # Sort the array
    print(number_arr)

    for i in range(len(number_arr)):
        if number_arr[i] != i + 1:
            print("The given array is not permutation")
            return

    print("The given array is permutation")


perm_check()
