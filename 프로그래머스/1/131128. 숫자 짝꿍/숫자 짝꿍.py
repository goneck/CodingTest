from collections import Counter
def solution(X, Y):
    xnums=Counter(list(X))
    ynums=Counter(list(Y))
    
    answer=""
    
    for i in range(9, -1, -1):
        answer+=str(i)*min(xnums[str(i)], ynums[str(i)])
        
    if answer=="":
        return "-1"
    if len(answer)==answer.count("0"):
        return "0"
    return answer
        
        
        