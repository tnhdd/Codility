# Write a function that, given an array A consisting of N integers,
# returns 1 if there exists a triangular triplet for this array and
# returns 0 otherwise.

def triangle():
    num_arr = list(map(int, input("Introduce numbers: ").split()))
    num_arr.sort()
    for i in range(len(num_arr) - 2):
        if num_arr[i] + num_arr[i+1] >= num_arr[i+2]:
            print(f"Triangular triplet found: {num_arr[i], num_arr[i + 1], num_arr[i + 2]}")
            return

    print("No triangular triplet found")


triangle()
