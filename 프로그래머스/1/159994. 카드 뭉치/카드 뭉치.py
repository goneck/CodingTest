from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1=deque(cards1)
    cards2=deque(cards2)
    for i in range(len(goal)):
        if len(cards1)>0 and cards1[0]==goal[i]:
            answer+=cards1.popleft()
            continue
        if len(cards2)>0 and cards2[0]==goal[i]:
            answer+=cards2.popleft()
            continue
    if answer!=''.join(goal):
        return "No"
    else:
        return "Yes"
            
        