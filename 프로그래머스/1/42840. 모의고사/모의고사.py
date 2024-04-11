def solution(answers):
    patterns=[[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score=[0,0,0]
    for idx, a in enumerate(answers):
        for pidx, p in enumerate(patterns):
            if a==p[idx%len(p)]:
                score[pidx]+=1
                
    answer=[]
    for i in range(len(score)):
        if score[i]==max(score):
            answer.append(i+1)
    return answer
    
    
                