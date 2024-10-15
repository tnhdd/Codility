def cyclic_rotation():
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))
    print("You entered:", number_arr)
    rotation = int(input("How many time do you want to rotate? "))
    new_arr = number_arr[rotation:] + number_arr[:rotation]
    print("Rotated array:", new_arr)


cyclic_rotation()
