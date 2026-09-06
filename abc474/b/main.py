n = int(input())
p = list(map(int, input().split()))

hantei = True

for i in range(n -1):
    ima = (p[i] - 1) // 10
    tugi = (p[i + 1] - 1) // 10
    if ima > tugi:
        hantei = False
        break

if hantei:
    print("Yes")
else:
    print("No")