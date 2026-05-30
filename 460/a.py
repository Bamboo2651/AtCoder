n,m = map(int,input().split())
count = 1
while True:
    x = n % m
    if x == 0:
        break
    else:
        count += 1
        m = x
print(count)