import random

miniscule = "abcdefghijklmnopqrstuvwxyz"
majiscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre = "1234567890"
symbole = "?!@#$%&_-|\\"

taille = int(input("Entrer la taille de votre mot de passe [8 - 32]: "))

formatt = miniscule + majiscule + symbole + chiffre

while taille !=0:
    if taille < 8:
        print("Taille trop petite")
    elif taille > 32:
        print("taille trop grande")

    else:
        motDePasse = "".join(random.sample(formatt, taille)) 
        stock = input("Voulez-vous stocker ce mot de passe ? [oui/non]")
        if stock == "oui" or stock == "o" or stock == "O" or stock == "OUI":
            with open("FilePWD.txt", 'w+') as fiche:
                fiche.write(motDePasse)
        else:
            print("Mot de passe genere--> ", motDePasse)
    break
