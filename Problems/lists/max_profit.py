def max_profit(prices):
    
    """
    finds the best times to buy and sell
    assuming you could only buy and sell ONCE
    """
    
    when_to_buy  = prices[0]
    bought_idx   = 0
    when_to_sell = 0

    for idx in range(1, len(prices)):
        if prices[idx] < when_to_buy:
            when_to_buy, bought_idx = prices[idx], idx
            
    when_to_sell = prices[bought_idx + 1]
    for price in prices[bought_idx + 2:]:
        if price > when_to_sell:
            when_to_sell = price

    return  when_to_sell - when_to_buy
            
    
#! O(n^2)

def max_profit_(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)


"""
    EXPECTED OUTPUT:
    ----------------
    Maximum profit: 5


"""