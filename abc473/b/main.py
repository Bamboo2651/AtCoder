n = int(input())
a = list(map(int, input().split()))
aset = set(a)
ans = 0
for x in aset:
    if a.count(x) % 2 == 1:
        ans += x

print(ans)