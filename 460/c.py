n,m = map(int,input().split())
syari = list(map(int,input().split()))
neta = list(map(int,input().split()))

syari.sort()
neta.sort()
syarikazu = 0
netakazu = 0
count = 0
while syarikazu < n and netakazu < m:
    if neta[netakazu] <= syari[syarikazu] * 2:
        count += 1
        netakazu += 1
        syarikazu += 1
    else:
        syarikazu += 1
print(count)