from collections import Counter
def solution(X, Y):
    xnums=Counter(list(X))
    ynums=Counter(list(Y))
    # for i in range(10):
    #     xnums[i]=X.count(str(i))
    # for i in range(10):
    #     ynums[i]=Y.count(str(i))
    answer=""
    for i in range(9, -1, -1):
        answer+=str(i)*min(xnums[str(i)], ynums[str(i)])
    if answer=="":
        return "-1"
    elif len(answer)==answer.count("0"):
        return "0"
    else:
        return answer
#     answer=""
#     for i in range(9, -1, -1):
#         answer+=str(i)*min(X.count(str(i)), Y.count(str(i)))
    
#     if answer=="":
#         return "-1"
    
#     if len(answer) == answer.count("0"):
#         return "0"
    
#     return answer
        
        
        
        