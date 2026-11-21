n = int(input())
c = list(map(int, input().split()))

INF = 10**18

left = [INF] * n
right = [INF] * n

for i in range(1, n):
    if c[i] != c[i - 1]:
        left[i] = 1
    else:
        left[i] = left[i - 1] + 1

for i in range(n - 2, -1, -1):
    if c[i] != c[i + 1]:
        right[i] = 1
    else:
        right[i] = right[i + 1] + 1

ans = []

for i in range(n):
    ans.append(min(left[i], right[i]))

print(*ans)