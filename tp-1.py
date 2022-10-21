
def CalculTotal():
    """
          --pour la fonction CalculTotal()--
           Pobjectif: calcul le prix total des produits commandés
           Méthode: En multipliant la quantité de chaque produit commandé par le prix unitaire de ce produit puis
                                           l'additionner aux prix des produits précédent
           Besoin: on a bejoin du prix unitaire de chaque produit (pu) et la quantité de chaque produit commander (qtcom)
           Connus: néant
           Entrés: pu et qtcom
           Sortie: le prix total des produits commandés (total)
           Resultat: néant
           Hypothése: néant
    """
    command=int (input("donner le nombre de produit commander:\t"))
    total = 0

    for i in range(command):

        pu = int(input("donner le prix unitaire du produit:\t"))
        qtcom = int(input("donner la quantité commander du produit:\t"))

        total = total + pu * qtcom

    return total



#   -- Pour la fonction CalculPort() --


def CalculPort():
    """
      Objectif: calcul le port des produits
       Méthode:  en mutlipliant  le prix total des produits par 0,01 (1% du prix total des produit) si le total > 10000
                  sinon le port sera égal à 0
       Besoin: de ce fait on a besoin du prix total des produits calculer dans la fonction précédant
       Connus: le prix total des produits (total)
       Entrer: néant
       Sortie: port
       Hypothése: si total est superieur à 10000
                  si total est inferieur à 10000
     """
    if total < 10000:

        port = 0

    else:

        port = total*0.01

    return port

#   -- Pour la fonction CalculRemise() ---



def CalculRemise():
    """
      Objectif : calculer la remise
       Méthode :  En se servant du prix total des produits commandés pour faire la comparaison
       Besoin :   on a besoin du prix total des produits commandés
       Connus : total
       Entrées : néant
       Sorties: remise
       Resultats: néant
       Hypothéses: si total est comprise entre 5000 et 20000
                    ou si total est superieur à 20000
    """

    if (total > 5000) and (total <= 20000) :

        remise = total*0.02

    elif total > 20000:

        remise = total*0.03

    return remise



#   -- Pour la fonction AffichePrix --


def AffichePrix():

    """  Objectif: afficher le prix à payer pour tous les produit commander, la remise et le port
      Méthode:  calculer le prix puis le calcul l'afficher par print()
      Besoin : total , remise, port
      Connus: total , remise, port
      Entrées : néant
      Sorties: néant
      Resultats: print()
      Hypothése : néant
   """

    print(f"\nle prix à payer est : {total+CalculPort()-CalculRemise()}\nla remise -> {CalculRemise()} \nle port -> {CalculPort()} ")

if __name__ == '__main__':

    total = CalculTotal()

    AffichePrix()

