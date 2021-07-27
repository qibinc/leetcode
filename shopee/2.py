import json

if __name__ == "__main__":
    s = input()
    # s = "[[1, 2, 3, 4, 5, 6], 0]"
    s = json.loads(s)
    prices = list(map(int, s[0]))
    fee = int(s[1])

    hold = [0] * len(prices)
    no_hold = [0] * len(prices)
    hold[0] = -prices[0] - fee

    for i in range(1, len(prices)):
        no_hold[i] = max(no_hold[i - 1], hold[i - 1] + prices[i])
        hold[i] = max(hold[i - 1], no_hold[i - 1] - prices[i] - fee)

    print(max(no_hold + hold))
