n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

w = [1] * n
hantei = False

for i in range(n):
    if a[i] > b[i]:
        w[i] = 10**18
        hantei = True
        break

if hantei:
    print("Yes")
    print(*w)
else:
    print("No")
