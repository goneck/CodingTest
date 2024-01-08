def solution(s):
    even=True
    s=list(s)
    for i in range(len(s)):
        if s[i]==" ":
            even=True
            continue
        if even:
            s[i]=s[i].upper()
        else:
            s[i]=s[i].lower()
        even=not even
    return ''.join(s)