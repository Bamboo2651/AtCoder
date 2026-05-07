n = int(input())
data = []
for _ in range(n):
    abc = list(map(int,input().split()))
    data.append(abc)
dp =[[0 for _ in range(n)] for _ in range(3)]
dp[0][0] = data[0][0]
dp[1][0] = data[0][1]
dp[2][0] = data[0][2]

for i in range(1,n):
    for j in range(3):
        dp[j][i] = max(dp[(j+1) % 3][i-1] + data[i][j],dp[(j+2) % 3][i-1]+data[i][j] )
    
print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))
    
