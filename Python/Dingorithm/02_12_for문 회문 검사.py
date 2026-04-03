input = "abcba"

def is_palindrome(string):
    # 홀수면 가운데 자리는 하나니까 검사 안하고 넘어가도 됨.
    for i in range((len(string))//2):
        if string[i] != string [-i-1]:
            return False
    return True
print(is_palindrome(input))