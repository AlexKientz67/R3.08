def affiche(texte):
    """
    Affiche une chaîne de caractères précédée de 'texte à afficher :'.

    :param texte: La chaîne de caractères à afficher.
    """
    print("texte à afficher :", texte)


class Velo:
    """
    Représente un vélo.

    Un vélo est défini par sa marque, sa taille de pneu,
    sa couleur et son nombre de vitesses.
    """

    def __init__(self, marque, taille_pneu, couleur, nombre_vitesses):
        """
        Initialise un vélo.

        :param marque: Marque du vélo.
        :param taille_pneu: Taille des pneus en pouces.
        :param couleur: Couleur du vélo.
        :param nombre_vitesses: Nombre maximal de vitesses.
        """
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nombre_vitesses = nombre_vitesses
        self.vitesse_courante = 1

    def gear_up(self):
        """
        Augmente la vitesse courante de 1.

        La vitesse ne peut pas dépasser le nombre maximal
        de vitesses du vélo.

        :return: La nouvelle vitesse courante.
        """
        if self.vitesse_courante < self.nombre_vitesses:
            self.vitesse_courante += 1

        return self.vitesse_courante

    def gear_down(self):
        """
        Diminue la vitesse courante de 1.

        La vitesse ne peut pas être inférieure à 1.

        :return: La nouvelle vitesse courante.
        """
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1

        return self.vitesse_courante


def main():
    """
    Fonction principale du programme.

    Crée une chaîne de caractères, l'affiche avec la fonction
    affiche(), puis crée un vélo et utilise ses changements
    de vitesse.
    """

    # (1) Définition d'une chaîne de caractères
    str1 = "Bonjour, ceci est un test."

    # (2) Appel de la fonction affiche
    affiche(str1)

    # (3) Création d'une instance de Vélo
    v1 = Velo("Decathlon", 26, "bleu", 18)

    # (4) Utilisation des méthodes gear_up et gear_down
    print("Vitesse après gear_up :", v1.gear_up())
    print("Vitesse après gear_up :", v1.gear_up())
    print("Vitesse après gear_down :", v1.gear_down())


if __name__ == "__main__":
    main()