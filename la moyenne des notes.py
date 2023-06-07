n1=float(input("entrer le note 1:"))
n2=float(input("entrer le note 2:"))
n3=float(input("entrer le note 3:"))
n4=float(input("entrer le note 4:"))
n5=float(input("entrer le note 5:"))
somme=n1+n2+n3+n4+n5
m=somme/5
if m>=10 :
    print("Valide")
elif m<=10 and m>=6:
    print("ratt")
else:
    print("F")
        

print(f"la somme est {somme} et la moyenne des notes est {m}")
