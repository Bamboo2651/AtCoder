h, w = map(int, input().split())
grid = [input() for _ in range(h)]


ans = 0
for r1 in range(h):
    for r2 in range(r1, h):
        for c1 in range(w):
            for c2 in range(c1, w):
                taisyou = True
                th = r2 - r1 + 1
                tw = c2 - c1 + 1
                
                for i in range(r1, r1 + (th + 1) // 2):
                    for j in range(c1, c1 + tw):
                        ni = r1 + r2 - i
                        nj = c1 + c2 - j
                        if grid[i][j] != grid[ni][nj]:
                            taisyou = False
                            break
                    if not taisyou:
                        break
                if taisyou:
                    ans += 1

print(ans)