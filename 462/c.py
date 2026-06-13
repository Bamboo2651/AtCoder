#間違ってます (TLE)
n = int(input())
x = [[]]
for _ in range(n):
    x.append(list(map(int,input().split())))
# print(x)

count = 0

for i in range(1,n+1):
    ix = x[i][0]
    iy = x[i][1]
    
    hantei = True
    
    for j in range(1, n + 1):
        if i == j:
            continue
        jx = x[j][0]
        jy = x[j][1]
        
        if jx < ix and jy < iy:
            hantei = False
            break
    if hantei:
        count += 1
print(count)