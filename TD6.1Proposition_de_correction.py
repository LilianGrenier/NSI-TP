# Classe Arbre
class Arbre():
    # constructeur de l'arbre:
    def __init__(self, valeur):
       self.label = valeur
       self.G = None
       self.D = None

    # setters 
    def set_label(self, label):
        self.label = label
    def set_G(self ,greffe):
        self.G = greffe
    def set_D(self, greffe):
        self.D = greffe

    # test si l'arbre est une feuille ou non
    def est_une_feuille(self):
        return not self.G and not self.D

    # getters
    def get_label(self):
        return self.label
    def get_G(self):
        return self.G
    def get_D(self):
        return self.D



def affichageBST(arbre: Arbre):
    if arbre != None:
        return (arbre.get_label(), affichageBST(arbre.get_G()), affichageBST(arbre.get_D()))

# Exercice 1

# a.

def isaBST(arbre: Arbre):
    if isinstance(arbre.G, Arbre) and (arbre.G.label > arbre.label or not isaBST(arbre.G)): return False
    if isinstance(arbre.D, Arbre) and (arbre.D.label <= arbre.label or not isaBST(arbre.D)): return False
    return True

# b.

def smallestElementBST(arbre: Arbre):
    if arbre.G: return smallestElementBST(arbre.G)
    return arbre.label

# c.

def greatestElementBST(arbre: Arbre):
    if arbre.D: return smallestElementBST(arbre.D)
    return arbre.label

# d.

def existElementBST(valeur: int, arbre: Arbre):
    if arbre.label == valeur: return True
    if valeur <= arbre.label and arbre.G: return existElementBST(valeur, arbre.G)
    if arbre.D: return existElementBST(valeur, arbre.D)
    return False
# e.

def insertElementBST(valeur: int, arbre: Arbre):
    if valeur <= arbre.label:
        if arbre.G: insertElementBST(valeur, arbre.G)
        else: arbre.set_G(Arbre(valeur))
    elif valeur > arbre.label:
        if arbre.D: insertElementBST(valeur, arbre.D)
        else: arbre.set_D(Arbre(valeur))
# .

def getElementsBST(arbre: Arbre):
    valeurs = [arbre.label]
    if arbre.G:
        valeurs += getElementsBST(arbre.G)
    if arbre.D:
        valeurs += getElementsBST(arbre.D)
    return valeurs
# h.

def removeElementBST(valeur: int, arbre: Arbre):
    if valeur <= arbre.label and arbre.G:
        if valeur == arbre.G.label:
            copy = arbre.G
            arbre.set_G(None)
            for v in getElementsBST(copy)[1:]: insertElementBST(v, arbre)
        else: removeElementBST(valeur, arbre.G)
    if valeur > arbre.label and arbre.D:
        if valeur == arbre.D.label:
            copy = arbre.D
            arbre.set_D(None)
            for v in getElementsBST(copy)[1:]: insertElementBST(v, arbre)
        else: removeElementBST(valeur, arbre.D)


# Exercice 2
#1) voir le google Docs

#2)
E = Arbre('+')
E.set_G(Arbre('*'))
E.set_D(Arbre('-'))
E.G.set_G(Arbre('12'))
E.G.set_D(Arbre('9'))
E.D.set_G(Arbre('8'))
E.D.set_D(Arbre('5'))



# 3) Cas du parcours en profondeur d'abord Infixe
def affichageArithm(arbre: Arbre):
    string = ''
    if arbre.G:
        if arbre.G.est_une_feuille(): string += affichageArithm(arbre.G) + ' '
        else: string += '(' + affichageArithm(arbre.G) + ') '
    string += arbre.label
    if arbre.D:
        if arbre.D.est_une_feuille(): string += ' ' + affichageArithm(arbre.D)
        else: string += ' (' + affichageArithm(arbre.D) + ')'
    return string



# Exercice 3
# Cas d'un parcours en profondeur d'abord préfixe : la racine est vsité avant les fils gauches puis fils droit
def affichageSyntax(arbre: Arbre):
    racine = arbre.label
    #affichage de l'arbre gauche
    if arbre.G: racine += affichageSyntax(arbre.G)
    #affichage de l'arbre droit
    if arbre.D: racine += affichageSyntax(arbre.D)
    return racine
