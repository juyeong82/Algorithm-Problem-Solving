# 문제: 백준 11720번 (숫자의 합)
# 날짜: 2026-01-29
# 틀린 이유: input().split() 사용 (입력에 공백이 없으므로 split 없이 문자열 순회 필요)

"""
1. n값 받기
2. numbers 변수에 map() list() 함수이용해서 숫자를 한자리씩 나누어 받기
3. sum 변수 선언

for i in numbers:
    sum 변수에 numbers의 각 자릿수를 가져와 더하기
    
sum 출력
"""

n = input()
numbers = list(map(int, input()))
sum = 0

for i in numbers:
    sum += i
    
print(sum)

