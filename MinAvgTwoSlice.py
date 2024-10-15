# A non-empty array A consisting of N integers is given. A pair of integers (P, Q),
# such that 0 ≤ P < Q < N, is called a slice of array A
# (notice that the slice contains at least two elements).
# The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q]
# divided by the length of the slice.
# To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:
#     A[0] = 4, A[1] = 2, A[2] = 2, A[3] = 5, A[4] = 1, A[5] = 5, A[6] = 8
# contains the following example slices:
#         slice (1, 2), whose average is (2 + 2) / 2 = 2;
#         slice (3, 4), whose average is (5 + 1) / 2 = 3;
#         slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
#
# The goal is to find the starting position of a slice whose average is minimal.

def min_avg_two_slice():

    num_arr = list(map(int, input("Introduce numbers separate by space ").split()))
    if len(num_arr) < 2:
        return "Array must contain at least 2 elements"
    first_min = second_min = float('-inf')

    for num in num_arr:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num > second_min:
            second_min = num
    print(f"The two minium numbers are: {first_min}  and {second_min}")
    avg = (first_min + second_min)/2
    print(f"Average of those slice is {avg}")


min_avg_two_slice()
