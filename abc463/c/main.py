from fractions import Fraction

n = int(input())

box = []
for _ in range(n):
    h, l = map(int, input().split())
    box.append([h, l])

q = int(input())
l = list(map(int, input().split()))

for ti in l:
    ans = 0
    for h, l in box:
        if l > ti:
            ans = max(ans,h)
    print(ans)
