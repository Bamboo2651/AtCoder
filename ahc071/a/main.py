w,h,k = map(int,input().split())
c = list(map(int,input().split()))
box = [[0,0] for _ in range(k)]
for i in range(k):
    a,b = map(int,input().split())
    box[i][0] = a
    box[i][1] = b

hole = set((x,y) for x,y in box)
# print(hole)

renga = []
place = set()

for x,y in sorted(holes, )