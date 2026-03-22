input = 20

# =====================
# 내 풀이(틀림)
# =====================
# 문제점1) 한번이라도 안나눠지면 소수가 되어버림(ex: 9 -> 2로 못나눠서 소수로 추가됨.)
# 문제점2) range의 특성으로 인해 number-1 까지만 확인하고 number는 확인하지 않음.
def find_prime_list_under_number(number):
    prime_list = [2]
    if number > 2: 
        for num in range(3, number):
            # num = 5
            count = 0
            for i in range(2, num):
                
                if num % i == 0:
                    break
                else:
                    if count > 0:
                        continue
                    count += 1
                    prime_list.append(num)
                    
    elif number == 2:
        prime_list.append(2)
        
    return prime_list

# =====================
# 1차 개선 풀이 (모든 수로 나눠보기)
# =====================
# 1. for-else 사용하여 루프가 끝날 때까지 한 번도 나눠지지 않았을 때 소수로 추가

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

# =====================
# 2차 개선 풀이 (이하 소수로만 나눠보기)
# =====================
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


# =====================
# 3차 개선 풀이 (N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.)
# 예를 들어 N = 29인지 확인하려면:

# - √29 ≈ 5.38이니까 5 이하의 소수(2, 3, 5) 로만 나눠보면 됩니다.
# - 2, 3, 5 중 어느 것도 29를 나누지 못하면 → 29는 소수!
# -> 만약 N에 약수가 있다면 그 약수 쌍 중 하나는 반드시 √N 이하이기 때문
# =====================
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if i*i <= n and n % i == 0: # 이하이므로 반드시 =이 들어가야함.
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)