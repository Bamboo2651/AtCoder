n, m = map(int, input().split())

a = []
b = []
for i in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

box = []
box.append(1)

koukan = True
while koukan:
    koukan = False
    for i in range(m):
        if a[i] in box and b[i] not in box:
            box.append(b[i])
            koukan = True

print(len(box))