input = [4, 6, 2, 9, 1]

4 
46
462
426
246
2469

def insertion_sort(array):
    sorted_array = []
    for i in array:
        sorted_array.append(i)
        for j in range(len(sorted_array)-1, 0, -1):
            if sorted_array[j] < sorted_array[j-1]:
                sorted_array[j], sorted_array[j-1] = sorted_array[j-1], sorted_array[j]
            else:
                break
    return sorted_array

# 리스트 내부에서 바로 정렬
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i,0,-1): #1, 21, 321, 4321
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
                
    return array


print(insertion_sort(input)) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))