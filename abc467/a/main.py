h, w = map(int, input().split())

if w * 10000 >= 25 * h * h:
    print("Yes")
else:
    print("No")