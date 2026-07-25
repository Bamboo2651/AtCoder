m,d = map(int,input().split())
s = input()

gud =[False] * m

for i in range(m):
    if s[i] == "G":
        left = max(0, i-d)
        right = min(m-1, i+d)
        for j in range(left, right+1):
            gud[j] = True

ans = 0
for a in gud:
    if not a:
        ans += 1
print(ans)