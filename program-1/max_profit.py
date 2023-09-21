def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    buy_day = -1
    sell_day = -1
    
    for i, price in enumerate(prices[1:], start=1):
        if price < min_price:
            min_price = price
            buy_day = i
        else:
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit
                sell_day = i
    
    if max_profit > 0:
        return max_profit, buy_day, sell_day
    else:
        return -1

def test_max_profit():
    # Test Case 1: Normal input
    assert max_profit([7, 1, 5, 3, 6, 4]) == (5, 1, 4)
    
    # Test Case 2: All decreasing prices
    assert max_profit([7, 6, 5, 4, 3, 2, 1]) == -1
    
    # Test Case 3: All increasing prices
    assert max_profit([1, 2, 3, 4, 5, 6, 7]) == (6, 0, 6)
    
    # Test Case 4: One price
    assert max_profit([1]) == -1
    
    # Test Case 5: Two prices
    assert max_profit([1, 2]) == (1, 0, 1)
    
test_max_profit()
