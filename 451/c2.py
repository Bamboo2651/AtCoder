Q = int(input())
tree = []
query = []
for i in range(Q):
    query.append(list(map(int, input().split())))

for que in query:
    a = que[0]
    b = que[1]

    if a == 1:
        left = 0
        right = len(tree)
        while left < right:
            mid = (left + right) // 2
            if tree[mid] < b:
                left = mid + 1
            else:
                right = mid
        tree.insert(left, b)
        
    else:
        left = 0
        right = len(tree)
        while left < right:
            mid = (left + right) // 2
            if tree[mid] <= b:
                left = mid + 1
            else:
                right = mid
        tree = tree[left:]

    print(len(tree))