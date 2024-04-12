from collections import deque
def solution(progresses, speeds):
    answers=[]
    progresses=deque(progresses)
    speeds=deque(speeds)
    while(len(progresses)>0):
        cnt=0
        while(True):
            if len(progresses)<=0:
                break
            if progresses[0]>=100:
                progresses.popleft()
                speeds.popleft()
                cnt+=1
                if len(speeds)==0:
                    answers.append(cnt)
                    break;
                continue
            else:
                if cnt>0: 
                    answers.append(cnt)
                break
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
    return answers
        