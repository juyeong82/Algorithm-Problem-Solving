input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    length = len(array)
    
    for i in range(length-1): # array 길이 맨 마지막 인덱스 제외 -1번 비교하기 위함
        for i in range(length-1): # 
            # 01 12 23 34 / 01 12 23 / 01 12 / 01 
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        length -= 1
        
    return array

# length -= 1 을 i를 활용해 for문에서 처리
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))