from ticket import Ticket
from catalogue import Catalogue


class Caisse(object):
    
    def __init__(self, prix_file="test_data/prix.csv",
                        remises_file="test_data/remises.csv"):
        catalog = Catalogue(prix_file, remises_file)
        self.catalog_prix, self.catalog_remises = catalog.get_dicts()
        self.tickets = []


    def introduction_ticket(self,):
        print('\n* Début de saisie...')
        print("""
                Veuillez entrer les produits sous la forme:
                NomDuProduit  NombreDeKilo
                et taper fin pour terminer la saisie.
               """)

        end_saisie = False
        total_achat = 0
        i = 1
        ticket = Ticket()

        # Boucler sur l'introduction des articles
        while not end_saisie==True:
            saisie = input('Article n°{}: '.format(i))

            if 'fin' == saisie.lower():
                # Fin de saisie du ticket
                end_saisie = True

                # Affichage ticket
                print(ticket)

                # Sauvegarde du ticket
                self.tickets.append(ticket)
            else:
                saisie = saisie.split(',')

                try:

                    produit = saisie[0]
                    quantite = float(saisie[1])
                    prix = self.catalog_prix[produit]
                    
                    if produit in self.catalog_remises:
                        prix = self.appliquer_remises(produit, quantite, prix)
                    else:
                        ticket.ajout(produit, quantite, prix)

                except ValueError:
                    print("[ERREUR]: Quantité mal introduite!!")
                except IndexError:
                    print("[ERREUR]: Saisie erronée!")
                except KeyError:
                    print("[ERREUR]: Produit inconue!")

            i += 1


    def appliquer_remises(self, produit, quantite, prix):
        condition, cadreau = self.catalog_remises[produit]

        if quantite > condition:
            # Condition satisfaite
            part_1 = condition*prix 

            # Appliquer la reduction
            part_2 = ((quantite-condition) - cadeau)*prix
            return part_1 + (0 if part_2<0 else part2)

        else:
            # Condition non satisfaite
            return prix*quantite

