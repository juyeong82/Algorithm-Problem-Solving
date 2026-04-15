input = 20


def fibo_recursion(n):
    """
    재귀로 피보나치 수열을 구하게 되면 
    같은 계산이 무한정 반복되어 매우 비효율적이게 됨.
    """
    
    if n <= 2:
        return 1
    
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765