# Write a function
# that, given an array A consisting of N integers,
# returns the number of distinct values in array A.

def distinct():
    num_arr = list(map(int, input("Introduce numbers: ").split()))
    counter = len(set(num_arr))
    print(counter)


distinct()
