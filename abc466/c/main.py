n = int(input())
hantei = [False] * (n + 2)

for i in range(1, n):
    print(f"? {i} {i+1}", flush=True)
    user = input()
    if user == "Yes":
        hantei[i] = True

ans = 0
for i in range(1, n):
    if hantei[i]:
        ans += 1  
        right = i + 2
        while hantei[right-1]:
            print(f"? {i} {right}", flush=True)
            user = input()
            
            if user == "Yes":
                ans += 1
                right += 1  
            else:
                break  

print(f"! {ans}", flush=True)