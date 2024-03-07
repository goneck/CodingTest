def solution(brown, yellow):
    if yellow==1:
        return [3,3]
    for i in range(1, int(yellow/2)+1):
        if yellow%i!=0:
            continue
        print(i)
        if i*2+(yellow/i)*2+4==brown:
            return [(yellow/i)+2, i+2]