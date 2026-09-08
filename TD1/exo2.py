class Tasse:
    matiere: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return f"la tasse de matiere {self.matiere}, de couleur {self.couleur}, de marque {self.marque} a une contenance de {self.contenance}ml"

    def remplir(self, contenue):
        self.contenue = contenue

    def vider(self):
        del self.contenue


tasse = Tasse("blanche", 250, "IKEA")

tasse.remplir("café")

print(tasse.contenue)

print(tasse)