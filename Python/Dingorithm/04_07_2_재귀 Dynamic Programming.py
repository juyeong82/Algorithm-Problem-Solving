input = 50

def fibo_bottom_up(n):
    # 작은 것부터 미리 다 채워놓기
    dp = {1: 1, 2: 1}

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 아래서 위로 쌓아올리기

    return dp[n]

print(fibo_bottom_up(input))