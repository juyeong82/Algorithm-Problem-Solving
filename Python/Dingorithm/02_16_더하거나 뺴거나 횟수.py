"""
Q. 음이 아닌 정수들로 이루어진 배열이 있다. 
이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target_number이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
"""

numbers = [1, 1, 1, 1, 1]
target_number = 3

[2, 3, 1]
+2 +3 +1
+2 +3 -1 

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    sum_array = []
    cnt=0
    def count_plus_minus(array, current_index, current_sum):
        if current_index == len(array):
            sum_array.append(current_sum)
            return
        
        count_plus_minus(array, current_index+1, current_sum+array[current_index])
        count_plus_minus(array, current_index+1, current_sum-array[current_index])
            
    count_plus_minus(array, 0, 0)
    print(sum_array)
    for i in sum_array:
        if i == target:
            cnt+=1
    return cnt
    
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    
    def count_plus_minus(current_index, current_sum):
        # 배열 끝까지 왔을 때 (Base Case)
        if current_index == len(array):
            # 타겟과 같으면 성공(1), 다르면 실패(0)를 반환함
            return 1 if current_sum == target else 0
        
        # 왼쪽 길(더하기)에서 성공한 개수와 오른쪽 길(빼기)에서 성공한 개수를 합산함
        plus_way = count_plus_minus(current_index + 1, current_sum + array[current_index])
        minus_way = count_plus_minus(current_index + 1, current_sum - array[current_index])
        
        # 합산된 결과를 위로 배달(return)함
        return plus_way + minus_way
            
    # 최종적으로 합산된 총 개수를 반환함
    return count_plus_minus(0, 0)

# get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number)
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!