import random
# On définit la liste des pays
listepays=("Allemagne","Angleterre","Autriche","Bulgarie","Chypre","Croatie","Danemark","Espagne","France")
# On choisit aléatoirement 1 pays
pays=random.choice(listepays)
print(pays)
print("Deviner le nom du pays")
print("La première lettre est : ", pays[0])
print("Le nombre de lettre est de : ",len(pays))
mots=""
essais=0


while mots!=pays and essais<5:
 mots = input ("Saissisez le nom qui vous semble juste:")
 essais=essais+1

 if mots==pays:
     print ("Vous avez gagné")
 if essais >=5 :
    print ("Vous avez perdu !")
