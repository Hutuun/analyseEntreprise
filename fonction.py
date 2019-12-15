#Import des librairies

import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas
import fonction as fct

def AffichageClassement(p,eigval):
	plt.plot(numpy.arange(1,p+1),eigval)
	plt.title("Classement en fonction de leur importance des valeurs propres")
	plt.ylabel("Valeurs propres")
	plt.xlabel("Classement")
	plt.savefig("Image/fig1.png")
	plt.show()

def AffichageCumul(p,acp):
	plt.plot(numpy.arange(1,p+1),numpy.cumsum(acp.explained_variance_ratio_)) 
	plt.title("Cumul de la représentativité des valeurs propres") 
	plt.ylabel("Somme de la représentativité des valeurs propres") 
	plt.xlabel("Nombres de valeurs propres") 
	plt.savefig("Image/fig2.png")
	plt.show() 

def RepresentationIndividus(n,nbEle,dimx,coord,secteurs2):
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