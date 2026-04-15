'''
1. 입장권에 있는 자리 or 자리의 왼쪽/오른쪽 앉을 수 있음
2. ex) 7번 입장권 => 678 가능
3. [예외] VIP 회원은 입장권 좌석에만 앉을 수 있음.

seat_count = 9
vip_seat_array = [4, 7]
[케이스 분리 후 각 경우의 수 곱하기]
[1-2-3] | 4(VIP) | [5-6] | 7(VIP) | [8-9]

[2명]
1 2
2 1

[3명]
1 2 3   # 1. 3번째 사람이
2 1 3   # 3번째에 앉을때
1 3 2   # 2. 3번째 사람이 옆 사람과 바꿔 앉을 때

[4명]

'''
seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    return


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))