from caisse import Caisse

if __name__=="__main__":
    print("Lancement de la caisse:")
    caisse = Caisse()

    actions = { 1: caisse.introduction_ticket,
                2: caisse.maj
                }


    print("""
    Bienvenue dans le système de gestion de caisse.
    Choix:""")

    menu = """
    ------------------------------------------
    1: Calculer total d'un cady
    2: Mettre à jour les fichiers de catalogue 
    3: sortire du programme
    ------------------------------------------
    """

    prog_active = True
    while(prog_active = True)
        choix = input(menu)
        if choix == 3:
            prog_active = False
        elif choix not in actions:
            print("Usage: python run_tests.py [caisse|ticket|catalogue]")
        else:
            actions[choix]()

