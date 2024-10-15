# Write a function that, given a non-empty array A of N integers,
# returns the maximum number of flags that can be set on the peaks of the array.

def flag(num_arr):
    peaks = []
    position = []
    for i in range(1, len(num_arr)):
        if num_arr[i] > num_arr[i - 1] and num_arr[i] > num_arr[i + 1]:
            peaks.append(num_arr[i])
            position.append(i)

    peaks = list(dict.fromkeys(peaks))
    count = len(peaks)

    print(f"There are {count} peaks, those are {peaks}, position in array {position}")


array = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
flag(array)
