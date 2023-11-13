def solution(sizes):
    sizes.sort(reverse=True, key=lambda x:x[0])
    max_w=sizes[0][0]
    sizes.sort(reverse=True, key=lambda x:x[1])
    for item in sizes:
        if item[1]>item[0]:
            if item[1]>max_w:
                max_w =item[1] 
            item[0], item[1]= item[1], item[0]
    sizes.sort(reverse=True, key=lambda x:x[1])
    return max_w*sizes[0][1]