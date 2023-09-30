def solution(today, terms, privacies):
    answer = []
    today=(int(today[0:4])-2000)*28*12+int(today[5:7])*28+int(today[8:10])
    termsDict=dict()
    for item in terms:
        k, v = map(str, item.split())
        termsDict[k] = int(v)
    
    for idx, privacy in enumerate(privacies):
        if (int(privacy[0:4])-2000)*28*12+int(privacy[5:7])*28+int(privacy[8:10])+termsDict[privacy[-1]]*28<=today:
            answer.append(idx+1)
    return answer