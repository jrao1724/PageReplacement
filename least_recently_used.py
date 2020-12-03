def lru(page_nums, frame_size):
    x = 0
    pf = 0
    page = []
    for i in range(frame_size):
        page.append(-1)
    for i in range(len(page_nums)):
        flag = 0
        for j in range(frame_size):
            if page[j] == page_nums[i]:
                flag = 1
                break
        
        if flag == 0:
            if page[x] != -1:
                minimum = 99999
                for k in range(frame_size):
                    flag = 0
                    j = i
                    while j >= 0:
                        j -= 1
                        if page[k] == page_nums[j]:
                            flag = 1
                            break
                    if flag == 1 and minimum > j:
                        minimum = j
                        x = k
            page[x] = page_nums[i]
            x = (x + 1) % frame_size
            pf += 1
    
    return pf