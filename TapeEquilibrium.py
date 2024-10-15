def tape_equilibrium():
    # Read input from user
    number_arr = list(map(int, input("Enter integers separated by space: ").split()))

    total_sum = sum(number_arr)  # Calculate the total sum of the array
    left_sum = 0
    minimal_different = float('inf')
    position = -1

    for i in range(1, len(number_arr)):
        left_sum += number_arr[i - 1]  # Add the current element to the left sum
        right_sum = total_sum - left_sum  # Calculate the right sum
        difference = abs(left_sum - right_sum)  # Calculate the absolute difference

        # If the current difference is smaller, update the minimal difference and position
        if difference < minimal_different:
            minimal_different = difference
            position = i

    print(f"The total sum is {total_sum}")
    print(f"The minium difference is {minimal_different}, position {position}")


tape_equilibrium()
