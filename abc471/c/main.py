n = int(input())
a = list(map(int, input().split()))

ue = []
sita = []

for x in a:
    if x> 0:
        ue.append(x)
    else:
        sita.append(x)

ue.sort()
sita.sort(reverse=True)

current = 0
ans = 0
i = 0
j = 0

while i<len(ue) or j<len(sita):
    if i < len(ue) and j < len(sita):
        distance_ue = abs(current - ue[i])
        distance_sita = abs(current - sita[j])
        
        if distance_sita <= distance_ue:
            ans += distance_sita
            current = sita[j]
            j += 1
        else:
            ans += distance_ue
            current = ue[i]
            i += 1
    elif i < len(ue):
        ans += abs(current - ue[i])
        current = ue[i]
        i += 1
    else:
        ans += abs(current - sita[j])
        current = sita[j]
        j += 1
print(ans)