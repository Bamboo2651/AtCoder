n,m = map(int,input().split())
s= []
for _ in range(n):
    s.append(input())

row = []
for i in range(n):
    if s[i].count("x") == m:
        row.append(i)
if len(row) == 1:
    print("Faucet", row[0]+1)
else:
    for j in range(m):
        x = True
        for i in range(n):
            if s[i][j] != "x":
                x = False
                break
        if x:
            print("Drain", j+1)
            break