def fif(page_nums, frame_size):
    pf = 0
    page = []
    for i in range(frame_size):
        page.append(-1)
    for i in range(len(page_nums)):
        flag = 0
        for j in range(frame_size):
            if (page[j] == page_nums[i]):
                flag = 1
                break
        
        if flag == 0:
            fault = False
            new_slot = -1
            for s in range(frame_size):
                if page[s] == -1:
                    fault = True
                    new_slot = s
            
            if not fault:
                max_future = 0
                max_future_s = -1
                for s in range(frame_size):
                    if page[s] != -1:
                        found = False
                        for ii in range(i, len(page_nums)):
                            if page_nums[ii] == page[s]:
                                found = True
                                if ii > max_future:
                                    max_future = ii
                                    max_future_s = s
                                break
                        if not found:
                            max_future_s = s
                            break
                fault = True
                new_slot = max_future_s
            pf += 1
            page[new_slot] = page_nums[i]
    
    return pf
    
pages = [1,2,1,5,0,4,0,0,7,3,1,2,1,5,0,4,0,0,7,3]
frameSize = 4

print(fif(pages,  frameSize))
    