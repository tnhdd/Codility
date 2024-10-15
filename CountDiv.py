# Write a function:
#     def solution(A, B, K)
# that, given three integers A, B and K,
# returns the number of integers within the range [A B] that are divisible by K, i.e.:
#     { i : A ≤ i ≤ B, i mod K = 0 }
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

def count_div():
    first_num = int(input("Introduce first number "))
    second_num = int(input("Introduce second number "))
    third_num = int(input("Introduce third number "))
    counter = 0
    for i in range(first_num, second_num):
        if i % third_num == 0:
            counter += 1

    print(f"From {first_num} to {second_num} there are {counter} divisible by {third_num}")


count_div()
