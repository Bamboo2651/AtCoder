n = int(input())
l = list(map(int,input().split()))

jukeizu = []
mid = 0.5
midTF = True
count = 0
mae = 0

for i in range(2 ** n):
    nishin = bin(i)[2:].zfill(n)
    # print(nishin)
    mid = 0.5
    midTF = True
    for m in range(n):
        if nishin[m] == "0":
            mid -= l[m]
        else:
            mid += l[m]
        if mid > 0 and midTF == False:
            midTF = True
            count += 1
        elif mid < 0 and midTF == True:
            midTF = False
            count += 1
    mid = 0.5
    mae = max(count,mae)
    count = 0
print(mae)
