import sys

from caisse import Caisse
from ticket import Ticket
from catalogue import Catalogue


# ------ CATALOGUE --------
def test_catalogue():
    catalog = Catalogue(prix_file="test_data/prix.csv", remises_file="test_data/remises.csv")
    catalog_prix, catalog_remises = catalog.get_dicts()

    print("Liste des prix:")
    print(catalog_prix)
    print("Liste des promo:")
    print(catalog_remises)

    print("--- MAJ catalogue ---")
    catalog.maj()


# ------ TICKET --------
def test_ticket():
    print("- Ticket initialisation")
    ticket = Ticket()
    articles = [('a', 2, 2.5, -2, 'Parce que vous le valez bien!'),
                ('b', 3, 1.5, 0, '')]

    print("- Appending articles")
    for a in articles:
        ticket.ajout(a[0], a[1], a[2], a[3], a[4])

    print("- Printing ticket")
    print(ticket)


# ------ CAISSE --------
def test_caisse():
    print("--- Initialisation ---")
    caisse = Caisse()

    print("--- MAJ catalogue ---")
    caisse.maj()

    print("--- Introduction Ticket ---")
    caisse.introduction_ticket()


if __name__=="__main__":
    test = {
            "caisse": test_caisse,
            "ticket": test_ticket,
            "catalogue": test_catalogue
            }

    arg = sys.argv[1].lower()

    if arg not in test:
        print("Usage: python run_tests.py [caisse|ticket|catalogue]")
    else:
        test = test[arg]()


