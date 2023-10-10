from Adresse import Adresse

class Personne:
    def __init__(self, nom, sexe):
        self.__nom = nom
        self.__sexe = sexe
        self.__adresses = []

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def get_sexe(self):
        return self.__sexe
    
    def set_sexe(self, sexe):
        self.__sexe = sexe

    def get_adresses(self):
        return self.__adresses
    
    def set_adresses(self, adresses):
        self.__adresses = adresses

    def ajouter_adresse(self, adresse):
        self.__adresses.append(adresse)
