def solution(s):
    # answer=''
    # s=list(s.split(" "))
    # for item in s:
    #     item=item[0].upper()+item[1:].lower()
    #     answer+=item+' '
    # return answer[:-1]
    answer = ''
    words = s.split(" ")    
    for idx, word in enumerate(words):
        words[idx] = word[:1].upper() + word[1:].lower()
        # words[idx] = word[0].upper() + word[1:].lower()        
    return ' '.join(words)