def f1 (a : int, b : int) -> int:
    """"
    Fonction qui retourne la valeur la plus grande entre a et b
    """
    if a > b:
        return a
    elif b > a:
        return b

def f2 (valeur : int, seuil : int) -> int:
    """
    Fonction qui retourne 1 si la valeur depasse le seuil
    """
    if valeur > seuil:
        return 1
    elif valeur < seuil:
        return 0

def f3 (liste : int) -> int:
    """
    Fonction qui retourne la valeur la plus grande d'une liste
    """
    return max(liste)

def f4 (liste : int, seuil : int) -> int:
    """
    Fonction qui retourne le nombre de valeur suppérieur au seuil dans une liste
    """
    nbr = 0
    i = 0
    while i != len(liste):
        if liste[i] > seuil:
            nbr += 1
        i = i + 1
    return nbr

def f5 (dictionnaire : str, phrase : str):
    """
    Fonction qui retourne le contenue de la liste avec une phrase avant.
    """
    print(phrase)
    i = 0
    while i != len(dictionnaire):
        print(dictionnaire[i])
        i = i + 1

chaine = ["coucou", "cou", "couc"]
f5(chaine, "Contenue de la liste :")