class vehicule():
    def __init__(self, marque : str, nombre_de_porte : int):
        self.__marque = marque
        self.__nombre_de_porte = nombre_de_porte

    def __str__(self) -> str:
        return f"véhicule de marque {self.__marque} avec {self.__nombre_de_porte} portes."

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, marque : str):
        self.__marque = marque

    @property
    def nombre_de_porte(self):
        return self.__nombre_de_porte

    @nombre_de_porte.setter
    def nombre_de_porte(self, nombre_de_porte : int):
        self.__nombre_de_porte = nombre_de_porte

class voiture(vehicule):
    def __init__(self, modele : str, marque : str, nombre_de_porte : int):
        super().__init__(marque, nombre_de_porte)
        self.__modele = modele

    def __str__(self) -> str:
        return f"Voiture de modèle {self.__modele} de la marque {self.marque} avec {self.nombre_de_porte} portes."

if __name__ == "__main__":
    v1 = voiture("A4", "AUDI", 5)

    print(v1)
