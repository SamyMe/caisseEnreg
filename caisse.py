from ticket import Ticket
from catalogue import Catalogue


class Caisse(object):
    
    def __init__(self, prix_file="test_data/prix.csv",
                        remises_file="test_data/remises.csv"):

        self.catalog_manager = Catalogue(prix_file, remises_file)
        self.catalog_prix, self.catalog_remises = self.catalog_manager.get_dicts()
        self.tickets = []


    def introduction_ticket(self,):
        """
            Lecture du contenue du cady.
            La saisie se fait via clavier. 
        """
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
                    # Traitement de la saisie
                    produit = saisie[0]
                    quantite = float(saisie[1])
                    prix_u = self.catalog_prix[produit]
                    
                    if produit in self.catalog_remises:
                        remise, justification = self.appliquer_remises(produit, 
                                                                            quantite, prix_u)
                        ticket.ajout(produit, 
                                quantite, prix_u, 
                                remise, justification)
                    else:
                        ticket.ajout(produit, quantite, prix_u)

                except ValueError:
                    print("[ERREUR]: Quantité mal introduite!!")
                except IndexError:
                    print("[ERREUR]: Saisie erronée!")
                except KeyError:
                    print("[ERREUR]: Produit inconue!")

            i += 1


    def appliquer_remises(self, produit, quantite, prix_u):
        """
            Calcule de la remise sur un produit donné
         
            :type produit: string
            :param produit: nom du produit

            :type quantite: float 
            :param quantite: quantité acheté de produit

            :type prix_u: float 
            :param data: prix unitaire de produit   
        """

        condition, cadeau = self.catalog_remises[produit]
        prix_total = prix_u*quantite
        remise = 0
        justification = ''
        
        # Calculer nombre de remise appliquable
        remise = (quantite//(cadeau+condition))*cadeau*prix_u
        reste = quantite%(cadeau+condition) - condition
        remise += reste*prix_u if reste>0 else 0

        justification = "{} acheté(s), {} offert".format(condition, cadeau)

        return -remise, justification


    def maj(self):
        """
            Mise a jour des donnée de la caisse.
        """

        self.catalog_prix, self.catalog_remises = self.catalog_manager.maj()


