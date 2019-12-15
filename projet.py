#Import des librairies

import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

#Ouverture des fichiers sources

X = open("bilan_X.txt","r")
Y = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#Initialisation des variables

i=0
dimx = 10
nbEle = 5

temp = []
temp2 = []

secteurs = []
sources = []
secteurs2 = []
sources2 = []

Z = []
coord = []

sc = StandardScaler()
acp = PCA(svd_solver='full')

#Preparation des donnees

for ligne in X:
	temp += [ligne.split()]
	
for i in range(0,len(temp)):
	for j in range(0,len(temp[i])):
		temp[i][j]=float(temp[i][j])

for ligne in Y:
	temp2 += [ligne]

for i in range(0,len(temp)):
	temp3=0 
	for j in temp[i]:
		if j == -1:
			temp3=1
	if temp3==0:
		secteurs += [temp2[i]]
		sources += [temp[i]]

for i in range(0,len(secteurs)):
	temp3=0
	for j in secteurs2:
		if secteurs[i]==j:
			temp3=1
	if temp3==0:
		secteurs2 += [secteurs[i]]
		sources2 += [sources[i]]
		
#Calcul des valeurs propres

Z = sc.fit_transform(sources2)
#print(Z)

n = len(sources2)
p = len(sources2[0])

coord = acp.fit_transform(Z)

eigval = (acp.singular_values_**2)/n

print(acp.explained_variance_ratio_)

#Determination du nombre de facteurs a retenir

bs = 1/numpy.arange(p,0,-1) 
bs = numpy.cumsum(bs) 
bs = bs[::-1]

print(pandas.DataFrame({'Val.Propre':eigval,'Seuils':bs,'Choisi':eigval>bs})) 

#del (secteurs2[0])
#del (sources2[0])

#Affichage

plt.plot(numpy.arange(1,p+1),eigval)
plt.title("Classement en fonction de leur importance des valeurs propres")
plt.ylabel("Valeurs propres")
plt.xlabel("Classement")
plt.savefig("Image/fig1.png")
plt.show()


plt.plot(numpy.arange(1,p+1),numpy.cumsum(acp.explained_variance_ratio_)) 
plt.title("Cumul de la représentativité des valeurs propres") 
plt.ylabel("Somme de la représentativité des valeurs propres") 
plt.xlabel("Nombres de valeurs propres") 
plt.savefig("Image/fig2.png")
plt.show() 


for j in range(int(n/nbEle)):

	#positionnement des individus dans le premier plan 
	fig, axes = plt.subplots(figsize=(12,12)) 
	axes.set_xlim(-dimx,dimx) #même limites en abscisse 
	axes.set_ylim(-dimx,dimx) #et en ordonnée 

	#placement des etiquettes des observations 
	for i in range(nbEle):
		plt.annotate(secteurs2[j*nbEle+i],(coord[j*nbEle+i,0],coord[j*nbEle+i,1]))

	#ajouter les axes 
	plt.plot([-dimx,dimx],[0,0],color='silver',linestyle='-',linewidth=1) 
	plt.plot([0,0],[-dimx,dimx],color='silver',linestyle='-',linewidth=1)

	#affichage 
	name = "Image/Correlation/fig" + str(j) + ".png"
	fig.savefig(name)
	fig.clear()
	#plt.show()
	plt.cla()
	plt.clf()
	plt.close('all')



#Fermeture des fichiers

X.close()
Y.close()
resultat.close()