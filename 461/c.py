n,k,M = map(int,input().split())
box = []
for i in range(n):
    c,v = map(int,input().split())
    box.append((v,c,i))

# print(box)
box.sort(reverse=True)
# print(box)

data = {}
for v, c, number in box:
    if c not in data:
        data[c] = number
# print(data)
toridasi = box[:k]
nokori = box[k:]
# print(toridasi)
# print(nokori)

select_num = {}
for v, c, number in toridasi:
    if c not in select_num:
        select_num[c] = 0
    select_num[c] += 1

ima = len(select_num)

goukei = sum([v for v, c, number in toridasi])

if ima >= M:
    print(goukei)
else:
    new_add = []
    for v, c, number in nokori:
        if c not in select_num and data[c] == number:
            new_add.append((v, c, number))
    sakujo = []
    for v, c, number in reversed(toridasi):
        if select_num[c] > 1:
            sakujo.append((v, c, number))
            select_num[c] -= 1
            
    aa = M - ima
    for i in range(aa):
        goukei += new_add[i][0]
        goukei -= sakujo[i][0]
        
    print(goukei)