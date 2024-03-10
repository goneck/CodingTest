import math

def solution(n, words):
    order=0
    wordList=dict()
    for idx, item in enumerate(words):
        if idx>0 and words[idx-1][len(words[idx-1])-1] != item[0]:
            order = idx
            break
        if item in wordList:
            order = idx
            break
        else:
            wordList[item]=1
        if idx==len(words)-1:
            return [0, 0]
    turn=0
    order+=1
    if order%n ==0:
        turn=n
    else:
        turn=order%n
    return [turn, math.ceil(order/n)]