q,v = map(int,input().split())

battery = []

for _ in range(q):
    query = list(map(int,input().split()))
    # print(query)
    if query[0] == 1:
        t = query[1]
        w = query[2]
        battery.append((t,w))
        # print(battery)
    else:
        t = query[1]

        if len(battery) == 0:
            print(-1)
        else:
            max_w = -1
            max_index = -1

            for i in range(len(battery)):
                time, weight = battery[i]

                current_weight = weight + (t - time)
                if current_weight > v:
                    current_weight = v
                if current_weight > max_w:
                    max_w = current_weight
                    max_index = i 
            
            print(max_w)
            battery.pop(max_index)