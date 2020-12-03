def fifo(page_nums, frame_size):
    f = -1
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
            f = (f + 1) % frame_size
            page[f] = page_nums[i]
            pf += 1
            
    return pf
    
pages = [1,2,1,5,0,4,0,0,7,3,1,2,1,5,0,4,0,0,7,3]
frameSize = 5

print(fifo(pages, frameSize))