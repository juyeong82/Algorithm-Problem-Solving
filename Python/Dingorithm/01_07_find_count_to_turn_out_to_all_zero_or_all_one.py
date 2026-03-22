input = "01111001110100101"

# =====================
# 내 풀이
# =====================
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 1. 첫번째 인덱스가 0인지 1인지 저장
    fix = string[0]
    idx = []
    # 2. 다음 인덱스를 처음 인덱스와 비교해서 달라지는 인덱스를 저장
    for num in range(1, len(string)):
        if string[num] != fix:
            idx.append(num)  # 1,5,7
            fix = string[num]
    # len(idx): 숫자가 바뀌는 경계선 (ex)경계선 4개면 
    # len(idx)+1: 전체 그룹의 수(A+B) (ex)그룹은 2개짜리, 3개짜리 총 5개가 됨
    # N // 2 -> (A, B)두 그룹 중 개수가 더 적은 쪽의 그룹 수 
    return (len(idx) + 1) // 2

# =====================
# 정답 풀이
# =====================
# 0 -> 1 일때 뒤집는다. -> 전체를 0으로 만드는 작업
# 1 -> 0 일때 뒤집는다. -> 전체를 1으로 만드는 작업

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count_to_all_zero = 0
    count_to_all_one = 0
    
    # 맨 앞 숫자가 바뀌는 경우의 수 추가
    if string[0] == 0:
        count_to_all_one += 1
    elif string[0] == 1:
        count_to_all_one += 1
    
    # idx i랑 i+1을 비교해서 다르면 앞에 숫자가 0이냐 1이냐에 따라 횟수 추가
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == 0:
                count_to_all_one += 1
            elif string[i+1] == 1:
                count_to_all_zero += 1
    
    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)