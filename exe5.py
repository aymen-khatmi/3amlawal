def pair_impair(nb):
    pair=[]
    impair=[]

    for nombre in nb:
        if nombre % 2 == 0:
            pair.append(nombre)
        else:
            impair.append(nombre)
    
    return pair,impair
        
