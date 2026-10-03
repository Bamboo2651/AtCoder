n, v = map(int, input().split())
w = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            price = (i + 1) + (j + 1) + (k + 1)

            if price <= v:
                uresisa = w[i] + w[j] + w[k]
                ans = max(ans, uresisa)

print(ans)