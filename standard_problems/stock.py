prices = [100, 180, 260, 310, 40, 535, 695]

buyPrice = 0
total = 0

for i in range(len(prices)-1):
    if buyPrice:        # if looking to sell
        if prices[i] > prices[i+1]:
            total += prices[i] - buyPrice
            buyPrice = 0
    else:
        if prices[i] < prices[i+1]:
            buyPrice = prices[i]
else:
    if buyPrice:
        total += prices[-1] - buyPrice

print(total)
