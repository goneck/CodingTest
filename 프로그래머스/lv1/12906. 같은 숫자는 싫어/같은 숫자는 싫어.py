def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        if len(answer)==1:
            continue
        if answer[len(answer)-1]==answer[len(answer)-2]:
            answer.pop()
    return answer