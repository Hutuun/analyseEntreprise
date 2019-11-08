

#Ouverture des fichiers sources

sources = open("bilan_X.txt","r")
secteurs = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

i=0

temp = []
temp2 = []

for ligne in sources:
	temp += [ligne.split()]

for ligne in secteurs:
	temp2 += [ligne]
	
print (len(temp))
print (len(temp2))

for i in range(0,len(temp)):
	for j in temp[i]:
		if j == -1:
			

#Fermeture des fichiers

sources.close()
secteurs.close()
resultat.close()