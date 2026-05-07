n = int(input())
h = [0] +list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = 0
dp[2] = abs(h[1]-h[2])

for i in range(3,n+1):
    iti = abs(h[i-1]-h[i]) + dp[i-1]
    ni = abs(h[i-2]-h[i]) + dp[i-2]
    dp[i] = min(iti,ni)

print(dp[n])