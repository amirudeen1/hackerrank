def repeatedString(s, n):
    # count a in s
    a_per_set = s.count('a')
    
    # find total sets and remainder
    sets = n // len(s)
    remainder = n % len(s)
    
    # count a in remainder
    a_in_remainder = s[:remainder].count('a')
    
    # add a x sets + remainder a's
    return a_per_set * sets + a_in_remainder
