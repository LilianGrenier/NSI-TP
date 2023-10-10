from Personne import Personne

class ListePersonnes:
    def __init__(self):
        self.__personnes = []

    def get_personnes(self):
        return self.__personnes

    def ajouter_personne(self, personne):
        self.__personnes.append(personne)

    def find_by_nom(self, s):
        for personne in self.__personnes:
            if personne.get_nom() == s:
                return personne
        return None

    def exists_code_postal(self, cp):
        for personne in self.__personnes:
            adresses = personne.get_adresses()
            for adresse in adresses:
                if adresse.get_code_postal() == cp:
                    return True
        return False

    def count_personne_ville(self, ville):
        count = 0
        for personne in self.__personnes:
            adresses = personne.get_adresses()
            for adresse in adresses:
                if adresse.get_ville() == ville:
                    count = count + 1
        return count

    def edit_personne_nom(self, old_nom, new_nom):
        for personne in self.__personnes:
            if personne.get_nom() == old_nom:
                personne._Personne__nom = new_nom

    def edit_personne_ville(self, nom, new_ville):
        for personne in self.__personnes:
            if personne.get_nom() == nom:
                adresses = personne.get_adresses()
                for adresse in adresses:
                    adresse._Adresse__ville = new_ville
