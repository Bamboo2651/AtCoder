N=int(input())
T=list(map(int,input().split()))

box=[]
for i in range(N):
    box.append((T[i],i+1))

box.sort()
print(box[0][1], box[1][1], box[2][1])
