

#Ouverture des fichiers sources

sources = open("bilan_X.txt","r")
secteurs = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

i=0

temp = []

for ligne in sources:
	temp += [ligne.split()]
	
	
print(temp[1])

#Fermeture des fichiers

sources.close()
secteurs.close()
resultat.close()