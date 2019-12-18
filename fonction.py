#Import des librairies

import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas
import fonction as fct

def FonctionPrincipale(sources2,secteurs2,caracteristique,nbEle,dimx,adresse):
	sc = StandardScaler()
	acp = PCA(svd_solver='full')

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
 
	print(pandas.DataFrame({'id':caracteristique,'CTR_1':ctrvar[:,0],'CTR_2':ctrvar[:,1]})) 

	#Affichage

	fct.AffichageClassement(p,eigval,adresse)

	fct.AffichageCumul(p,acp,adresse)

	fct.RepresentationIndividus(n,nbEle,dimx,coord,secteurs2,adresse)

	fct.AffichageCercleCorrelation(caracteristique,corvar,p,adresse)

def AffichageClassement(p,eigval,adresse):
	plt.plot(numpy.arange(1,p+1),eigval)
	plt.title("Classement en fonction de leur importance des valeurs propres")
	plt.ylabel("Valeurs propres")
	plt.xlabel("Classement")
	plt.savefig(adresse+"fig1.png")
	plt.show()

def AffichageCumul(p,acp,adresse):
	plt.plot(numpy.arange(1,p+1),numpy.cumsum(acp.explained_variance_ratio_)) 
	plt.title("Cumul de la représentativité des valeurs propres") 
	plt.ylabel("Somme de la représentativité des valeurs propres") 
	plt.xlabel("Nombres de valeurs propres") 
	plt.savefig(adresse+"fig2.png")
	plt.show() 

def RepresentationIndividus(n,nbEle,dimx,coord,secteurs2,adresse):
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
		name = adresse+"Correlation/fig" + str(j) + ".png"
		fig.savefig(name)
		fig.clear()
		#plt.show()
		plt.cla()
		plt.clf()
		plt.close('all')
		
def AffichageCercleCorrelation(caracteristique,corvar,p,adresse):
	fig, axes = plt.subplots(figsize=(8,8)) 
	axes.set_xlim(-1,1) 
	axes.set_ylim(-1,1) 
 
	#affichage des étiquettes (noms des variables) 
	for j in range(p):     
		plt.annotate(caracteristique[j],(corvar[j,0],corvar[j,1]))      

	#ajouter les axes 
	plt.plot([-1,1],[0,0],color='silver',linestyle='-',linewidth=1) 
	plt.plot([0,0],[-1,1],color='silver',linestyle='-',linewidth=1) 
	
	#ajouter un cercle 
	cercle = plt.Circle((0,0),1,color='blue',fill=False) 
	axes.add_artist(cercle) 
 
	#affichage 
	plt.savefig(adresse+"CercleCorrelation.png")
	plt.show() 