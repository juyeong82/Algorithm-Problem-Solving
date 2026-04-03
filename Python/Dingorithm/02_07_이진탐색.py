finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    number = len(array)
    ind = len(array)//2
    while array[ind] != target:
        if target > array[ind]:
            ind = (ind+number)//2
            
        elif target < array[ind]:
            ind = (0+ind)//2
    
    return array[ind], ind

def is_existing_target_number_binary(target, array):
    min = 0
    max = len(array)-1
    
    # 값이 존재하지 않을 때 모순 방지
    while min <= max: 
        cur = (min+max)//2
        if target == array[cur]:
            return array[cur], cur
        elif array[cur] > target:
            max = cur - 1
        elif array[cur] < target:
            min = cur + 1
            
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)