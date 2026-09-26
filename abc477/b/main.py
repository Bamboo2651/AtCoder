n,d = map(int,input().split())
x = list(map(int,input().split()))

hito = []

for i in range(n):
    hito.append((x[i], i + 1))

hito.sort()
# print(hito)

ans = []

for i in range(n):
    x, num = hito[i]
    is_left = True
    is_right = True

    if i>0:
        left_x = hito[i - 1][0]
        if x - left_x < d:
            is_left = False

    if i < n - 1:
        right_x = hito[i + 1][0]
        if right_x - x < d:
            is_right = False

    if is_left and is_right:
        ans.append(num)

ans.sort()
print(len(ans))
print(*ans)