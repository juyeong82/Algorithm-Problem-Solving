input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    """
    fibo3 -> memo3? -> 없으면 fibo(3-1) fibo(3-2) 추적 -> 찾으면 저장
    """
    if n not in fibo_memo:
        nth_fibo =  fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
        fibo_memo[n] = nth_fibo
        return nth_fibo
    else:
        return fibo_memo[n]
    
    
    

print(fibo_dynamic_programming(input, memo))