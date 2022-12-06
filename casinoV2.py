# -*- coding: utf-8 -*-
#Clément, Adrien, Emmanuelle 
#BDD always data
# https://www.alwaysdata.com/fr/
# https://python.doctor/page-python-encodage-encode-decode-unicode-ascii-codec-character-accents-probleme-string-utf8

# 2 vérification et affichage du message d'erreur 
# modifier la mise
#Faire une variable lev qui détermine le nombre d'essaie et le nombre maximum
#supprimer les breaks inutiles des fonctions
#SI LE MONTANT EST NULL NE PAS POUVOIR CONTINUER 

from random import randrange

def affiche_regle():
    print(""" 
	*  *  *  *  *  *  *  *  *  *  * PROJET : REALISER UN JEU DE CASINO *  *  *  *  *  *  *  *  *\n
	Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).
	En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
	Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),
	level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è 
	level, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà, 
	vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent.
	Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. 
	En absence de validation de la décision, le jeu est terminé.
	Python fournit enfin les statistiques du jeu (voir ci-dessous).
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

pseudo= input("\t- Je suis Python. Quel est votre pseudo ? \n")
montant= 10 #valeur par défault d'un nouveau joueur, faire requete SQL
print("\t- Hello "+pseudo+", vous avez "+ str(montant)+" €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n")
print("""\t- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n
\t- Att : vous avez le droit à trois essais !\n
	\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
	\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
	\t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
	\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et
	\tvous avez le droit : 
	\t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
	\t\t- de quitter le jeu.\n
	\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n """)

def ramdom(max):
    nb_ordi = randrange (1, max, 1)
    print('(ORDI)  Mon choix est = ', nb_ordi) 
    return nb_ordi
    
# nb_coup = 0

def choix_mise():
    while True:
        try : 
            mise = int(input("\t- Le jeu commence, entrez votre mise : ?\n """))
            if (mise<=montant):
                return mise       
                break
            else : 
                print("\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et "+str(montant)+" € :  ?\n ")
        except :
          print("\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et "+str(montant)+" € :  ?\n ")
mise = choix_mise()
# print("La mise en sortie de la fonction : "+str(mise))
nb_ordi= ramdom(10)


def lev(nombre_max, nbcoups_max, montant, level): #refléchir pour l'insertion de la bd, voir les tables 
    nb_coup = 0
    while True:
        try:
            nb_choisi = int(input("\t- Entrez SVP votre nombre ? \n"))
            if(nb_choisi<=nombre_max):
                nb_coup += 1

                print("Nombre de coup : "+str(nb_coup))
                if ((nb_coup==nbcoups_max) and (nb_choisi != nb_ordi)):
                    print("\t- Vous avez perdu ! Mon nombre est "+ str(nb_ordi)+" !\n")
                    montant -= mise
                    print("votre nouveau montant : "+ str(montant))
                    return montant
                    break

                if(nb_coup==(nbcoups_max-1)): print("\t- Il vous reste une chance !\n ")
                if nb_choisi > nb_ordi :
                    print ('Votre nbre est trop grand')
                elif nb_choisi < nb_ordi :
                    print ('Votre nbre est trop petit')


                else :

                        if(level==1):
                            if(nb_coup==1):
                                montant= (montant-mise) + mise*2
                            elif (nb_coup==3):
                                montant = montant- mise/2
                        if(level==2):
                            if(nb_coup==1):
                                 montant= (montant-mise) + mise*2
                            elif(nb_coup==2):
                                  montant= (montant-mise) + mise*(4/5)
                            elif(nb_coup==3):
                                  montant= (montant-mise) + mise*(3/5)
                            elif(nb_coup==4):
                                  montant= (montant-mise) + mise*(2/5)
                            elif(nb_coup==5):
                                  montant= (montant-mise) + mise*(1/5)
                        if(level==3):
                            if(nb_coup==1):
                                 montant= (montant-mise) + mise*2
                            elif(nb_coup==2):
                                  montant= (montant-mise) + mise*(6/7)
                            elif(nb_coup==3):
                                  montant= (montant-mise) + mise*(5/7)
                            elif(nb_coup==4):
                                  montant= (montant-mise) + mise*(4/7)
                            elif(nb_coup==5):
                                  montant= (montant-mise) + mise*(3/7)
                            elif(nb_coup==6):
                                  montant= (montant-mise) + mise*(2/7)
                            elif(nb_coup==7):
                                  montant= (montant-mise) + mise*(1/7)
                        print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                        print("votre nouveau montant : "+ str(montant))
                        return montant
                        break      
            else :
                print("La valeur saisie n'est pas correct, veuillez saisir un nombre entre 1 et "+str(nombre_max))
        except Exception as err:
            print(err)
            print("La valeur saisie n'est pas correct, veuillez saisir un nombre entre 1 et "+str(nombre_max))  #Lev 1

montant = lev(10,3,montant, 1)  # pour le niv1      lev(nombre_max, nbcoups_max)
print("MONTANT APRES LE LEV1 : "+str(montant))


#FIN DE PARTIE 
while True:
    try:
        new_game = input("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
        if(new_game=='O'):
            print("	\t- Super ! Vous passez au Level 2.\n") #Si remporte niv 1  Action... appeler fonction LEV 2 
            print("""\t- Les statistiques du level 1 sont les suivantes : ...
	              \t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et\n\t\t vous avez le droit à 5 essais !\n""")
            nb_ordi=ramdom(20) #lev2
            mise= choix_mise()
            montant = lev(20,5,montant, 2)
            print("le montant au Level 2 : "+str(montant))
            while True:
                try:
                    new_game = input("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
                    if(new_game=='O'):
                        print("	\t- Super ! Vous passez au Level 3.\n") #Si remporte niv 1  Action... appeler fonction LEV 2 
                        print("""\t- Les statistiques du level 2 sont les suivantes : ...
                            \t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 30 et\n\t\t vous avez le droit à 7 essais !\n""")
                        nb_ordi=ramdom(30) #lev2
                        mise= choix_mise()
                        montant = lev(30,7,montant, 3)
                        print("le montant au Level 3 : "+str(montant))
                        break
                except:
                      print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")
             

        if(new_game=='N'):
            print("\t- Au revoir ! Vous finissez la partie avec "+str(montant)+" €.\n ")
            break
        else:
            print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")    
    except:
        print("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n")




#LVL2 : 3COUPS *2 1 1/2
#LVL2 : 5COUPS 4/5 3/5 2/5 



# except Exception as err:
#         print(err)



	
