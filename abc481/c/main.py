q = int(input())
query = {}

for _ in range(q):
    s = input()

    if s  not in query:
        query[s] = len(query) + 1
    print(query[s])
# print(query)