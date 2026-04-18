n, m = map(int, input().split())
a = list(map(int, input().split()))

seen = []
ans1 = True
for x in a:
    if x in seen:
        ans1 = False
        break
    seen.append(x)

ans2 = True
for i in range(1, m + 1):
    if i not in seen:
        ans2 = False
        break

if ans1:
    print("Yes")
else:
    print("No")

if ans2:
    print("Yes")
else:
    print("No")