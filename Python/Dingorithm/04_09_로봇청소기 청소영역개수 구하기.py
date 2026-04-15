current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    dr = [-1, 0, +1, 0]
    dc = [0, +1, 0, -1]
    
    # 3, 4, 5, 6 //4  -> 탐색 순서 -> 3, 0 1 2
    # d//4
    # 2345
    # 0->3 3->2 2->1 1->0
    ''' d+3
    cnt_of_clean = 1
    while True:
        for _ in range(4)
            d = (d+3)//4
            if room_map[r+dr[d],c+dc[d]] = 0:
                nr, nc = r+dr[d], c+dc[d]
                room_map[nr, nc] = 2
                r, c = nr, nc
                cnt_of_clean += 1
                break
        2. 네 방향 다 돌았는데도 빈공간이 없으면 후진 후 방향(d) 유지 후진, r, c 갈아 끼우기
        if room_map[r-dr[d],c-dc[d]] == 0:
            r, c = r-dr[d], c-dc[d]
            break
        
        return cnt_of_clean

    '''
    cnt_of_clean = 1
    
    room_map[r][c] = 2
    while True:
        for _ in range(4):
            d = (d+3)%4
            print(r,c,d, r+dr[d],c+dc[d], room_map[r+dr[d]][c+dc[d]])
            if room_map[r+dr[d]][c+dc[d]] == 0:
                nr, nc = r+dr[d], c+dc[d]
                room_map[nr][nc] = 2
                r, c, d = nr, nc, d
                cnt_of_clean += 1
                # print(r,c,d, r+dr[d],c+dc[d], room_map[r+dr[d]][c+dc[d]])
                break
            
        # for 반복문이 break로 중간에 끊기지 않고 끝까지 다 돌았을 때만 실행
        else:
            if room_map[r-dr[d]][c-dc[d]] != 1:
                r, c = r-dr[d], c-dc[d]
            
            elif room_map[r-dr[d]][c-dc[d]] == 1:
                break
            
    return cnt_of_clean


# 57 가 출력되어야 합니다!
print("정답 = 57 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))