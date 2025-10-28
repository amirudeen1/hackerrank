def sockMerchant(n, ar):
    # creating a dictionary to count the occurence of each color
    color_counts = {}
    
    for sock_color in ar:
        if sock_color in color_counts:
            color_counts[sock_color] += 1
        else:
            color_counts[sock_color] = 1
    
    # to calculate total pairs
    total_pairs = 0
    for color, count in color_counts.items():
        pairs_of_this_color = count // 2
        total_pairs += pairs_of_this_color
    return total_pairs
