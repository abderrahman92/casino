# coding: utf-8
# Clément, Adrien, Emmanuel, Abderaman
# BDD always data
# https://www.alwaysdata.com/fr/
# https://python.doctor/page-python-encodage-encode-decode-unicode-ascii-codec-character-accents-probleme-string-utf8

from random import randint

choice = 0 # Choix pour naviguer dans le menu
name = "" # Nom du joueur
money = 10 # Argent du joueur
mise = 0 # Ce qu'il mise à chaque partie
propal = 0 # Les propositions du joueur pour deviner le nombre de Python
coup = 0 # Nombre de coups réalisé par le joueur
game_start = False # Variable déterminant si le jeu est lancé
level = 1 # Niveau de la partie

#  #  #
#  Affiche le menu
#  #  #

def print_menu():
  print("""*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n
                                  Bienvenue au jeu du Juste Prix !\n
                                            (1) Règles
                                            (2) Jouer
                                            (3) Statistiques
                                            (4) Quitter\n
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n
Python : Que choisis-tu ?
  """)
  
#  #  #
#  Affiche les règles
#  #  #

def print_rules():
  print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n")
  print("                                            RÈGLES\n")
  print("  Hello " + name + ", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")
  print("""  Je vous expliquerai le principe du jeu :\n
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
                               Si vous avez compris vous pouvez :\n
                                 - retourner au menu en tapant 0
                                      - jouer en tapant 2
                               - voir les statistiques en tapant 3
                                     - quitter en tapant 4\n
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n
Python : Que choisis-tu ?
  """)

#  #  #
#  Affiche l'entete pour une nouvelle partie
#  #  #

def print_new_game():
  print("""*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n
                                      - NOUVELLE PARTIE -\n
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n
  """)

#  #  #
#  Gestion des mises
#  #  #

def mise_fn():
  global mise
  global money
  
  try:
    if (level > 1) or (level == 1 and game_start == True):
      mise = int(input("Python : Le jeu va commencer, entrez votre mise :\n\n"))
      print("")
    else:
      mise = int(input())
      print("")

    if (mise <= money and mise <= 10 and mise > 0):
      money -= mise
    elif (mise > money):
      mise = int(input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et " + str(money) + " € :\n\n"))
      print("")
    else:
      mise = int(input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :\n\n"))
      print("")
  except:
    while (mise > money or mise > 10 or mise < 0):
      mise = int(input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :\n\n"))
      print("")

#  #  #
#  Gestion des propositions
#  #  #

def propal_fn(max, python_nb):
  global propal
  global coup

  try:
    propal = int(input())
    print("")

    coup += 1

    if (propal < python_nb):
      print("Votre nombre est trop petit\n")
    elif (propal > python_nb):
      print("Votre nombre est trop grand\n")
    else:
      print("Bravo vous avez trouvé !\n")
      return True

    if (coup == max):
      return False
    
  except:
    propal = int(input())
    print("")

    coup += 1

    if (propal < python_nb):
      print("Votre nombre est trop petit\n")
    elif (propal > python_nb):
      print("Votre nombre est trop grand\n")
    else:
      print("Bravo vous avez trouvé !\n")
      return True

    if (coup == max):
      return False

#  #  #
#  Calculer des gains
#  #  #

def calc_win(nbr_coup, max_coup):
  global money
  global mise

  if (nbr_coup == 1):
    money += round(mise * 2, 2)
    return round(mise * 2, 2)
  elif (nbr_coup == 2):
    money += round(mise, 2)
    return round(mise, 2)
  elif (nbr_coup == 3 and level == 1):
    money += round(mise / 2, 2)
    return round(mise / 2, 2)
  elif (nbr_coup >= 3 and nbr_coup <= max_coup and level > 1):
    for i in range(1, max_coup - 1):
      if (i + 2 == nbr_coup):
        money += round(mise * ((max_coup - i) / max_coup), 2)
        return round(mise * ((max_coup - i) / max_coup), 2)
  else:
    money -= round(mise, 2)
    return round(money, 2)

#  #  #
#  Gestion de la fin d'une partie
#  #  #

def result_game(result, python_nb, nbr_coup_max):
  global choice
  global level
  global coup
  global game_start
  
  if (result == True):
    level += 1
    print("Python : Bingo " + name + ", vous avez gagné en " + str(coup) + " coup(s) et vous avez remporté " + str(calc_win(coup, nbr_coup_max)) + " €.\n")
    print("Python : Vous avez actuellement : " + str(money) + "€!\n")
  else:
    print("Python : Vous avez perdu ! Mon nombre est " + str(python_nb) + "!\n")

  response = input("Souhaitez-vous continuer la partie ? (O/N)\n\n")
  print("")

  if (response == "O"):
    coup = 0
    level_game(level)
  elif (response == "N"):
    game_start = False
    coup = 0
    print("Python : Aurevoir ! Vous finissez la partie avec " + str(money) + " €.\n\n")
    pass
  else:
    input("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie ? (O/N)\n\n")
    print("")

#  #  #
#  Gestion des niveaux
#  #  #

def level_game(nbr_level):
  python_nb = randint(1, nbr_level * 10)
  nbr_coup_max = nbr_level + (nbr_level + 1)

  mise_fn()
  
  print("Python : Vous êtes au niveau " + str(nbr_level) + ". Je viens de penser à un nombre entre 1 et " + str(nbr_level * 10) + " (" + str(python_nb) + "). Devinez lequel.\n")

  if (nbr_level == 1):
    print("Python : Attention vous avez droit à " + str(nbr_coup_max) + " essais !\n")

  if (nbr_level > 1):
    print("Python : Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et " + str(nbr_level * 10) + " et vous avez le droit à " + str(nbr_level + (nbr_level + 1)) + " essais !\n")

  while (coup <= nbr_coup_max):
    if (coup == nbr_coup_max - 1):
      print("Il vous reste une chance !\n")
      
    res = propal_fn(nbr_coup_max, python_nb)

    if (res == True or coup == nbr_coup_max):
      result_game(res, python_nb, nbr_coup_max)
      break

#  #  #
#  Gestion du jeu
#  #  #

def game():
  global coup
  global game_start
  global choice
  global level

  game_start = True
  
  if (coup == 0 and game_start == True):
    print_new_game()

  level_game(level)
  choice = 0

#  #  #
#  Gestion du joueur
#  #  #

while True:
  try:
    name = str(input("Je suis Python. Quel est votre pseudo ?\n\n"))
    print("")

    if (name == ""):
      print("Je n'ai pas bien compris désolé")
      break

    break
  except:
    break

#  #  #
#  Gestion du menu
#  #  #

while True:
  if (choice == 0):
    print_menu()
    try:
      choice = int(input())
      print("")

      while (choice == 0 or choice < 0 or choice > 4):
        choice = int(input("Ce que vous avez saisi n'est pas valide, veuillez saisir 1, 2, 3 ou 4\n\n"))
        print("")
    except:
      while (choice == 0 or choice < 0 or choice > 4):
        choice = int(input("Ce que vous avez saisi n'est pas valide, veuillez saisir 1, 2, 3 ou 4\n\n"))
        print("")

  if (choice == 1):
    print_rules()
    try:
      choice = int(input())
      print("")

      while (choice == 1 or choice < 0 or choice > 4):
        choice = int(input("Ce que vous avez saisi n'est pas valide, veuillez saisir 0, 2, 3 ou 4\n\n"))
        print("")
    except:
      while (choice == 1 or choice < 0 or choice > 4):
        choice = int(input("Ce que vous avez saisi n'est pas valide, veuillez saisir 0, 2, 3 ou 4\n\n"))
        print("")

  if (choice == 2):
    game()

  if (choice == 3):
    print("LES STATS ICI")
    break

  if (choice == 4):
    print("A la prochaine " + name + "!")
    break