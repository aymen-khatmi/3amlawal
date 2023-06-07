class rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def primetre(self):
        return 2*(self.longueur+self.largeur)
    def surface(self):
        return self.longueur*self.largeur


class fille(rectangle):
    def __init__(self,longueur,largeur,hauteur):
        rectangle.__init__(self,longueur,largeur)
        self.hauteur=hauteur
    def volume(self):
        return self.longueur*self.largeur*self.hauteur
        
    
