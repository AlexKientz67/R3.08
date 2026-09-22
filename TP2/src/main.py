class Personnage():
    """
    Classe personnage qui permet de créer un personnage

    :param pseudo: personnage pseudo
    :param niveau: personnage niveau
    :param nbr_point_de_vie: personnage nbr_point_de_vie
    :param initiative: personnage initiative
    """
    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1):
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit etre de type str")

        if not isinstance(niveau, int):
            raise TypeError("Le niveau doit etre de type int")

        if not isinstance(nbr_point_de_vie, int):
            raise TypeError("Le nbr_point_de_vie doit etre de type int")

        if not isinstance(initiative, int):
            raise TypeError("Le initiative doit etre de type int")

        if niveau < 0:
            raise ValueError("Le niveau doit etre supperieur a 0")

        if nbr_point_de_vie < 0:
            raise ValueError("Le nbr_point_de_vie doit etre supperieur a 0")

        if initiative < 0:
            raise ValueError("Le initiative doit etre supperieur a 0")

        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbr_point_de_vie = nbr_point_de_vie
        self.__initiative = initiative

    def __str__(self) -> str:
        return f"le personnage {self.__pseudo} est niveau {self.__niveau} avec {self.__nbr_point_de_vie} point de vie et {self.__initiative} d'initiative"

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    def __eq__(self, autre : Personnage):
        return self.pseudo == autre.pseudo

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

        """
        Définir les points de vies du personnage
        :param point: point de vie
        """

        if not isinstance(point, int):
            raise TypeError("Le point doit etre de type int")

        self.__nbr_point_de_vie = point

    def attaque(self, attaque: Personnage) -> None:

        """
        Permet d'attaquer un joueur
        :param attaque: personnage
        """

        if not isinstance(attaque, Personnage):
            raise TypeError("Le pseudo doit etre de type Personnage")

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

    def combat(self, attaque: Personnage) -> None:
        """
        Cette fonction permet de lancer un combat
        :param attaque: personnage
        """


        if not isinstance(attaque, Personnage):
            raise TypeError("Le attaquant doit etre de type Personnage")

        while self.nbr_point_de_vie > 0 and attaque.nbr_point_de_vie > 0:
            self.attaque(attaque)

            print(f"{self.pseudo} : {self.nbr_point_de_vie} PV | {attaque.pseudo} : {attaque.nbr_point_de_vie} PV")

    def soigner(self, soigner : Personnage) -> None:
        """
        Cette fonction permet de lancer un soigner
        :param soigner: personnage
        """
        if not isinstance(soigner, Personnage):
            raise TypeError("Le soigner doit etre de type Personnage")
        soigner.nbr_point_de_vie = self.niveau


    def degat(self):
        return self.niveau

class Guerrier(Personnage):
    """
    Cette classe permet de créer un guerrier qui est hérité de Personnage
    """


    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1):
        super().__init__(pseudo, niveau, nbr_point_de_vie * 8 + 4, initiative * 4 + 6)

    def degat(self):
        return self.niveau * 2

class Mage(Personnage):
    """
    Cette classe permet de créer un mage qui est hérité de personnage
    """

    def __init__(self, pseudo : str, niveau : int = 1, nbr_point_de_vie : int = 1, initiative : int = 1,  mana : int = 0):
        super().__init__(pseudo, niveau, nbr_point_de_vie * 5 + 10, initiative * 6 + 4)
        self.__mana = niveau * 5

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, pmana : int):

        if not isinstance(pmana, int):
            raise TypeError("Le mana doit etre de type int")

        self.__mana = pmana

    def degat(self):
        if self.mana >= 4:
            self.mana -= 4
            return self.niveau + 3
        else:
            return self.niveau
class Joueur:
    def __init__(self, nom: str, maximum: int):

        if not isinstance(nom, str):
            raise TypeError("Le nom doit etre de type str")

        if not isinstance(maximum, int):
            raise TypeError("Le maximum doit etre de type int")

        self.__nom = nom
        self.__maximum = maximum
        self.__personnages = []

    def ajouter(self, personnage: Personnage) -> None:

        if not isinstance(personnage, Personnage):
            raise TypeError("Le personnage doit etre de type Personnage")

        if len(self.__personnages) < self.__maximum:
            self.__personnages.append(personnage)

    @property
    def nom(self):
        return self.__nom

    def numero_personnage(self, numero : int) -> Personnage:

        if not isinstance(numero, int):
            raise TypeError("Le numero doit etre de type int")

        return self.__personnages[numero]

    def pseudo_personnage(self, pseudo : str) -> Personnage:

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit etre de type str")

        i = 0
        while i != len(self.__personnages):
            if self.__personnages[i].pseudo == pseudo:
                return self.__personnages[i]
            i += 1
        return None

    def eq_personnage(self, personnage : Personnage) -> Personnage:

        if not isinstance(personnage, Personnage):
            raise TypeError("Le personnage doit etre de type Personnage")

        for p in self.__personnages:
            if p == personnage:
                return p
        return None

    def rm_numero_personnage(self, numero : int) -> None:

        if not isinstance(numero, int):
            raise TypeError("Le numero doit etre de type int")

        del self.__personnages[numero]

    def rm_pseudo_personnage(self, pseudo : str) -> None:

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit etre de type str")

        i = 0
        while i != len(self.__personnages):
            if self.__personnages[i].pseudo == pseudo:
                del self.__personnages[i]
            i += 1

    def rm_personnage_personnage(self, personnage : Personnage) -> None:

        if not isinstance(personnage, Personnage):
            raise TypeError("Le personnage doit etre de type Personnage")

        self.__personnages.remove(personnage)

def main():
    m1 = Mage("Mage1", mana=1)
    g1 = Guerrier("Guerrier1")
    p1 = Personnage("Personnage 1")

    j1 = Joueur("louis", 5)
    j1.ajouter(g1)
    j1.ajouter(m1)

    j1.rm_personnage_personnage(m1)

if __name__ == "__main__":
    main()