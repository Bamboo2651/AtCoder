Q = int(input())
tree=[]
query = []
for i in range(Q):
    query.append(list(map(int,input().split())))

for que in query:
    a = que[0]
    b = que[1]

    if a == 1:
        tree.append(b)
    else:
        chenge = []
        for t in tree:
            if t > b:
                chenge.append(t)

        tree = chenge
    print(len(tree))