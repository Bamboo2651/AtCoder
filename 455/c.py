from collections import Counter

n,k = map(int,input().split())
a = list(map(int,input().split()))
kouho = Counter(a)
# print(kouho)

total = sum(a)
eikyou = []
for atai, kazu in kouho.items():
    eikyou.append(atai * kazu)
# print(eikyou)

# for i in range(len(eikyou)):
#     for j in range(len(eikyou)-1):
#         if eikyou[j] < eikyou[j+1]:
#             eikyou[j], eikyou[j+1] = eikyou[j+1], eikyou[j]
eikyou = sorted(eikyou,reverse=True)
# print(eikyou)


for i in range(min(k,len(eikyou))):
    # m = max(eikyou)
    total -= eikyou[i]
    # eikyou[eikyou.index(m)] = 0

print(total)