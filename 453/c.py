N = int(input())
l = list(map(int,input().split()))
mid = 0.5
count = 0
for i in l:
    if mid > 0:
        mid = mid - i
        if mid < 0:
            count += 1
    else:
        mid = mid + i
        if mid > 0:
            count += 1

print(count)