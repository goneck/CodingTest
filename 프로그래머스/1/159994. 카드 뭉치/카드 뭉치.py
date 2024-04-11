from collections import deque
def solution(cards1, cards2, goal):
    cards1=deque(cards1)
    cards2=deque(cards2)
    for i in range(len(goal)):
        if len(cards1)>0 and cards1[0]==goal[i]:
            cards1.popleft()
        elif len(cards2)>0 and cards2[0]==goal[i]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"
            
        