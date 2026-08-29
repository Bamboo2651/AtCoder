n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n // 2, n):
    ans += a[i]

print(ans)