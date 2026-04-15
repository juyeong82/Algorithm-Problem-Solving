from collections import deque
prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    # 이 부분을 채워주세요!
    prices = deque(prices)
    result = []
    while prices:
        price_not_fall_period = 0
        current_prices = prices.popleft()
        for i in range(len(prices)):
            if current_prices <= prices[i]:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)
        
    
    return result
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))