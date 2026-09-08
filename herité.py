class vehicule():
    def __init__(self, nombre_de_porte):
        self.nombre_de_porte = nombre_de_porte

class voiture(vehicule):
    def __init__(self, nom, marque, nombre_de_porte):
        super().__init__(nombre_de_porte)
        self.nom = nom
        self.marque = marque

    def __str__(self):
        return f"nom : {self.nom}, marque : {self.marque}, nombre : {self.nombre_de_porte}"


clio = voiture("clio", "renault", 5)

print(clio)