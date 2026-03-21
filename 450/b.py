N = int(input())

C = {}
for i in range(1, N):
    sen = list(map(int, input().split()))
    for k in range(len(sen)):
        j = i + 1 + k
        cost = sen[k]
        C[(i, j)] = cost
ans = False
for a in range(1, N - 1):
    for b in range(a + 1, N):
        for c in range(b + 1, N + 1):
            if C[(a, b)] + C[(b, c)] < C[(a, c)]:
                ans = True
                break
        if ans: break
    if ans: break

if ans:
    print("Yes")
else:
    print("No")