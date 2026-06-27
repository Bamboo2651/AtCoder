n,m =map(int,input().split())

current_color = [0] * (n + 1)
change_day = [[] for _ in range(m + 1)]
color_cnt = [0] * (n + 1)


for i in range(1, n + 1):
    a, d, b = map(int, input().split())

    if d == 1:
        current_color[i] = b
    else:
        current_color[i] = a
        if a != b:
            change_day[d].append([i, b])
total = 0
for i in range(1,n + 1):
    c = current_color[i]
    if color_cnt[c] == 0:
        total += 1
    color_cnt[c] += 1
print(total)


for day in range(2, m + 1):

    for tori_num, next_color in change_day[day]:
        old_color = current_color[tori_num]
        color_cnt[old_color] -= 1
        
        if color_cnt[old_color] == 0:
            total -= 1
            
        if color_cnt[next_color] == 0:
            total += 1 
            
        color_cnt[next_color] += 1
        current_color[tori_num] = next_color
    
    print(total)