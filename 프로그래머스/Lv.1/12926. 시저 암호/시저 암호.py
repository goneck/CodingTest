def solution(s, n):
    answer=''
    for i in range(len(s)):
        if s[i]==" ":
            answer+=" "
            continue
        asciiChr=ord(s[i])+n
        if (s[i].isupper() and asciiChr>90) or (s[i].islower() and asciiChr>122):
            asciiChr-=26
        answer+=chr(asciiChr)
    return answer