def solution(n, m, section):
    answer = 0
    if(m==1 or n==1):
        return len(section)
    nowSection=1
    while(nowSection<=section[-1]):
        if(nowSection not in section):
            nowSection+=1
        else:
            nowSection+=m
            answer+=1
    return answer