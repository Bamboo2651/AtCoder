x, y, l, r, a, b = map(int, input().split())
ans = 0

for t in range(a, b):
    if l <= t and t < r:
        ans += x 
    else:
        ans += y

print(ans)