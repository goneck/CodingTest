def solution(X, Y):
    # X=sorted(X)
    # Y=sorted(Y)
    # xnums=dict()
    # ynums=dict()
    # for i in range(10):
    #     cnt=X.count(str(i))
    #     xnums[i]=cnt
    #     X=X[cnt:]
    # for i in range(10):
    #     cnt=Y.count(str(i))
    #     ynums[i]=cnt
    #     Y=Y[cnt:]
    # answer=""
    # for i in range(9, -1, -1):
    #     if xnums[i]==0 or ynums[i]==0:
    #         continue
    #     answer+=str(i)*min(xnums[i], ynums[i])
    # if answer=="":
    #     return "-1"
    # elif int(answer)==0:
    #     return "0"
    # else:
    #     return answer
    answer=""
    for i in range(9, -1, -1):
        answer+=str(i)*min(X.count(str(i)), Y.count(str(i)))
    
    if answer=="":
        return "-1"
    
    if len(answer) == answer.count("0"):
        return "0"
    
    return answer
        
        
        
        