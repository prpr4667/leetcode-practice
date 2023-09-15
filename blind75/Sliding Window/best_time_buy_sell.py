def maxProfit(prices):
    buy, profit = 0, 0

    for i in range(len(prices)):
        if prices[i] < prices[buy]:
            buy = i
        else:
            profit = max(profit, prices[i] - prices[buy])

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
