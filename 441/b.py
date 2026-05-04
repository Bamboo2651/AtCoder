n, m = map(int, input().split())
s = input()
t = input()

q = int(input())
wordList = []
for _ in range(q):
    wordList.append(input())

for word in wordList:
    is_takahashi = True
    is_aoki = True
    
    for char in word:
        if char not in s:
            is_takahashi = False
        if char not in t:
            is_aoki = False
            
    if is_takahashi and not is_aoki:
        print("Takahashi")
    elif is_aoki and not is_takahashi:
        print("Aoki")
    else:
        print("Unknown")