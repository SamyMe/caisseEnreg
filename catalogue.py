

class Catalogue(object):
    def __init__(self, prix_file, remises_file):
        self.prix_file = prix_file
        self.remises_file = remises_file

        self.prix = {}
        self.remises = {}

        self._lire_prix()
        self._lire_remises()


    def get_dicts(self):
        return self.prix, self.remises


    def _lire_prix(self,):
        """ Lecture du fichier contenant les produits.
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
        """ Lecture du fichier contenant les remises.
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

if __name__=="__main__":
    catalog = Catalogue(prix_file="test_data/prix.csv", remises_file="test_data/remises.csv")
    catalog_prix, catalog_remises = catalog.get_dicts()
    print(catalog_prix)
    print(catalog_remises)
