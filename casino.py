# -*- coding: utf-8 -*-
#Clément, Adrien, Emmanuel, Abderrahman 

from random import randrange
import database as db

cnx=db.database_connection()

name_user= input("\t- Je suis Python. Quel est votre pseudo ? \n")
dotation=10
solde= dotation #valeur par défault d'un nouveau joueur, faire requete SQL

def affiche_regle():
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n")

    print("                                            RÈGLES\n")

    print("  Hello " + name_user + ", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")

    print("""  Je vous expliquerai le principe du jeu :\n

      Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?

      Att : vous avez le droit à trois essais !

      - Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !

      - Si vous le devinez au 2è coup, vous gagnez exactement votre mise !

      - Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !

      - Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit :\n

        - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu

        - de quitter le jeu\n

      - Dès que vous devinez mon nombre vous avez le droit:\n

        - de quitter le jeu et de partir avec vos gains

        - de continuer le jeu en passant au level supérieur\n

                                  

    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n

    Python : Que choisis-tu ?

    """)


while True :
    regle= input("Bonjour, voulez-vous afficher les règles du jeu ? (O/N)")
    print(regle)
    try:
        if(regle=="O"):
            affiche_regle()
            break
        elif (regle=='N'):
            break
        else :
            print("La valeur saisie n'est pas correct")
    except:
        print("La valeur saisie n'est pas correct")


def ramdom(max):
    nb_python = randrange (1, max, 1)
    print('(ORDI) : ', nb_python) 
    return nb_python

def choix_mise():
    while True:
        try : 
            mise = int(input("\t- Le jeu commence, entrez votre mise : ?\n """))
            if (mise<=solde):
                return mise       
                break
            else : 
                print("\t- Le solde saisi n'est pas valide. Entrer SVP un solde entre 1 et "+str(solde)+" € :  ?\n ")
        except :
          print("\t- Le solde saisi n'est pas valide. Entrer SVP un solde entre 1 et "+str(solde)+" € :  ?\n ")
mise = choix_mise()
nb_python= ramdom(10)


def lev(nombre_max, nbcoups_max, solde, level):
    nb_coup = 0
    while True:
        try:
            nb_user  = int(input("\t- Entrez SVP votre nombre ? \n"))
            if(nb_user <=nombre_max):
                nb_coup += 1

                print("Nombre de coup : "+str(nb_coup))
                if ((nb_coup==nbcoups_max) and (nb_user  != nb_python)):
                    print("\t- Vous avez perdu ! Mon nombre est "+ str(nb_python)+" !\n")
                    solde -= mise
                    print("votre nouveau solde : "+ str(round(solde,2))+" €")
                    db.insert_stats(cnx, name_user, level, nb_coup, mise, 0, -solde)
                    return solde
                    break

                if(nb_coup==(nbcoups_max-1)): print("\t- Il vous reste une chance !\n ")
                if nb_user  > nb_python :
                    print ('Votre nbre est trop grand')
                elif nb_user  < nb_python :
                    print ('Votre nbre est trop petit')

                else :
                        if(level==1):
                            if(nb_coup==1):
                                solde= (solde-mise) + mise*2
                            elif (nb_coup==3):
                                solde = solde- mise/2
                        if(level==2):
                            if(nb_coup==1):
                                 solde= (solde-mise) + mise*2
                            elif(nb_coup==2):
                                  solde= (solde-mise) + mise*(4/5)      
                            elif(nb_coup==3):
                                  solde= (solde-mise) + mise*(3/5)
                            elif(nb_coup==4):
                                  solde= (solde-mise) + mise*(2/5)
                            elif(nb_coup==5):
                                  solde= (solde-mise) + mise*(1/5)
                        if(level==3):
                            if(nb_coup==1):
                                 solde= (solde-mise) + mise*2
                            elif(nb_coup==2):
                                  solde= (solde-mise) + mise*(6/7)
                            elif(nb_coup==3):
                                  solde= (solde-mise) + mise*(5/7)
                            elif(nb_coup==4):
                                  solde= (solde-mise) + mise*(4/7)
                            elif(nb_coup==5):
                                  solde= (solde-mise) + mise*(3/7)
                            elif(nb_coup==6):
                                  solde= (solde-mise) + mise*(2/7)
                            elif(nb_coup==7):
                                  solde= (solde-mise) + mise*(1/7)
                        print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                        print("votre nouveau solde : "+ str(round(solde,2))+" €" )
                        db.insert_stats(cnx, name_user, level, nb_coup, mise, 0, solde)
                        return solde
                        break      
            else :
                print("La valeur saisie n'est pas correct, veuillez saisir un nombre entre 1 et "+str(nombre_max))
        except Exception as err:
            print(err)
            print("La valeur saisie n'est pas correct, veuillez saisir un nombre entre 1 et "+str(nombre_max))  #Lev 1

solde = lev(10,3,solde, 1)  # pour le niv1


#FIN DE PARTIE 
while True:
    try:
        new_game = input("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
        if(new_game=='O'):
            print("- Super ! Vous passez au Level 2.\n") #Si remporte niv 1  Action... appeler fonction LEV 2 
            print("""\t- Les statistiques du level 1 sont les suivantes :
	              - Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et\n\t\t vous avez le droit à 5 essais !\n\t""")
            nb_python=ramdom(20) #lev2
            mise= choix_mise()
            solde = lev(20,5,solde, 2)
            while True:
                try:
                    new_game = input("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
                    if(new_game=='O'):
                        print("	\t- Super ! Vous passez au Level 3.\n") #Si remporte niv 1  Action... appeler fonction LEV 2 
                        print("""\t- Les statistiques du level 2 sont les suivantes : ...
                            \t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 30 et\n\t\t vous avez le droit à 7 essais !\n""")
                        nb_python=ramdom(30) #lev2
                        mise= choix_mise()
                        solde = lev(30,7,solde, 3)
                        print("\t- Au revoir ! Vous finissez la partie avec "+str(round(solde,2))+" €.\n ")
                        # scores = db.scoreboard(cnx)
                        # print("Scores:")
                        # for score in scores:
                        #     print("{} {}€ \n\tgain maximum {}\n\tpourcentage de reussite {:.0f}%\n\tlevel 1:\n\tnb de victoires: {} moyenne de tentatives: {} nb de victoire en un coup: {}\n\tlevel 2:\n\tnb de victoires: {} moyenne de tentatives {}\n\tlevel 3:\n\tnb de victoires: {} moyenne de tentatives {}".format(
                        #     score["user"], score["sum"], score["max_gain"], score["win_percentage"], score["win_level_1"], score["average_tries_level_1"], score["first_try_win"], score["win_level_2"], score["average_tries_level_2"], score["win_level_3"], score["average_tries_level_3"]))
                        break

                    if(new_game=='N'):
                        print("\t- Au revoir ! Vous finissez la partie avec "+str(round(solde,2))+" €.\n ")
                        break
                except:
                      print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")     
            break
             

        if(new_game=='N'):
            print("\t- Au revoir ! Vous finissez la partie avec "+str(round(solde,2))+" €.\n ")
            break
        else:
            print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")    
    except:
        print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")

scores = db.scoreboard(cnx)
print("Scores:")
for score in scores:
    print("{} {}€ \n\tgain maximum {}\n\tpourcentage de reussite {:.0f}%\n\tlevel 1:\n\tnb de victoires: {} moyenne de tentatives: {} nb de victoire en un coup: {}\n\tlevel 2:\n\tnb de victoires: {} moyenne de tentatives {}\n\tlevel 3:\n\tnb de victoires: {} moyenne de tentatives {}".format(
    score["user"], score["sum"], score["max_gain"], score["win_percentage"], score["win_level_1"], score["average_tries_level_1"], score["first_try_win"], score["win_level_2"], score["average_tries_level_2"], score["win_level_3"], score["average_tries_level_3"]))




# except Exception as err:
#         print(err)




	
