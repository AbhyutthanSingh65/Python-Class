def cal(x,a,b):
    h=0
    m=0
    while h<=x:
        h+=a
        m+=1
        if h>=x:
            return m
        h-=b
        m+=1
    return m
print(cal(30,10,5))

