n,s,l = map(int,input().split())
a = list(map(int,input().split()))

left = [0]
distance = 0

for i in range(s-2, -1, -1):
    distance += a[i]
    left.append(distance)

right = [0]
distance = 0
for i in range(s -1, n- 1):
    distance += a[i]
    right.append(distance)

ans = 1
r_count = len(right) -1

for l_count in range(len(left)):
    l_distance = left[l_count]

    while r_count >= 0:
        r_distance = right[r_count]

        idou = min(
            l_distance * 2 + r_distance,
            l_distance + r_distance * 2
        )

        if idou <= l:
            break
        r_count -= 1

    if r_count < 0:
        break

    goal = 1 + l_count + r_count

    ans = max(ans, goal)
print(ans)