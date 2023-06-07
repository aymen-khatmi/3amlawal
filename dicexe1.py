def ch():
    c=input("enter une chaine de caractere")
    d=dict((i,c.count(i)) for i in c)
    
    return d
        
    
def ch2():
    c=input("enter une chaine de caractere")
    d={}
    for i in c:
        d[i]=c.count(i)
    return d
