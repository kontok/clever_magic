def delete(chars, s):
    s=str(s)
    for i in chars:
        if s.find(i):
            s = ''.join(s.split(i))
    return s
def is_palindrom(s):
        p=True
        s = delete(' !?,.\'"', s)
        print(s)
        a=0
        b=len(s)-1
        while a<b:
            if s[a] != s[b]:
                    p=False
            a +=1
            b -=1
        print (p)
is_palindrom()
