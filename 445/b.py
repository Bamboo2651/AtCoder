n = int(input())
m = 0
tbox=[]
for i in range(n):
    tbox.append(input())
    if len(tbox[i]) >= m:
        m = len(tbox[i])

for i in tbox:
    ten = m -len(i)
    ten = ten // 2
    print("."*ten+i+"."*ten)