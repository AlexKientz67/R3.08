class Personnage():
    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbr_point_de_vie = nbr_point_de_vie
        self.__initiative = initiative

    def __str__(self) -> str:
        return f"le personnage {self.__pseudo} est niveau {self.__niveau} avec {self.__nbr_point_de_vie} point de vie et {self.__initiative} d'initiative"

    @property
    def get_pseudo(self) -> str:
        return self.__pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @property
    def initiative(self) -> int:
        return self.__initiative

    @property
    def nbr_point_de_vie(self):
        return self.__nbr_point_de_vie

    @nbr_point_de_vie.setter
    def nbr_point_de_vie(self, point : int):
        self.__nbr_point_de_vie = point

    def attaque(self, attaque: "Personnage") -> None:
        if self.initiative > attaque.initiative:
            attaque.nbr_point_de_vie -= self.degat()
            if attaque.nbr_point_de_vie > 0:
                self.nbr_point_de_vie -= attaque.degat()
        elif attaque.initiative < self.initiative:
            self.nbr_point_de_vie -= attaque.degat()
            if self.nbr_point_de_vie > 0:
                attaque.nbr_point_de_vie -= self.degat()
        else:
            self.nbr_point_de_vie -= attaque.degat()
            attaque.nbr_point_de_vie -= self.degat()

    def combat(self, attaque: "Personnage") -> None:
        while self.nbr_point_de_vie > 0 and attaque.nbr_point_de_vie > 0:
            self.attaque(attaque)

            print(f"{self.get_pseudo} : {self.nbr_point_de_vie} PV | {attaque.get_pseudo} : {attaque.nbr_point_de_vie} PV")

    def soigner(self, soigner : Personnage) -> None:
        soigner.nbr_point_de_vie = self.niveau


    def degat(self):
        return self.niveau

class Guerrier(Personnage):
    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1):
        super().__init__(pseudo, niveau, nbr_point_de_vie * 8 + 4, initiative * 4 + 6)

    def degat(self):
        return self.niveau * 2

class Mage(Personnage):
    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1,  mana : int = 0):
        super().__init__(pseudo, niveau, nbr_point_de_vie * 5 + 10, initiative * 6 + 4)
        self.__mana = niveau * 5

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, pmana : int):
        self.__mana = pmana

    def degat(self):
        if self.mana >= 4:
            self.mana -= 4
            return self.niveau + 3
        else:
            return self.niveau


def main():
    m1 = Mage("Mage1", mana=1)
    g1 = Guerrier("Guerrier1")
    p1 = Personnage("Personnage 1")

    m1.combat(g1)

if __name__ == "__main__":
    main()