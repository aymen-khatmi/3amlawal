class votrcompt:
    def __init__(self,num,nom,solde):
        self.num=num
        self.nom=nom
        self.solde=solde
    def verser(self,montant):
        self.solde += montant
    def retrait(self,montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant.")
    def affichage(self):
        print("Numéro de compte : ", self.num)
        print("Nom du titulaire : ", self.nom)
        print("Solde : ", self.solde)
