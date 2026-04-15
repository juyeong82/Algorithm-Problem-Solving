#각 시점에서, 처음으로 현재 가격보다 낮은 가격이 나올 때까지의 시간을 구하라.
# 단, 하락한 시점도 시간에 포함한다.

from collections import deque

prices = [1, 2, 3, 2, 3]

# 가격이 떨어질때까지의 기간 (3314 이면 3, 1까지 떨어진 시점까지 1초씩 추가)

def get_price_not_fall_periods(prices):
    # 이 부분을 채워주세요!
    result = []
    prices = deque(prices)
    
    # 1,2,3,4 / 2,3,4 / 3,4 / 4
    for i in range(len(prices)):
        # i = 0,1,2,3,4
        price_not_fall_period = 0
        for j in range(i+1, len(prices)): # j = 1,2,3,4
            if prices[j] >= prices[i]:
                price_not_fall_period += 1
            elif prices[j] < prices[i]:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)
            
    
    return result
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))