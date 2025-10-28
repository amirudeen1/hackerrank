def countingValleys(steps, path):
    # we count a valley when we go from -1 altitude to 0 
    altitude = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            if altitude == -1:
                valleys += 1
            altitude += 1
        else:
            altitude -= 1
    return valleys
