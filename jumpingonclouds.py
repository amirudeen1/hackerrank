def jumpingOnClouds(c):
    
    jumps = 0
    position = 0
    n = len(c)
    
    while position < n-1: 
        if position + 2 < n and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1 
    return jumps
