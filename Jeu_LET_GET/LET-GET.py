import random
import time

def teste(d):
    """

               Pobjectif: afficher
               Méthode: en utilisant les bare et points pour afficher le nombre de tentative
               Besoin: on a bejoin du nombre de tentative restant
               Connus: nombre de tentative restant
               Entrés: néant
               Sortie: néant
               Resultat: print()
               Hypothése: si i egale 0 ou 1 ou 2 ou 3 ou 4
        """

    print("      +---+")
    for i in range(5):
        if i==0:
            print("\t  |   |")
        if i==1:
            if d <= 5: print("\t  o   |")
            else: print("\t      |")


        if i == 2:
            if d == 4: print("\t /    |")
            elif d == 3: print("\t /|   |")
            elif d <= 2: print("\t /|\  |")
            else: print(f"\t      |")

        if i == 3:
            if d == 1: print("\t /    |")
            if d== 0: print("\t / \  |")
            else:print(f"\t      |")
        if i == 4:
            print(f"\t      |")

    print("  ===========\n")

def etape1():
    """

               Pobjectif: choisir un mot dans le dictionnaire de mot
               Méthode: En se servant du fonction random()
               Besoin: on a bejoin du niveau de jeu , de la taille du mot
               Connus: néant
               Entrés: niveau
               Sortie: le mot choisi aléatoirement (motchoisit) et le mot avec lequelle elle doit correspondre
               Resultat: si niveau = 1 , 2 ou 3
               Hypothése: print()
        """


    print("Bienvenu dans le jeu LET-GET.")
    print("######################################")
    print("Vous avez 3 point_erreur.")
    print("######################################")
    print("Vous avez 6 tentatives.")
    print("######################################")
    teste(6)
    niveau=''
    while (niveau != '1') and (niveau != '2') and (niveau != '3'):

        niveau = input("Choisi un niveau de 1 à 3: \t")

        if (niveau != '1') and (niveau != '2') and (niveau != '3'):

            print("-Entrer un nombre!")
    print("######################################")
    print(f"Vous avez choisi le niveau {niveau}")
    print("Chargement des données.....")
    if niveau == '1':
        taille = random.randint(2, 4)

    elif niveau == '2':
        taille = random.randint(5, 7)
    elif niveau == '3':
        taille = random.randint(8, 25)

    motchoisit=""
    motTrouve = '-'


    while (len(motTrouve) < taille):

      motTrouve += '-'

    while len(motchoisit) != taille:
        with open("fichiers/mots.txt", "r") as file:
            data = file.read()
            words = data.split()
            word_pos = random.randint(0, len(words) - 1)
            #print("Position:", word_pos)
            motchoisit = words[word_pos]


    print("8964 mots chargés")
    print(f"Je vous propose un mot de {taille} lettres. De quel mot s'agit-il ?")
    print("######################################")
    print(motTrouve)
    return [motTrouve, motchoisit]


def occu(mot, lettre):
    """

               Pobjectif: trouver le nombre d'occurence d'un lettre saisi dans un mot et ca dernier position dans ce mot
               Méthode: En utilisant la fonction find()
               Besoin: on a bejoin du lettre à chercher( lettre) et la où chercher (mot)
               Connus: lettre et mot
               Entrés: néant
               Sortie: long et last
               Resultat: néant
               Hypothése: trouve != (-1)
        """

    i = 0
    liste = []
    while i < len(mot):
        trouve = mot.find(lettre, i, len(mot))
        if trouve != (-1):

            liste.append(trouve)
            i = trouve + 1
        else:
            i += 1

    long = len(liste)
    last = liste[long - 1]
    return [long, last]


def etape2():
    """

               Pobjectif: trouver le mot choisi aléatoirement
               Méthode: en se servante du nombre de tentative restant et du nombre d'avertissement
               Besoin: on a bejoin de: nbTentative, point_erreur, motTrouve, motchoisit
               Connus: nbTentative, point_erreur, motTrouv, motchoisit
               Entrés: lettre
               Sortie: nbTentative et score
               Resultat: print()
               Hypothése: if elif
        """


    score = 0
    nbTentaive = 6

    point_erreur = 3

    resultat = etape1()

    motTrouve = resultat[0]

    motchoisit = resultat[1]

    trouve3 = motTrouve.find('-', 0, len(motTrouve))
    longueurMot = len(motchoisit)
    start = time.perf_counter()
    end = time.perf_counter()

    voyelle = 'aeiouy'
    i = 0


    while ((nbTentaive > 0) and (trouve3 != (-1)) and (end - start <= 300)):
        lettre= str(input("Saisir une lettre: \t"))
        trouve1 = motTrouve.find(lettre, 0, len(motTrouve))
        trouve2 = voyelle.find(lettre, 0, len(voyelle))


        trouve= motchoisit.find(lettre,0,len(motchoisit))

        if (lettre.isalpha() == False) or (len(lettre)>1):

            print("Vous ne devez choisir que les lettre l'alphabet.\n")

            if point_erreur > 1:


                point_erreur -= 1

                print(f"il vous reste {point_erreur} avertissement.")
                print("######################################")

            elif point_erreur ==1:
                point_erreur -= 1
                print("Vous avez perdu 1 tentative.\n")
                print("######################################")

                nbTentaive -=1

                print(f"Il vous reste {nbTentaive} tentatives")
                print("######################################")

                teste(nbTentaive)


        elif (trouve != (-1)) and (trouve1 == (-1)):

            b = list(motTrouve)

            b[(trouve)] = lettre

            motTrouve = "".join(b)


            print(motTrouve)
            print("\n Bravo, lettre correct")
            if nbTentaive < 6:
                nbTentaive += 1

        elif (trouve == (-1)) and (trouve1 == (-1) and (trouve2 ==(-1))):
            print("Vous avez saisi une consonne qui n'est dans le mot.\n")
            print("Vous avez perdu une tentative.")
            print("######################################")

            if nbTentaive >= 1:
                nbTentaive -= 1
            print(f"Il vous reste {nbTentaive} tentative.")
            print("######################################\n")
            teste(nbTentaive)

        elif (trouve == (-1)) and (trouve1 == (-1) and (trouve2 !=(-1))):
            print("Vous avez saisi une voyelle qui n'est pas dans le mot.\n")
            print("Vous avez perdu deux tentative.")
            print("######################################")
            if nbTentaive >= 2:
                nbTentaive -= 2
            else: nbTentaive = 0
            print(f"Il vous reste {nbTentaive} tentative.")
            print("######################################\n")
            teste(nbTentaive)

        elif (trouve != (-1)) and (trouve1 != (-1)): # and (trouve == trouve1)):
            nb3 = occu(motchoisit,lettre)
            nb1 = int(nb3[0])
            nb = occu(motTrouve,lettre)
            nb2 = int(nb[0])
            trouve4 =  motchoisit.find(lettre, i, len(motchoisit))

            i= int(nb[1]) + 1

            while i < len(motchoisit):# and (trouve4 != (-1)):

                trouve4 = motchoisit.find(lettre, i, len(motchoisit))

                if trouve4 != (-1):
                    break
                i += 1


            if trouve4 != (-1) and nb2 != nb1:

                b = list(motTrouve)

                b[(trouve4)] = lettre

                motTrouve = "".join(b)


                print(motTrouve)
                print("\n Bravo, lettre correct")
                if nbTentaive < 6:
                    nbTentaive += 1

            elif nb2 == nb1:
                print("Lettre déja trouver.")
                print("######################################")
                if point_erreur > 0:
                    point_erreur -=1
                    print(f"Il vous reste {point_erreur} avertissement.")
                    print("######################################")
                if point_erreur == 0:
                    nbTentaive -= 1
                print(f"Il vous reste {nbTentaive} tentative.")
                print("######################################\n")
                teste(nbTentaive)
        trouve3 = motTrouve.find('-', 0, len(motTrouve))
        end = time.perf_counter()

    if trouve3 == (-1):
            print("Félicitation: vous avez deviné le mot.")
            score = nbTentaive * longueurMot
            print(f"Votre score : {score}")

    elif ((nbTentaive < 1) and (trouve3 != (-1))):
            print("Vous avez perdu.\n")
            teste(nbTentaive)
            print(f"Le mot était: {motchoisit}")

    return [nbTentaive, score]



def etape3():
    """

               Pobjectif: executer jusqu'a l'utilisateur entre 1 ou autre
               Méthode: en utilisant le boucle while
               Besoin: on a besoin de la partie
               Connus: partie
               Entrés: néant
               Sortie: néant
               Resultat: print()
               Hypothése: while execute == '1'
        """

    execute = '1'
    partie = 1
    while execute == '1':
        liste=etape2()

        fichier = open("fichiers/log_game.txt", "a")
        fichier.write(f"\n Partie: {partie}\n Tentative restant: {liste[0]} ;\t Score:{liste[1]} ")
        fichier.close()
        partie += 1
        execute = input("Saisir 1 pour continuer ou autre touche pour quitter:\t")


if __name__ == '__main__':

    etape3()