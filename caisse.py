
class caisse(object):
    
    def __init__(self, catalogue_file="catalogue.csv"):
        self.catalogue_file=catalogue_file
        self.catalogue = {}
        self._lire_catalogue()


    def _lire_catalogue(self,):
        """ Lecture du fichier contenant les produits.
            Le fichier est donné en argument lors de la 
            creation de l'instance de la classe. 
        """

        print('\n* Lecture du catalogue...')
        with open(self.catalogue_file, 'r') as cat_file:
            i = 0
            produit = ''
            prix = ''
            for row in cat_file.readlines():
                try:
                    produit, prix = row.rstrip().split(',')
                    # Pour faciliter la comparaison
                    produit = produit.lower()

                    if produit in self.catalogue: 
                        # Produit dupliqué
                        raise KeyError
                    else:
                        # Introduire au catalogue
                        self.catalogue[produit] = float(prix)

                except ValueError:
                    print("[ERREUR CATALOGUE]: Erreure de format dans: {}".format(row))
                except KeyError:
                    print("[ERREUR CATALOGUE]: Produit '{}' dupliqué!".format(produit))


            i += 1



if __name__ == "__main__":
	c = caisse()
