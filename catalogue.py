

class Catalogue(object):
    def __init__(self, prix_file, remises_file):
        self.prix_file = prix_file
        self.remises_file = remises_file

        self.prix = {}
        self.remises = {}

        self._lire_prix()
        self._lire_remises()


    def get_dicts(self):
        """
             Retourne les catalogues de prix et remises
        """
        return self.prix, self.remises


    def _lire_prix(self,):
        """
            Lecture du fichier contenant les produits.
            Le fichier est donné en argument lors de la 
            creation de l'instance du Catalogue. 
        """

        with open(self.prix_file, 'r') as cat_file:
            produit = ''
            prix = ''
            for row in cat_file.readlines():
                try:
                    produit, prix = row.rstrip().split(',')
                    # Pour faciliter la comparaison
                    produit = produit.lower()

                    if produit in self.prix: 
                        # Produit dupliqué
                        raise KeyError
                    else:
                        # Introduire au catalogue
                        self.prix[produit] = float(prix)

                except ValueError:
                    print("[ERREUR CATALOGUE]: Erreure de format dans: {}".format(row))
                except KeyError:
                    print("[ERREUR CATALOGUE]: Produit '{}' dupliqué!".format(produit))


    def _lire_remises(self,):
        """ 
            Lecture du fichier contenant les remises.
            Le fichier est donné en argument lors de la 
            creation de l'instance du Catalogue. 
        """

        with open(self.remises_file, 'r') as cat_file:
            produit = ''
            prix = ''
            for row in cat_file.readlines():
                try:
                    produit, condition, cadeau= row.rstrip().split(',')
                    # Pour faciliter la comparaison
                    produit = produit.lower()

                    if produit in self.remises: 
                        # Produit dupliqué
                        raise KeyError
                    else:
                        # Introduire au catalogue
                        self.remises[produit] = (float(condition), float(cadeau))

                except ValueError:
                    print("[ERREUR CATALOGUE]: Erreure de format dans: {}".format(row))
                except KeyError:
                    print("[ERREUR CATALOGUE]: Produit '{}' dupliqué!".format(produit))


    def maj(self, prix_file=None, remises_file=None):
        """
            Mise a jour du catalogue.
            Relire les fichiers defin par les parametres
            ou stoqués dans: self.prix_file et self.remises_file 

            :type prix_file: string
            :param produit: chemain vers fichier prix

            :type remise_file: string
            :param produit: chemain vers fichier remise
        """
        if prix_file:
            self.prix_file = prix_file
        if remises_file:
            self.remises_file = remises_file

        self.prix = {}
        self.remises = {}

        # Lecture des fichiers
        self._lire_prix()
        self._lire_remises()
        return self.prix, self.remises
