p,q = map(int,input().split())
x,y = map(int,input().split())

result = False
if p <= x < p+100 and q <= y < q+100:
    result = True
if result :
    print("Yes")
else:
    print("No")
