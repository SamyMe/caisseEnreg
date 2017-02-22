from caisse import Caisse

if __name__=="__main__":

    caisse = Caisse()
    actions = { '1': caisse.introduction_ticket,
                '2': caisse.maj
                }

    print("""
 *** Bienvenue dans le système de gestion de caisse. *** """)

    menu = """
    ----------------- MENU --------------------
    1: Calculer total d'un cady
    2: Mettre à jour les fichiers de catalogue 
    3: sortire du programme
    -------------------------------------------
    """

    prog_active = True
    while(prog_active == True):
        print(menu)
        choix = input(' choix:')
        if choix == '3':
            prog_active = False
        elif choix not in actions.keys():
            print("[ERREUR] choix erroné!")
        else:
            actions[choix]()

