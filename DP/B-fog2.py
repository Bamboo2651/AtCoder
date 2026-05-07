n,k = map(int,input().split())
h = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = 0
dp[2] = abs(h[1]-h[2])

atai = []
for i in range(3,n+1):
    atai = []
    for j in range(1,k+1):
        if i <= j:
            break
        kosuto = abs(h[i-j]-h[i])
        atai.append(kosuto + dp[i-j])
    dp[i] = min(atai)

print(dp[n])