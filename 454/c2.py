from collections import deque

n,m = map(int,input().split())

box = dict()

for _ in range(m):
    am, bm = map(int,input().split())
    if am in box:
        box[am].append(bm)
    else:
        syoki = [bm]
        box[am] = syoki
    
# print(box)
koukan = set()
koukan.add(1)
current = deque([1])
# print(current)
# print(box)

while current:
    a = current.popleft()
    # print(a)
    # print(box[a])
        # print(koukan)
    if a in box :
        for i in box[a]:
            if i not in koukan:
                koukan.add(i)
                current.append(i)
        
    # print(current)
# print(box[2])
print(len(koukan))

