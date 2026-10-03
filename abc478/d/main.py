# 最初はLからRまでの集合にxを実際に追加して、
# 最後にそれぞれの集合の数をlenで求めた
# でも、この方法だと何回も同じ場所を調べるので時間がかかる
# n, q = map(int, input().split())

# inbox = []
# for _ in range(q):
#     l,r,x = map(int, input().split())
#     inbox.append((l,r,x))

# syugo = [[] for _ in range(n)]

# for l,r,x in inbox:
#     for i in range(l-1,r):
#         if x not in syugo[i]:
#             syugo[i].append(x)
# # print(syugo)
# for i in range(n):
#     ans = syugo[i]
#     print(len(ans),end=" ")


# 改善後は、Lでxを追加してR+1でxを外すようにして、
# 今その場所に何種類のxがあるかを数えて答えを求めた
n, q = map(int, input().split())

start = [[] for _ in range( n + 2)]
end = [[] for _ in range( n + 2)]

# inbox = []
for _ in range(q):
    l,r,x = map(int, input().split())
    start[l].append(x)
    end[r+ 1].append(x)
    # inbox.append((l,r,x))
# print("start",start)
# print("end",end)
syugo_count = [0] * (q + 1 )
kazu = 0

ans = []
for i in range(1, n + 1):
    for x in end[i]:
        syugo_count[x] -= 1

        if syugo_count[x] == 0:
            kazu -= 1

    for x in start[i]:
        if syugo_count[x] == 0:
            kazu += 1

        syugo_count[x] += 1

    ans.append(kazu)

print(*ans)
