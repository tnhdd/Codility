# find the maximal product of any triplet.

def MaxProduct():
    num_arr = list(map(int, input("Introduce numbers: ").split()))
    max1 = max2 = max3 = float('-inf')
    for num in num_arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num
    # return max1, max2, max3
    max_product = max1 * max2 * max3
    print(f"Max product of any triple is: {max_product}, from {max1}, {max2}, {max3}")



MaxProduct()
