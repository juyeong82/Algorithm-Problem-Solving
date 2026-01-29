# 문제: 백준 11660 (평균)
# 날짜: 2026-01-29
# 시간 복잡도: 단순 합산 시 O(M*N^2)로 약 1,000억 번 연산 필요 
#      -> O(N^2) 합 배열 생성 후 O(1) 질의로 해결 (2차원 구간 합)

# [문제 분석]
# N=1024, M=100,000일 때 매번 합을 구하면 O(M*N^2)로 약 1,000억 번 연산 -> 시간 초과 발생
# 해결: 2차원 구간 합 배열(DP)을 생성하여 O(N^2 + M)으로 해결 (약 110만 번 연산)

# [핵심 공식 1: 합 배열 생성]
# D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]
# 설명: 위쪽 누적합 + 왼쪽 누적합 - 중복 더해진 대각선 + 현재 값

# [핵심 공식 2: 질의 답변(구간 합)]
# (x1, y1) ~ (x2, y2) 까지의 합
# Answer = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
# 설명: 전체 큰 사각형 - 위쪽 영역 - 왼쪽 영역 + 두 번 빠진 대각선 영역 복구
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 인덱스 번호를 맞추기 위한 사전 패딩 추가(n+1) -> A[1][1]이 문제의 (1, 1)과 정확히 일치
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    # 인덱스 번호를 맞추기 위한 패딩 [0]
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합배열 구하기    
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        
# 구간합배열로 질의에 답변
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    
    print(result)
    