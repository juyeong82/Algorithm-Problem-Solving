import sys
input = sys.stdin.readline
suNo, quizNo = list(map(int, input().strip().split()))
numbers = list(map(int, input().strip().split()))

prefix_sum = [0]
sum = 0

for i in numbers:
    sum = sum + i
    prefix_sum.append(sum)
    
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])
    

