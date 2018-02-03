def delete(chars, s):
    s=(str(s))
    s=s.lower()
    for i in chars:
        if s.find(i):
            s = ''.join(s.split(i))
    return s
def is_palindrome(s):
        p=True
        s = delete(' !?,.\'"', s)
        a=0
        b=len(s)-1
        while a<b:
            if s[a] != s[b]:
                    p=False
            a +=1
            b -=1
        return (p)

