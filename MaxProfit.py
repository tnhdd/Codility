# Write a function, that, given an array A consisting of N integers containing
# daily prices of a stock share for a period of N consecutive days,
# returns the maximum possible profit from one transaction during this period.
# The function should return 0 if it was impossible to gain any profit.

def find_max_profit():
    price_arr = list(map(int, input("Type the price in ").split()))
    min_price = price_arr[0]
    max_profit = 0
    min_day = 0
    buy_day = sell_day = None

    for i in range(1, len(price_arr)):
        current_profit = price_arr[i] - min_price

        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = min_day
            sell_day = i

        if price_arr[i] < min_price:
            min_price = price_arr[i]
            min_day = i
    if max_profit > 0:
        print(f"Maximum possible profit: {max_profit}")
        print(f"Buy on day {buy_day + 1}, price = {price_arr[buy_day]}")
        print(f"Sell on day: {sell_day + 1}, price = {price_arr[sell_day]}")
    else:
        print("There is not possible profit")


find_max_profit()

