def solution(s):
    answer = []
    for idx, item in enumerate(s):
        for i in range(idx-1, -1, -1):
            if s[i]==item:
                answer.append(idx-i)
                break
        if len(answer)<=idx:
            answer.append(-1)
    return answer