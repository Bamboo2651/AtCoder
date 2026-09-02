n,q = map(int,input().split())
a = list(map(int,input().split()))
q_box = []
for _ in range(q):
    query =[]
    k = int(input())
    b = list(map(int,input().split()))
    query.append(k)
    query.append(b)
    q_box.append(query)
# print(q_box)

for i in range(q):
    b = q_box[i][1]
    num = 0
    select = []
    for i in a:
        num += 1
        if num not in b:
            select.append(i)
    num = 0
    print(min(select))