#Import des librairies

import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas
import fonction as fct

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

fct.AffichageClassement(p,eigval)


fct.AffichageCumul(p,acp)


fct.RepresentationIndividus()



di = numpy.sum(Z**2,axis=1) 
print(pandas.DataFrame({'ID':secteurs2,'d_i':di})) 

#Fermeture des fichiers

X.close()
Y.close()
resultat.close()