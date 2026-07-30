n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s1_a = a.copy()
s0_a = a.copy()

s0_right_count =0
s1_right_count = 0

for i in range(1, n):
    if i == 1:
        if a[i-1] % 2 == 0:
            s1_a[i-1] = a[i-1] + 1
            s1_right_count += 1
        else:
            s0_a[i-1] = a[i-1] + 1
            s0_right_count += 1
    
    #先頭0の右側
    if (s0_a[i-1] + s0_a[i]) % 2 != b[i-1]:
        s0_a[i] = s0_a[i] + 1
        s0_right_count += 1

    #先頭1の右側
    if (s1_a[i-1] + s1_a[i]) % 2 != b[i-1]:
        s1_a[i] = s1_a[i] + 1
        s1_right_count += 1

print(min(s0_right_count, s1_right_count))  