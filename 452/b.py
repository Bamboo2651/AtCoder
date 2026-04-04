H, W = map(int,input().split())

for h in range(H):
    for w in range(W):
        if h == 0 or h == H-1 or w == 0 or w == W-1:
            print("#",end="")
        else:
            print(".",end="")
    print()