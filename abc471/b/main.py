n = int(input())

counts = {}

for _ in range(n):
    s = input().lower()
    
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
    
max_count = max(counts.values())
print(max_count)