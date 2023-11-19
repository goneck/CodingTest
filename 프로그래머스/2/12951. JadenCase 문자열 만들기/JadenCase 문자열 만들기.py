def solution(s):
    s = s.split(" ")    
    for idx, item in enumerate(s):
        s[idx] = item[:1].upper() + item[1:].lower()    
    return ' '.join(s)