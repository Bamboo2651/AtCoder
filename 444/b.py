n,k = map(int,input().split())
def a(i):
    m = str(i)
    ans =0
    for c in m:
        ans += int(c)
    return ans

count = 0
for i in range(1, n+1):
    if a(i) == k:
        count += 1
        
print(count)