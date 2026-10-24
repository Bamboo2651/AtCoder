n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

if a[0] == k:
    count += 1


for i in range(n-1):
    a_num, b_num = a[i], a[i+1]
    if a_num < b_num:
        if a_num < k <= b_num:
            count += 1
    else:
        if b_num <= k < a_num:
            count += 1

print(count)