def bonjour(texte : str) -> None:
    '''
    fonction permettant de dire bonjour \'a une a personne dont le nom est pass\'e en argument
    '''
    print("Texte a afficher : ", texte)



if __name__ == "__main__":
    bonjour("bonjour d\'apple ")
    print(f" documentation fonction bonjour { bonjour . __doc__ } " )