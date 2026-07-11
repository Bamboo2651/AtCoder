n = int(input())
hantei = [False] * n

for i in range(1, n):
    print(f"? {i} {i+1}", flush=True)
    user = input()
    if user == "Yes":
        hantei[i] = True

ans = 0
for i in range(1, n):
    if hantei[i]:
        ans += 1

        if i + 1 < n and hantei[i+1]:
            print(f"? {i} {i+2}", flush=True)
            user = input()
            if user == "Yes":
                ans += 1

print(f"! {ans}", flush=True)