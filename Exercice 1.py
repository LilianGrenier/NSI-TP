class Film:
    def __init__(self,titre,réalisateur):
        self.titre = titre
        self.réalisateur = réalisateur
    
    def get_titre(self):
        return self.titre
    
    def set_titre(self,titre):
        self.titre = titre
        
    def get_réalisateur(self):
        return self.réalisateur
    
    def set_réalisateur(self,réalisateur):
        self.réalisateur = réalisateur
        
class Personne:
    def __init__(self,nom,année_naissance,lieu_naissance):
        self.nom = nom
        self.année_naissance = année_naissance
        self.lieu_naissance = lieu_naissance
        
    def get_nom(self):
        return self.nom
    
    def set_nom(self,nom):
        self.nom = nom
        
    def get_année_naissance(self):
        return self.année_naissance
    
    def set_année_naissance(self,année_naissance):
        self.année_naissance = année_naissance
        
    def get_lieu_naissance(self):
        return self.lieu_naissance
    
    def set_lieu_naissance(self,lieu_naissance):
        self.lieu_naissance = lieu_naissance
        
film = Film("interstellar","Christopher Nolan")

acteur = Personne("Matthew McConaughey",1969,"États-Unis")

réalisateur = Personne("Christopher Nolan",1970,"Royaume-Uni")

print(réalisateur.get_année_naissance())