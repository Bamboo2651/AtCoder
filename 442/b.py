q = int(input())
oto = 0
saisei = False
hantei = []
for i in range(1,q+1):
    a = int(input())
    if a == 1:
        oto += 1
    elif a == 2 and oto >= 1:
        oto -= 1
    elif a == 3 and saisei == False:
        saisei =  True
    elif a == 3 and saisei == True:
        saisei = False

    if oto >= 3 and saisei == True:
        hantei.append("Yes")
    else: 
        hantei.append("No")

for i in hantei:
    print(i)