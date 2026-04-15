array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

# 1. for문만 사용 제일 비효율
def merge(array1, array2):
    merged_array = []
    start = 0

    for i in range(len(array2)):
        inserted = False

        for j in range(start, len(array1)):
            if array1[j] < array2[i]:
                merged_array.append(array1[j])
            else:
                merged_array.append(array2[i])
                start = j
                inserted = True
                break
        
        # array2가 array1의 모든 원소보다 커서 삽입이 안되면
        if not inserted:
            start = len(array1)
            merged_array.append(array2[i])
            
    # array2를 다 처리한 뒤에도 array1에 남은 값이 있으면
    for j in range(start, len(array1)):
        merged_array.append(array1[j])

    return merged_array


# while 사용 투 포인터 방식
def merge(array1, array2):
    # 이 부분을 채워보세요!
    merged_array = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            merged_array.append(array1[array1_index])
            array1_index += 1
        else:
            merged_array.append(array2[array2_index])
            array2_index += 1
            
    while array1_index < len(array1):
        merged_array.append(array1[array1_index])
        array1_index += 1
        
    while array2_index < len(array2):
        merged_array.append(array2[array2_index])
        array2_index += 1
    return merged_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))