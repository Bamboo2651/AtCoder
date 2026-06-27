h,w = map(int,input().split())
c_box = []
for i in range(h):
    c = list(input())
    c_box.append(c)

top = h
bottom = -1
left = w
right = -1

for r in range(h):
    for c in range(w):
        if c_box[r][c] == '#':
            
            if r < top:
                top = r
            if r > bottom:
                bottom = r
            
            if c < left:
                left = c
            if c > right:
                right = c

for r in range(top, bottom + 1):
    ans = c_box[r][left : right + 1]
    for char in ans:
        print(char,end="")
    print()