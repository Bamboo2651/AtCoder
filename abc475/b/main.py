n = int(input())
a = list(map(int, input().split()))

ichi = 0
juu = 0
hyaku = 0

for i in range(n):
    price = a[i]

    satu = price // 1000

    if price % 1000 != 0:
        satu += 1

    oturi = satu * 1000 - price

    hyaku += oturi // 100
    oturi %= 100

    juu += oturi // 10
    oturi %= 10

    ichi += oturi

print(ichi, juu, hyaku)