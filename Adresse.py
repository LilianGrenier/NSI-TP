class Adresse:
    def __init__(self, rue, ville, code_postal):
        self.__rue = rue
        self.__ville = ville
        self.__code_postal = code_postal

    def get_rue(self):
        return self.__rue
    
    def set_rue(self, rue):
        self.__rue = rue

    def get_ville(self):
        return self.__ville
    
    def set_ville(self, ville):
        self.__ville = ville

    def get_code_postal(self):
        return self.__code_postal
    
    def set_code_postal(self, code_postal):
        self.__code_postal = code_postal
