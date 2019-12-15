import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Ouverture des fichiers sources

X = open("bilan_X.txt","r")
Y = open("bilan_secteurs.txt","r")
resultat = open("resultat.txt","w")

#Initialisation des variables

i=0

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

#Traitement

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
		
Z = sc.fit_transform(sources2)
#print(Z)

n = sources2.shape[0]
p = sources2.shape[1]

coord = acp.fit_transform(Z)

eigval = (acp.singular_values_**2)/n

print(acp.explained_variance_ratio_)

del (secteurs2[0])
del (sources2[0])

#Affichage

plt.plot(numpy.arange(1,

#Fermeture des fichiers

X.close()
Y.close()
resultat.close()