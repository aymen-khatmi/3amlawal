
classe={}
tup=tuple()
def etudiants():
    n=int(input("donner le nombre des etudiants:"))
    for etudiant in range(1,n+1):
        nom=input("donner le nom:")
        age=int(input("enter l'age:"))
        moyenne=float(input("enter la moyenne:"))
        tup=(age,moyenne)
        classe[nom]=tup
    for i in classe.items():
        print(i)
    
def affichage():
    choice=input("donner le nom pour afficher:")
    if choice in classe:
        print(f"nom:{choice} age:{classe[choice][0]} moyenne:{classe[choice][1]}")
    else:
        print("Étudiant non reconnu")

def affichage_co():
    counter=0
    for i in classe:
        if classe[i][0] <= 20 and classe[i][1] >= 10:
            counter+=1
            print(f"nom:{i} age:{classe[i][0]} moyenne:{classe[i][1]}")
    return counter

            
            
