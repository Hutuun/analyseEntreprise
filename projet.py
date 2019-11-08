

#Ouverture des fichiers sources

sources = open("bilan_X.txt","r")
secteurs = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

i=0

temp = []
temp2 = []
secteurs = []
sources = []

for ligne in sources:
	temp += [ligne.split()]

for ligne in secteurs:
	temp2 += [ligne]
	
print (len(temp))
print (len(temp2))

for i in range(0,len(temp)):
	temp3=true 
	for j in temp[i]:
		if j == -1:
			temp3=false
	if temp3:
		secteurs += temp2[i]
		sources += temp[i]

#Fermeture des fichiers

sources.close()
secteurs.close()
resultat.close()