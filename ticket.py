

class Ticket():
    # Un ticket d'achat
    def __init__(self,):
        self.articles = []
        self.total = 0

    def __str__(self,):
        # format le ticket pour affichage
        output_str = """\n +++ Votre ticket: +++\n\n"""

        for article in self.articles:
            # prix de l'article x quantité
            prix_qt = article[1]*article[2]
            output_str+="  {}: {} x {}€ = {:.2f}€\n".format(
                    article[0], article[1],
                    article[2], prix_qt)

            remise = article[3]
            justification = article[4]
            if remise != 0:
                output_str+="    PROMO: {}\n".format(justification)
                output_str+="    remise: {:.2f}€\n\n".format(remise)


        output_str+="""\n ++ Total : {:.2f}€ ++ \n\n""".format(self.total)
        
        return output_str
        

    def ajout(self, produit, quantite, prix, remise=0, justification=''):
        # Ajouter Article
        self.articles.append((produit, quantite, prix, remise, justification))
        self.total += quantite*prix + remise


if __name__=="__main__":

    print("- Ticket initialisation")
    ticket = Ticket()
    articles = [('a', 2, 2.5), ('b', 3, 1.5)]

    print("- Appending articles")
    for a in articles:
        ticket.ajout(a[0], a[1], a[2])

    print("- Printing ticket")
    print(ticket)
