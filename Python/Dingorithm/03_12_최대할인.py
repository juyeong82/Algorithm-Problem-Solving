
# Q. 
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다. 
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

# 정렬 sort 내장함수
# sorted(arr, key=lambda x: x)
# arr.sort(reverse=True)

from collections import deque

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    # 정렬 -> 큐로 변환 -> 최대끼리 매칭 - > 매칭되면 디큐 ->  둘중 하나가 끝날때까지
    prices_queue = sorted(prices, reverse = True)
    coupons_queue = sorted(coupons, reverse = True)
    
    prices_queue = deque(prices_queue)
    coupons_queue = deque(coupons_queue)
    
    charge = 0
    
    if not coupons_queue:
        charge += sum(prices_queue)
        prices_queue = []
        return charge
        
    if not prices_queue:
        charge = 0
        return charge, "가격 배열이 비어있습니다."
        
    while prices_queue and coupons_queue:
        
        max_prices = prices_queue.popleft()
        max_coupons = coupons_queue.popleft()

        # print(max_coupons, max_prices)
        charge += max_prices * (100-max_coupons) / 100
    
    charge += sum(prices_queue)
    prices_queue = []
        
    return charge


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))