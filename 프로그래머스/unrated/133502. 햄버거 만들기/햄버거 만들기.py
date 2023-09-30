def solution(ingredient):
    answer = 0
    hamstack=[]
    for item in ingredient:
        hamstack.append(item)
        if len(hamstack)>3 and hamstack[-4:]==[1,2,3,1]:
            for i in range(4):
                hamstack.pop()
            answer+=1
    return answer