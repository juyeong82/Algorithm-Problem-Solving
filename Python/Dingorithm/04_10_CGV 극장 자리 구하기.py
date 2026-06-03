'''
1. 입장권에 있는 자리 or 자리의 왼쪽/오른쪽 앉을 수 있음
2. ex) 7번 입장권 => 678 가능
3. [예외] VIP 회원은 입장권 좌석에만 앉을 수 있음.

seat_count = 9
vip_seat_array = [4, 7]
[케이스 분리 후 각 경우의 수 곱하기]
[1-2-3] | 4(VIP) | [5-6] | 7(VIP) | [8-9]
-> 3 x 1 x 2 x 1 x 2 = 12

[2명] dp[i=2]
1 2
2 1

[3명] dp[i=3]
1 2 3   # 1. 3번째 사람이
2 1 3   # 3번째에 앉을때
1 3 2   # 2. 3번째 사람이 옆 사람과 바꿔 앉을 때

[4명] dp[i=4]
1 2 3 4  # 1. 4번째 사람이 4번째에 앉을때 dp[i-1]
2 1 3 4 
1 3 2 4  
1 2 4 3 # 2. 3번째 사람이 옆 사람과 바꿔 앉을 때 dp[i-2]
2 1 4 3
'''
seat_count = 9
vip_seat_array = [4, 7]

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    #   (0), 1, 2
    dp = [1, 1, 2]
    
    for i in range(3, total_count+1):
        dp.append(dp[i-1] + dp[i-2])
        # print(dp)

    length = len(fixed_seat_array)
    result = 1
    j = 0
    
    for i in fixed_seat_array: # 4 -> 7
        '''
        [1-2-3] | 4(VIP) | [5-6] | 7(VIP) | [8-9]
        -> dp[4-(0+1)] x 1 x dp[7-(4+1))]2 x 1 x dp[10-(7+1)] = 12   
        
        length = len(vip_seat_array)
        result = 1
        1. i = 4
        result *= dp[i-(j+1)]
        j = i
        length -= 1
        2. i = 7
        result *= dp[i-(j+1)]
        j = i
        length -= 1
        3. 
        if length == 0:
            result *= dp[10-(j+1)]
            
        1(VIP) | [2-3] | 4(VIP) | [5-8] | 9(VIP)
        -> dp[1-(0+1)] x 1 x dp[7-(4+1))]2 x 1 x dp[9-(4+1)] x dp[10-(9+1)] = 12   
        
        '''      
        result *= dp[i-(j+1)]
        print(i, j, result, length)  
        j = i
        length -= 1
        
        if length == 0:
            result *= dp[(total_count+1)-(j+1)]
            print((total_count+1), j, result)  
            break
        
    return result


# 12가 출력되어야 합니다!
print("정답 = 12 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("(9,[2,4,7]) / 정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("(11,[2,5]) / 정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("(10,[2,6,9]) / 정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))