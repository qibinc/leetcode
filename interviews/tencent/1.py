# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Input: prices = [7,6,4,3,1]

from typing import List

def max_profit(prices: List[int]) -> int:
    max_price = -1
    max_prof = 0
    for price in reversed(prices):
        max_prof = max(max_prof, max_price - price)
        max_price = max(max_price, price)
    return max_prof

if __name__ == '__main__':
    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([7,6,4,3,1]))
