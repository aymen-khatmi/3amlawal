livre=dict()

test=True
while test:
    titre=input("enter le nom de livre:")
    auteur=input("enter le nom de auteur:")
    nb=int(input("enter le le nombre d’exemplaires:"))
    livre[titre]=(auteur,nb)
    cont=input(" 'y' to continue and 'n' to stop:")
    if cont == 'n':
        test=False
print(livre)

#----------------------question 2-----------------------
nom=input("enter le titre de livre pour afficher:")
if nom in livre:
    print("auteur :",livre[nom][0])
    print("nombre d’exemplaires:",livre[nom][1])
print('')
#----------------------question 3-----------------
print("l’ensemble des auteurs de la base")
for i in livre:
    print("l'auteurs",livre[i][0])
print('')

#-----------------------question 4 -----------------

for i in livre:
    if livre[i][1] > 0:
        print(f"le livre {i} est empruntables ")
print('')

#-----------------------question 5-------------------
nom_auteur=input("enter un nome d’un auteur pour chercher:")
for titre in livre:
    if nom_auteur == livre[titre][0]:
        print(f"le livres {titre} écrit par {nom_auteur}")



