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
C = open("bilan_caracteristique_abbr.txt")
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
secteurs3 = []
sources3 = []
sources4 = []
sources5 = []

caracteristique =[]
caracteristique2 =[]

Z = []
coord = []

#Preparation des donnees

for ligne in X:
	temp += [ligne.split()]

for ligne in C:
	caracteristique += [ligne]
	
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
		
del (secteurs2[0])
del (sources2[0])

fct.FonctionPrincipale(sources2,secteurs2,caracteristique,nbEle,dimx,"Image/",1)

caracteristique2 +=[caracteristique[2]]
caracteristique2 +=[caracteristique[3]]

for i in range(0,len(sources2)):
	temp = []
	temp +=[sources2[i][2]]
	temp +=[sources2[i][3]]
	sources3+=[temp]

#print(pandas.DataFrame({'Secteur':secteurs2,'Sources':sources3})) 

fct.FonctionPrincipale(sources3,secteurs2,caracteristique2,nbEle,dimx,"Image2/",1)

for i in range(0,len(sources2)):
	temp = []
	temp +=[sources2[i][12]]
	temp +=[sources2[i][23]]
	sources4+=[temp]

#print(pandas.DataFrame({'Secteur':secteurs2,'Sources':sources3})) 

fct.FonctionPrincipale(sources4,secteurs2,caracteristique2,nbEle,dimx,"Image3/",1)

for i in range(0,len(sources2)):
	temp = []
	temp +=[sources2[i][2]]
	temp +=[sources2[i][3]]
	temp +=[sources2[i][11]]
	sources5+=[temp]

#print(pandas.DataFrame({'Secteur':secteurs2,'Sources':sources3})) 

fct.FonctionPrincipale(sources4,secteurs2,caracteristique2,nbEle,dimx,"Image4/",0)

#Fermeture des fichiers

X.close()
Y.close()
resultat.close()