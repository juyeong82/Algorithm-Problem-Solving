# 알파벳 빈도수
# 1. a,b,c,처럼 문자가 해당 문자열에 얼마나 있는지 파악한다.
# 2. 그 개수가 가장 크다면 반환해줘야 하는 그 알파벳으로 변환한다.

def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurence_array = find_alphabet_occurence_array(string)
    max_occurence = alphabet_occurence_array[0]
    max_index = 0
    for index, i in enumerate(alphabet_occurence_array):
        
        if i > max_occurence:
            max_occurence = i
            max_index = index

    return chr(max_index + ord('a'))

# 알파벳 빈도수 출력
def find_alphabet_occurence_array(string):
    alphabet_occurence_array = [0] * 26
    
    for char in string:
        current_index = 0
        if not char.isalpha():
            continue   # 현재 반복을 건너띔
        
        current_index =  ord(char.lower())-97
        alphabet_occurence_array[current_index] += 1
        
    return alphabet_occurence_array

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))