from collections import deque

n = int(input())
s = input()

ans = deque()
hantei = False

for i in range(n):
    k = i + 1
    
    if not hantei:
        ans.append(k)
        # print(ans)
    else:
        ans.appendleft(k)
        # print(ans)
    
    if s[i] == "o":
        hantei = not hantei

if hantei:
    ans.reverse()

for i in ans:
    print(i,end=" ")