T, X = map(int, input().split())
a = list(map(int, input().split()))

ans = []
save = 0

for i in range(len(a)):
    if i == 0:
        ans.append([i, a[i]])
        save = a[i]
    else:
        diff_hig = a[i] - save
        diff_min = save - a[i]
        
        if diff_hig >= X or diff_min >= X:
            ans.append([i, a[i]])
            save = a[i]

for i in ans:
    print(i[0], i[1])