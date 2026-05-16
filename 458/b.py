H, W = map(int, input().split())

for r in range(H):
    row_counts = []
    for c in range(W):
        count = 4
        if r == 0:
            count -= 1 
        if r == H - 1:
            count -= 1 
        if c == 0:
            count -= 1
        if c == W - 1:
            count -= 1
        row_counts.append(count)
    
    print(*row_counts)