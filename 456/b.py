me =[]
for _ in range(3):
    row = list(map(int,input().split()))
    me.append(row)

count = 0
total = 0

for one in me[0]:
    for two in me[1]:
        for three in me[2]:
            total += 1
            if sorted([one,two,three]) == [4,5,6]:
                count += 1

ans = count / total

print(f"{ans:.10f}")