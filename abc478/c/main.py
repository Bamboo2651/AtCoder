n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)

first_miss = 0
for i in range(len(b)):
    if b[i] != a[i]:
        first_miss = i
        break

last_miss = 0
for i in range(len(b) - 1, -1, -1):
    if b[i] != a[i]:
        last_miss = i
        break

length = last_miss - first_miss + 1
if length <= k:
    print("Yes")
else:
    print("No")