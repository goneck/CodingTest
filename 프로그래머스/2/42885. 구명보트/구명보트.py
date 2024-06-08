def solution(people, limit):
    people = sorted(people)
    start=0
    end=len(people)-1
    answer=0
    
    while(start<=end):
        if start==end:
            answer+=1
            end-=1
            continue
        if people[start]+people[end] <= limit:
            start+=1
            end-=1
        else:
            end-=1
        answer+=1
    return answer