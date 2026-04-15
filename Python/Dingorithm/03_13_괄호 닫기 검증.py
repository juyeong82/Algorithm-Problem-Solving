# Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.

# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

### 내 풀이 ###

# 0. deque로 변환
# 1. 앞에서부터 꺼냈을때 처음은 무조건 (이 나와야 한다.
# 2. char = popleft() 하며 순차 제거하며, () 개수를 각각 순차 기록
# 3. )가 (의 개수를 초과하면 안됨.
# 4. while deque를 빠져나오면, )가 ( 개수와 일치하는지 확인

def is_correct_parenthesis(string):
    from collections import deque
    string_queue = deque(string)
    l_par = 0
    r_par = 0
        
    if string_queue.popleft() == '(':
        l_par += 1
    else:
        return False
    
    while string_queue:
        
        char = string_queue.popleft()
        if char == '(':
            l_par += 1
        elif char == ')':
            r_par += 1
        
        if r_par > l_par:
            return False
        
    if l_par == r_par:
        return True
    else:
        return False
    
# 더 효율적인 풀이
def is_correct_parenthesis(string):
    balance = 0

    for char in string:
        if char == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))