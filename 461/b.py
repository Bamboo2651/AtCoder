n = int(input())
a = [0] + list(map(int, input().split()))
# print(a)
b = [0] + list(map(int, input().split()))

hantei = True
for i in range(1, n + 1):
    hito = a[i]
    mega = b[hito]
    if mega != i:
        hantei = False
        break
if hantei:
    print("Yes")
else:
    print("No")