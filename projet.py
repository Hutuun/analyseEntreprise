

#Ouverture des fichiers sources

X = open("bilan_X.txt","r")
Y = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#

i=0

temp = []
temp2 = []
secteurs = []
sources = []
secteurs2 = []
sources2 = []

for ligne in X:
	temp += [ligne.split()]

for ligne in Y:
	temp2 += [ligne]
	
print (len(temp))
print (len(temp2))

for i in range(0,len(temp)):
	temp3=0 
	for j in temp[i]:
		if j == '-1':
			temp3=1
	if temp3==0:
		secteurs += [temp2[i]]
		sources += [temp[i]]

print (temp[0])
print (sources)

for i in range(0,len(secteurs)):
	temp3=0

#Fermeture des fichiers

X.close()
Y.close()
resultat.close()