def binary_gap():
    number = input("Introduce number: ")
    number_in_binary = bin(int(number))[2:]
    print(f"{number} in binary is {number_in_binary}")
    gaps = number_in_binary.strip('0').split('1')

    if gaps:
        longest_gap = max(len(gap) for gap in gaps)
        print(f"The longest binary gap is : {longest_gap}")
    else:
        print("No binary gap found")


binary_gap()
