# -*- coding: utf-8 -*-
#Clément, Adrien, Emmanuelle 
#BDD always data
# https://www.alwaysdata.com/fr/
# https://python.doctor/page-python-encodage-encode-decode-unicode-ascii-codec-character-accents-probleme-string-utf8

import database as db

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

cnx = db.database_connection()

while True :
    regle= input("Bonjour, voulez-vous afficher les règles du jeu ? (O/N)")
    print(regle)
    try:
        if(regle=="O"):
            #print("Voici les règles :")
            affiche_regle()
            break
        elif (regle=='N'):
            print("Pas de regle")
            break
        else :
            print("La valeur saisie n'est pas correct")
    except:
        print("La valeur saisie n'est pas correct")
scores = db.scoreboard(cnx)
print("Scores:")
for score in scores:
    print("{} {}$ {} {}".format(score[0], score[1], score[2], score[3]))
 

pseudo= input("\t- Je suis Python. Quel est votre pseudo ? \n")
montant= 10 #valeur par défault d'un nouveau joueur 
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

nb_ordi = randrange (1, 11, 1)
print('(ORDI)  Mon choix est = ', nb_ordi)
nb_coup = 0

#CHOIX DE LA MISE 
while True:
    try : 
        gains_total = db.winnings(cnx, pseudo)
        if gains_total == None:
            gains_total = 10
        mise = int(input("\t- Le jeu commence, entrez votre mise : ? Vous avez {}$\n """.format(gains_total)))
        if (mise<=gains_total):       
            break
    except :
          print("\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et "+str(montant)+" € :  ?\n ")

#CHOIX DU NOMBRE
while True:
    try:
        nb_choisi = int(input("\t- Entrez SVP votre nombre ? \n"))
        if(nb_choisi<=10): #LEV 1
            nb_coup += 1

            print("Nombre de coup : "+str(nb_coup))
            if (nb_coup==4):
                print("\t- Vous avez perdu ! Mon nombre est "+ str(nb_ordi)+" !\n")
                db.insert_stats(cnx, pseudo, 1, nb_coup, -mise, nb_choisi)
                break

            if(nb_coup==2): print("\t- Il vous reste une chance !\n ")
            if nb_choisi > nb_ordi :
                print ('Votre nbre est trop grand')
            elif nb_choisi < nb_ordi :
                print ('Votre nbre est trop petit')
            else :
                print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                db.insert_stats(cnx, pseudo, 1, nb_coup, mise * [2, 1, 1/2][nb_coup - 1], nb_choisi)                  
                break 
    except Exception as err:
        print(err)
        print("La valeur saisie n'est pas correct, veuillez saisir un nombre entre 1 et 10")  #Lev 1

scores = db.scoreboard(cnx)
                
print("Scores:")
for score in scores:
    print("{} {}$ {} {}".format(score[0], score[1], score[2], score[3]))
 

cnx.close()
