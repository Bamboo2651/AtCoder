n = int(input())
a = []
for i in range(1, n+1):
    box = list(map(int,input().split()))
    a.append(box)
uke = []
for _ in range(n+ 1):
    uke.append([])

for i in range(n):
    box = a[i]
    for target in box[1:]:
        uke[target].append(i+1)
# print(uke)

for i in range(1, n + 1):
    gif = uke[i]
    if len(gif) == 0:
        print(0)
    else:
        count = len(gif)
        print(count, *gif)