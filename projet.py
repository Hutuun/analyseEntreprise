

#Ouverture des fichiers sources

sources = open("bilan_X.txt","r")
secteurs = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

for ligne in sources:
	print ligne

#Fermeture des fichiers

sources.close()
secteurs.close()
resultat.close()