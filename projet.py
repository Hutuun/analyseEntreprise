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
C = open("bilan_caracteristiques.txt")
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

caracteristique =[]

Z = []
coord = []

sc = StandardScaler()
acp = PCA(svd_solver='full')

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

#Contribution à l'inertie
di = numpy.sum(Z**2,axis=1) 
print(pandas.DataFrame({'ID':secteurs2,'d_i':di})) 

#Qualité de représentation
cos2 = coord**2 
for j in range(p):     
	cos2[:,j] = cos2[:,j]/di 
 
print(pandas.DataFrame({'id':secteurs2,'COS2_1':cos2[:,0],'COS2_2':cos2[:,1]}))

#Contribution à chaque axes
ctr = coord**2
for j in range(p):
	ctr[:,j] = ctr[:,j]/(n*eigval[j])      
 
print(pandas.DataFrame({'id':secteurs2,'CTR_1':ctr[:,0],'CTR_2':ctr[:,1]})) 

#Représentation des variables
sqrt_eigval = numpy.sqrt(eigval) 

corvar = numpy.zeros((p,p))
 
for k in range(p):     
	corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k]

#print(corvar)

print(pandas.DataFrame({'id':caracteristique,'COR_1':corvar[:,0],'COR_2':corvar[:,1]}))

#Qualité de représentation des variables

cos2var = corvar**2 
print(pandas.DataFrame({'id':caracteristique,'COS2_1':cos2var[:,0],'COS2_2':cos2var[:,1]}))

#Contribution des variables aux axes

ctrvar = cos2var 
 
for k in range(p):     
	ctrvar[:,k] = ctrvar[:,k]/eigval[k] 
 
print(pandas.DataFrame({'id':X.columns,'CTR_1':ctrvar[:,0],'CTR_2':ctrvar[:,1]})) 

#Affichage

#fct.AffichageClassement(p,eigval)

#fct.AffichageCumul(p,acp)

#fct.RepresentationIndividus(n,nbEle,dimx,coord,secteurs2)

#fct.AffichageCercleCorrelation(caracteristique,corvar,p)

#Fermeture des fichiers

X.close()
Y.close()
resultat.close()