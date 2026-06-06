h,w,k = map(int,input().split())
tizu = []
for _ in range(h):
    s = input()
    tizu.append(s)
print(tizu)
S = [[0] * w for _ in range(h)]
# print(S)