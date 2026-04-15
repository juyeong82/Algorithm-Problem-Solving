'''
Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.

해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.

현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.

dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
'''
# >>> import heapq

# >>> heap = []
# >>> heapq.heappush(heap, 4)
# >>> heapq.heappush(heap, 1)
# >>> heapq.heappush(heap, 7)
# >>> heapq.heappush(heap, 3)
# >>> print(heap)
# [1, 3, 7, 4]

# >>> print(heapq.heappop(heap)) # 최솟값을 빼는 방법입니다.
# 1
# >>> print(heap)
# [3, 7, 4] # 마찬가지로 힙의 형태가 유지됩니다.

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 0일차  1일  2일  3일  4일
# 4    -> 3 -> 2-> 1 -> 0


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    """
    * 최소 [정상이 되는 시점(supply_recover_k) - 현재 재고(ramen_stock)]을 확보해야 버틸 수 있음.
    * 현재 재고(ramen_stock)보다 같거나 빠른 시점(supply_dates.)모두를 조회해서 최대 공급(supply_supplies) 가능한 시점(supply_dates)을 구한다.
    1. while 현재 재고 < 정상이 되는 시점
        2. 현재 재고 -= 1, i = 0
        3. if 공급일 < 현재 재고:
            4. heappush(supply_supplies), i += 1
        5. if 현재재고 == 0:
            6. 현재재고 += heappop(supply_supplies)
    """
    i = 0
    heap = []
    total_stock = 0
    minimum_count_of_overseas_supply = 0
    # 현재 재고가 정상시점보다 커질때까지 반복
    max = k-stock
    while total_stock < max:
        while i < len(dates) and dates[i] <= stock:
            heapq.heappush(heap, -supplies[i])
            i += 1
        
        if stock == 0:
            stock += (-heapq.heappop(heap))
            total_stock += stock
            minimum_count_of_overseas_supply += 1
        stock -= 1
        
    
    return minimum_count_of_overseas_supply

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    minimum_count_of_overseas_supply = 0
    i = 0
    heap = []
    
    # 확보한 재고(버틸 수 있는 최대 날짜)가 정상화 시점(k)보다 작을 때만 반복
    while stock < k:
        # 현재 보유한 재고로 도달할 수 있는 모든 날짜의 공급량을 힙에 추가
        while i < len(dates) and dates[i] <= stock:
            # 파이썬의 heapq는 Min Heap이므로 음수로 변환하여 Max Heap처럼 사용
            heapq.heappush(heap, -supplies[i])
            i += 1
            
        # 힙에서 가장 큰 공급량을 꺼내어 현재 재고(버틸 수 있는 날짜)에 합산
        if heap:
            stock += -heapq.heappop(heap)
            minimum_count_of_overseas_supply += 1
            
    return minimum_count_of_overseas_supply

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

# 경계값 테스트 케이스들

# 1. stock = k (이미 충분한 경우)
print("정답 = 0 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [5], [20], 10))

# 2. stock = 0 (재고 완전 바닥)
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 10, 15], [20, 10, 15], 35))

# 3. 딱 한 번만 공급받으면 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5], [30], 30))

# 4. 공급 후 stock이 정확히 k가 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10], [20], 30))

# 5. 첫날부터 공급 가능한 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [100], 50))

# 6. k = 1 (최소 기간)
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [10], 1))

# 7. 여러 번 공급받아야 하고 딱 맞아떨어지는 경우
print("정답 = 3 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 5, 10], [5, 5, 5], 15))

# 8. 공급 가능 날짜가 여러 개지만 하나만 선택해야 하는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5, 6, 7], [100, 10, 10], 50))

# 9. 마지막 날에 공급받는 경우
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10, 29], [20, 100], 30))

# 10. stock이 k보다 1 작은 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(29, [29], [100], 30))