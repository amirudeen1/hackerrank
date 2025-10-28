def rotLeft(a, d):
    # handle case when d > len(a)
    d = d % len(a)
    return a[d:] + a[:d]
