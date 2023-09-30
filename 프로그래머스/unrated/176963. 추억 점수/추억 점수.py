def solution(name, yearning, photo):
    answer = []
    for idx1, item1 in enumerate(photo):
        score=0
        for idx2, item2 in enumerate(name):
            if item2 in item1:
                score+=yearning[idx2]
        answer.append(score)
    
    return answer