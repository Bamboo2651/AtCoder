n, q = map(int, input().split())
p = list(map(int, input().split()))

a_list = []
last = [-1] * (n + 1)

for i in range(q):
    a = int(input())
    a_list.append(a)
    last[a] = i

ans = []
for num in p:
    if last[num] == -1:
        ans.append(num)

for i in range(q):
    a = a_list[i]

    if last[a] == i:
        ans.append(a)

print(*ans)