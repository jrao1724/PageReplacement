import fifo, farthest_in_future, least_recently_used

pages = [1,2,1,5,0,4,0,0,7,3,1,2,1,5,0,4,0,0,7,3]
frameSize = 4

print("FIFO:", fifo.fifo(pages, frameSize), "page faults")
print("Farthest in Future:", farthest_in_future.fif(pages, frameSize), "page faults")
print("Least Recently Used:", least_recently_used.lru(pages, frameSize), "page faults")