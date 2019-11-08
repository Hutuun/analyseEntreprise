

#Ouverture des fichiers sources

sources = open("bilan_X.txt","r")
secteurs = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

i=0
for ligne in sources:
	print (ligne[0])
	str = ligne
	print str.split()

#Fermeture des fichiers

sources.close()
secteurs.close()
resultat.close()