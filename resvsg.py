class vt:
    def __init__(self,num,nom,solde):
        self.num=num
        self.nom=nom
        self.solde=solde
    def verser(self,montant):
        self.solde+=montant
    def retrait(self,montant):
        if montant > self.solde:
            print("ta mrid")
        else:
            self.solde-=montant
    def afficher(self):
        print("votre solde est :",self.solde)
        print("numero de compte est :",self.num)
        print("votre nom est :",self.nom)
