input = "abadabac"

# =====================
# 내 풀이
# =====================
def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    occurence_dict = {}
    for char in string:
        if char not in occurence_dict:
            occurence_dict[char] = 0
        occurence_dict[char] += 1
        
    for char in string:  # 원본 문자열 순서대로 확인
        if occurence_dict[char] == 1:
            return char
        
    return "_"

# =====================
# 정답 풀이
# =====================
def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    occurence_list = [0]*26
    for char in string:
        if not char.isalpha():  # ← 이 줄 필수!
            continue
        occurence_list[ord(char)-ord('a')] += 1
        
    for char in string:  # 원본 문자열 순서대로 확인
        if not char.isalpha():  # ← 이 줄 필수!
            continue
        if occurence_list[ord(char)-ord('a')] == 1:
            return char
        
    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))