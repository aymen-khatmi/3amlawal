def power():
    n=int(input("enter un nombre"))
    d={}
    if n == 0:
        return {1:1}
    for i in range(1,int(n)+1):
        d[i]=fac(i)
    return d


def fac(i):
    f=1
    for nombre in range(1,i+1):
        f*=nombre
    return f



