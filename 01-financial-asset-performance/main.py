prices = [100, 102, 101, 105, 108]

initial_price = prices[0]
final_price = prices[-1]

price_change = final_price - initial_price

percentage_change = (
    price_change / initial_price
) * 100

print("FINANCIAL ANALYSIS")
print("------------------")
print("Initial price:", initial_price)
print("Final price:", final_price)
print("Price change:", round(price_change, 2))
print("Percentage change:", round(percentage_change, 2), "%")