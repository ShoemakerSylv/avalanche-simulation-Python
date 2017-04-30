# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:53:59 2015

@author: Sylvain
"""

from random import*
import numpy as np


#fonction qui créer le relief de la montagne. On par du haut du tableau 
def Relief(l,c):
    T=np.zeros((l,c))
    for k in range(c):
        T[(0,k)]=l/2
    for i in range(1,l):
        for k in range(c):
            test=random()
            if test>=0.5 and T[(i-1,k)]!=0:
                T[(i,k)]=T[(i-1,k)]-1
            else:
                T[(i,k)]=T[(i-1,k)]
    return T


#fait un dégradé de zone à risques
def ZoneRisqueDegrade(T):
    L=np.size(T,0) #nombre de lignes du tableau
    C=np.size(T,1) #nombre de colonnes du tableau
    R=[] #zone à risque principale
    R1=[] #2eme zone à risque
    R2=[] #3eme zone à risque
    #on construit la zone au centre (comme précédemment)
    lon=input('quel est la longueur du rectangle principale ? (dimension sur les colonnes) ')
    lar=input('quel est largeur du rectangle principale ? (dimension sur les lignes) ')
    CoinHautGaucheLigne=input('rentrer la ligne du coin en haut à gauche ')
    CoinHautGaucheColonne=input('rentrer la colonne du coin en haut à gauche ')
    for l in range(CoinHautGaucheLigne,CoinHautGaucheLigne+lar):
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon):
             element=(l,c)
             if l>=0 and c >=0 and l<=L-1 and c<=C-1:
                 R.append(element)
    #on regarde quelle dimension on gagne par rapport à R
    P1=input('combien de lignes il faut ajouter à R pour former R1?')     
    for k in range(P1):
        #on redéfinit le coin en haut à gauche
        CoinHautGaucheLigne-=1
        CoinHautGaucheColonne-=1
        #on construit les éléments situés sur la même ligne (contours haut et bas)
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon+2):
            element1=(CoinHautGaucheLigne,c)
            element2=(CoinHautGaucheLigne+lar+1,c)
            if CoinHautGaucheLigne>=0 and c>=0 and CoinHautGaucheLigne<=L-1 and c<=C-1:
                R1.append(element1)
            if CoinHautGaucheLigne+lar+1>=0 and c>=0 and CoinHautGaucheLigne+lar+1<=L-1 and c<=C-1:
                R1.append(element2)
        #on construit les éléments situés sur la même colonne(contours gauche et droite)
        for l in range(CoinHautGaucheLigne+1,CoinHautGaucheLigne+lar+1):
            element1=(l,CoinHautGaucheColonne)
            element2=(l,CoinHautGaucheColonne+lon+1)
            if l>=0 and CoinHautGaucheColonne>=0 and l<=L-1 and CoinHautGaucheColonne<=C-1:
                R1.append(element1)
            if l>=0 and CoinHautGaucheColonne+lon+1>=0 and l<=L-1 and CoinHautGaucheColonne+lon+1<=C-1:
                R1.append(element2)
        #on redifnit un nouveau rectangle qui a une largeur et longueur qui ont augmenté de 2 
        lar=lar+2
        lon=lon+2
    
    P2=input('combien de lignes il faut ajouter à R1 pour former R2')
    for k in range(P2):
        CoinHautGaucheLigne-=1
        CoinHautGaucheColonne-=1
        #on construit les éléments situés sur la même ligne (contours haut et bas)
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon+2):
            element1=(CoinHautGaucheLigne,c)
            element2=(CoinHautGaucheLigne+lar+1,c)
            if CoinHautGaucheLigne>=0 and c>=0 and CoinHautGaucheLigne<=L-1 and c<=C-1:
                R2.append(element1)
            if CoinHautGaucheLigne+lar+1>=0 and c>=0 and CoinHautGaucheLigne+lar+1<=L-1 and c<=C-1:
                R2.append(element2)
        #on construit les éléments situés sur la même colonne(contours gauche et droite)
        for l in range(CoinHautGaucheLigne+1,CoinHautGaucheLigne+lar+1):#on
            element1=(l,CoinHautGaucheColonne)
            element2=(l,CoinHautGaucheColonne+lon+1)
            if l>=0 and CoinHautGaucheColonne>=0 and l<=L-1 and CoinHautGaucheColonne<=C-1:
                R2.append(element1)
            if l>=0 and CoinHautGaucheColonne+lon+1>=0 and l<=L-1 and CoinHautGaucheColonne+lon+1<=C-1:
                R2.append(element2)
        #on redifnit un nouveau rectangle qui a une largeur et longueur qui ont augmenté de 2 
        lar=lar+2
        lon=lon+2
             
    return R,R1,R2

#fonction identique à la précédente mais où l'on peut saisir diretement les arguments
def ZoneRisqueDegradeParticuliere(T,lon,lar,CoinHautGaucheLigne,CoinHautGaucheColonne,P1,P2):
    L=np.size(T,0) #nombre de lignes du tableau
    C=np.size(T,1) #nombre de colonnes du tableau
    R=[]
    R1=[]
    R2=[]
    for l in range(CoinHautGaucheLigne,CoinHautGaucheLigne+lar):
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon):
             element=(l,c)
             if l>=0 and c >=0 and l<=L-1 and c<=C-1:
                 R.append(element)
    for k in range(P1):
        #on redéfinit le coin en haut à gauche
        CoinHautGaucheLigne-=1
        CoinHautGaucheColonne-=1
        #on construit les éléments situés sur la même ligne (contours haut et bas)
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon+2):
            element1=(CoinHautGaucheLigne,c)
            element2=(CoinHautGaucheLigne+lar+1,c)
            if CoinHautGaucheLigne>=0 and c>=0 and CoinHautGaucheLigne<=L-1 and c<=C-1:
                R1.append(element1)
            if CoinHautGaucheLigne+lar+1>=0 and c>=0 and CoinHautGaucheLigne+lar+1<=L-1 and c<=C-1:
                R1.append(element2)
        #on construit les éléments situés sur la même colonne(contours gauche et droite)
        for l in range(CoinHautGaucheLigne+1,CoinHautGaucheLigne+lar+1):
            element1=(l,CoinHautGaucheColonne)
            element2=(l,CoinHautGaucheColonne+lon+1)
            if l>=0 and CoinHautGaucheColonne>=0 and l<=L-1 and CoinHautGaucheColonne<=C-1:
                R1.append(element1)
            if l>=0 and CoinHautGaucheColonne+lon+1>=0 and l<=L-1 and CoinHautGaucheColonne+lon+1<=C-1:
                R1.append(element2)
        #on redifnit un nouveau rectangle qui a une largeur et longueur qui ont augmenté de 2 
        lar=lar+2
        lon=lon+2
    
    for k in range(P2):
        CoinHautGaucheLigne-=1
        CoinHautGaucheColonne-=1
        #on construit les éléments situés sur la même ligne (contours haut et bas)
        for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon+2):
            element1=(CoinHautGaucheLigne,c)
            element2=(CoinHautGaucheLigne+lar+1,c)
            if CoinHautGaucheLigne>=0 and c>=0 and CoinHautGaucheLigne<=L-1 and c<=C-1:
                R2.append(element1)
            if CoinHautGaucheLigne+lar+1>=0 and c>=0 and CoinHautGaucheLigne+lar+1<=L-1 and c<=C-1:
                R2.append(element2)
        #on construit les éléments situés sur la même colonne(contours gauche et droite)
        for l in range(CoinHautGaucheLigne+1,CoinHautGaucheLigne+lar+1):#on
            element1=(l,CoinHautGaucheColonne)
            element2=(l,CoinHautGaucheColonne+lon+1)
            if l>=0 and CoinHautGaucheColonne>=0 and l<=L-1 and CoinHautGaucheColonne<=C-1:
                R2.append(element1)
            if l>=0 and CoinHautGaucheColonne+lon+1>=0 and l<=L-1 and CoinHautGaucheColonne+lon+1<=C-1:
                R2.append(element2)
        #on redifnit un nouveau rectangle qui a une largeur et longueur qui ont augmenté de 2 
        lar=lar+2
        lon=lon+2
             
    return R,R1,R2




#algorithme qui provoque une chute de neige sur une zone à risque dégradé
def ChuteDeNeigeDegrade(T,R,I):#n I nombre de grains
    ST=np.copy(T) #copie du tableau
    l=np.size(T,0) #nombre de lignes du tableau
    c=np.size(T,1) #nombre de colones du tableau
    p=input('quelle est la probabilité de tomber sur la zone à risque centrale?(R)')
    p1=input('quelle est la probabilité de tomber sur la zone à risque suivante ?(R1)')
    p2=input('quelle est la probabilité de tomber sur la zone à risque suivante ?(R2)')
    if len(R[1])==0: #on test si la zone à risque R1 est vide
        p1=0
    if len(R[2])==0: #on test si la zone à risque R2 est vide
        p2=0
        
    while I>0:     #tant qu'on n'a pas distribué tous les grains
        test=random()
        if test<=p:
            Y=R[0]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        elif test>p and test<=(p+p1):
            Y=R[1]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        elif test>(p+p1) and test<=(p+p1+p2):
            Y=R[2]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        else:
            a=randrange(l)
            b=randrange(c)
            ST[(a,b)]+=1
            I-=1
    return ST

#fonction identique à la précédente mais à laquelle on peut directement
#saisir les arguments
def ChuteDeNeigeDegradeParticuliere(T,R,I,p,p1,p2):
    ST=np.copy(T) #copie du tableau
    l=np.size(T,0) #nombre de lignes du tableau
    c=np.size(T,1) #nombre de colones du tableau
    if len(R[1])==0: #on test si la zone à risque R1 est vide
        p1=0
    if len(R[2])==0: #on test si la zone à risque R2 est vide
        p2=0
        
    while I>0:     #tant qu'on n'a pas distribué tous les grains
        test=random()
        if test<=p:
            Y=R[0]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        elif test>p and test<=(p+p1):
            Y=R[1]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        elif test>(p+p1) and test<=(p+p1+p2):
            Y=R[2]
            u=randrange(len(Y))
            v=Y[u]
            a=v[0]
            b=v[1]
            ST[(a,b,)]+=1
            I-=1
        else:
            a=randrange(l)
            b=randrange(c)
            ST[(a,b)]+=1
            I-=1
    return ST


#fonction qui crée une forêt (rempli un tableau et place un 1 là où il y a une forêt)
def Foret(l,c):
    T=np.zeros((l,c))
    K=input('Quel type de foret ?" K=0 aléatoire, K=1 croix, K=2 rectangulaire' )
    if K==0:
        n=input('nombre arbres ?')
        while n>=0:
            a=randrange(l)
            b=randrange(c)
            if T[(a,b)]!=1:
                T[(a,b)]+=1
            n-=1
    if K==1:
        L=input('quelle est la ligne du centre de la croix?')
        C=input('quelle est la colonne du centre de la croix ?')
        T[(L,C)]==1
        P=input('combien de paliers à rajouter ?')
        H=[(L,C)]
        T[(L,C)]+=1
        u=P #compteur
        while u>0:
            for k in H:
                Y=[]
                if k[0]-1>=0:
                    T[(k[0]-1,k[1])]=1
                    Y.append([k[0]-1,k[1]])
                if k[0]+1<=l-1:
                    T[(k[0]+1,k[1])]=1
                    Y.append([k[0]+1,k[1]])
                if k[1]-1>=0:
                    T[(k[0],k[1]-1)]=1
                    Y.append([k[0],k[1]-1])
                if k[1]+1<=c-1:
                    T[(k[0],k[1]+1)]=1
                    Y.append([k[0],k[1]+1])
                H=H+Y
            u-=1
    if K==2:
        lon=input('quel est la longueur du rectangle ? (dimension sur les colonnes) ')
        lar=input('quel est largeur du rectangle ? (dimension sur les lignes) ')
        CoinHautGaucheLigne=input('rentrer la ligne du coin en haut à gauche ')
        CoinHautGaucheColonne=input('rentrer la colonne du coin en haut à gauche ')
        for l in range(CoinHautGaucheLigne,CoinHautGaucheLigne+lar):
            for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon):
                if T[l,c]!=1:
                    T[l,c]+=1
                    
    return T

#fonction qui crée une forêt (rempli un tableau et place un 1 là où il y a une forêt)
def ForetParticuliere(l,c,K,lon,lar,CoinHautGaucheLigne,CoinHautGaucheColonne):
    T=np.zeros((l,c))
    if K==0:
        n=input('nombre arbres ?')
        while n>=0:
            a=randrange(l)
            b=randrange(c)
            if T[(a,b)]!=1:
                T[(a,b)]+=1
            n-=1
    if K==1:
        L=input('quelle est la ligne du centre de la croix?')
        C=input('quelle est la colonne du centre de la croix ?')
        T[(L,C)]==1
        P=input('combien de paliers à rajouter ?')
        H=[(L,C)]
        T[(L,C)]+=1
        u=P #compteur
        while u>0:
            for k in H:
                Y=[]
                if k[0]-1>=0:
                    T[(k[0]-1,k[1])]=1
                    Y.append([k[0]-1,k[1]])
                if k[0]+1<=l-1:
                    T[(k[0]+1,k[1])]=1
                    Y.append([k[0]+1,k[1]])
                if k[1]-1>=0:
                    T[(k[0],k[1]-1)]=1
                    Y.append([k[0],k[1]-1])
                if k[1]+1<=c-1:
                    T[(k[0],k[1]+1)]=1
                    Y.append([k[0],k[1]+1])
                H=H+Y
            u-=1
    if K==2:
        for l in range(CoinHautGaucheLigne,CoinHautGaucheLigne+lar):
            for c in range(CoinHautGaucheColonne,CoinHautGaucheColonne+lon):
                if T[l,c]!=1:
                    T[l,c]+=1
                    
    return T


#algorithme qui prend un argument un tableau et qui le fait ébouler. Il 
#retourne le nombre d'éboulements, l'état final, et la répartition des 
#éboulements
def AvalancheFinal(m,M,ST,R,TerrainF):#m,M:capacité des cases (forêt, non forêt), R: relief, F:forêt
    
    l=np.size(ST,0) #nombre de lignes du tableau
    c=np.size(ST,1) #nombre de colones du tableau
    K=np.zeros((l,c)) #tableau récapitulant les éboulements
    a=0
    b=0
    k=0 #compteur d'éboulements
    while (a,b)!=(l-1,c-1): #tant qu'on arrive pas en bas à droite du tableau 
        while ST[(a,b)]<m and a!=l-1:# tant qu'il n'y a pas de problème, on avance sur les lignes 
            a=a+1
            print ST,(a,b)
        if ST[(a,b)]>=m:#si il y a un problème
            if TerrainF[(a,b)]==0:#si on dépasse la capacité m et pas de foret
                k=k+1
                if a==0 and b!=0 and b!=c-1:#côté en haut 
                    ST[(0,b-1)]+=1
                    ST[(0,b+1)]+=1
                    if R[(1,b)]==R[(0,b)]: #si la case en dessous est de même hauteur
                        ST[(1,b)]+=1
                    else:
                        ST[(1,b)]+=2 #sinon (elle est plus basse)
                    ST[(0,b)]=ST[(0,b)]-4
                    K[(0,b)]+=1
                elif a==0 and b==0: #coin en haut à gauche
                    ST[(0,1)]+=1
                    if R[(1,0)]==R[(0,0)]: #si la case en dessous est de même hauteur
                        ST[(1,0)]+=1
                    else:               #sinon (elle est plus basse)
                        ST[(1,0)]+=2
                    ST[(0,0)]=ST[(0,0)]-4
                    K[(0,0)]+=1
                elif a==0 and b==c-1: #coin en haut à droite
                    ST[(0,c-2)]+=1
                    if R[(1,c-1)]==R[(0,c-1)]: #si la case en dessous est à la même hauteur
                        ST[(1,c-1)]+=1
                    else:
                        ST[(1,c-1)]+=2 #si la case est plus basse 
                    K[(0,c-1)]+=1
                    ST[(0,c-1)]=ST[(0,c-1)]-4
                elif a!=0 and a!=l-1 and b==0: #côté à gauche
                    if R[(a+1,0)]<=R[(a,0)]: #si la case en dessous est plus basse
                        ST[(a+1,0)]+=2
                    else:               #sinon (elle est à la même hauteur)
                        ST[(a+1,0)]+=1
                    if R[(a,1)]<R[(a,0)]: #si la case à droite est plus basse (sinon on ne fait rien)
                        ST[(a,1)]+=1
                    ST[(a,0)]=ST[(a,0)]-4
                    K[(a,0)]+=1
                elif a==l-1 and b==0: #coin en bas à gauche
                    if R[(l-1,0)]>=R[(l-1,1)]:
                        ST[(l-1,1)]+=1
                    ST[(l-1,0)]=ST[(l-1,0)]-4
                    K[(l-1,0)]+=1
                elif a==l-1 and b!=0 and b!=c-1: #côté en bas
                    if R[(l-1,b)]<R[(l-1,b-1)] and R[(l-1,b)]<R[(l-1,b+1)]:#la case est la plus basse
                        ST[(l-1,b)]=ST[(l-1,b)]-4
                    elif R[(l-1,b)]>=R[(l-1,b-1)] and R[(l-1,b)]<R[(l-1,b+1)]:#une case à côté est plus basse
                        ST[(l-1,b)]=ST[(l-1,b)]-4
                        ST[(l-1,b-1)]+=1
                    elif R[(l-1,b)]>=ST[(l-1,b-1)] and R[(l-1,b)]>=R[(l-1,b+1)]:#les deux cases sont plus basses
                        if R[(l-1,b-1)]>R[(l-1,b+1)]: #on compare les deux cases égales
                            ST[(l-1,b-1)]+=1
                            ST[(l-1,b)]=ST[(l-1,b)]-4
                        elif R[(l-1,b-1)]==R[(l-1,b+1)]:
                            ST[(l-1,b-1)]+=1
                            ST[(l-1,b+1)]+=1
                            ST[(l-1,b)]=ST[(l-1,b)]-4
                        else:
                            ST[(l-1,b+1)]+=1
                            ST[(l-1,b)]=ST[(l-1,b)]-4
                    K[(l-1,b)]+=1
                elif a==l-1 and b==c-1: #coin en bas à droite
                    if R[(l-1,c-1)]>=R[(l-1,c-2)]: #si le coin est plus haut que la case d'à côté
                        ST[(l-1,c-2)]+=1
                    ST[(l-1,c-1)]=ST[(l-1,c-1)]-4
                    K[(l-1,c-1)]+=1
                elif a!=0 and a!=l-1 and b==c-1:#côté à droite  
                    if R[(a+1,c-1)]==R[(a,c-1)]:#si la case en dessous est de la même hauteur
                        ST[(a+1,c-1)]+=1
                    else:             #sinon (elle est plus basse)
                        ST[(a+1,c-1)]+=2
                    if R[(a,c-1)]>=R[(a,c-2)]: #si la case à gauche est plus basse
                        ST[(a,c-2)]+=1
                    ST[(a,c-1)]=ST[(a,c-1)]-4
                    K[(a,c-1)]+=1
                else:                       #on est au milieu
                        ST[(a+1,b)]+=2
                        if R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]>=R[(a,b)]:
                            ST[(a,b)]+=2
                        elif R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]<R[(a,b)]:
                            ST[(a,b+1)]+=1
                            ST[(a,b)]+=1
                        elif R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]<R[(a,b)]:
                            ST[(a,b-1)]+=1
                            ST[(a,b)]+=1
                    
                        ST[(a,b)]=ST[(a,b)]-4
                        K[(a,b)]+=1
                if a>=1 and b>=1: #on revient à la case situé en haut à gauche 
                    a=a-1
                    b=b-1
                else: #si elle n'existe pas, on revient à 0
                    a=0
                    b=0
        
        
            else:
                if ST[(a,b)]>=M:
                    k=k+1
                    if a==0 and b!=0 and b!=c-1:#côté en haut 
                        ST[(0,b-1)]+=1
                        ST[(0,b+1)]+=1
                        if R[(1,b)]==R[(0,b)]: #si la case en dessous est de même hauteur
                            ST[(1,b)]+=1
                        else:
                            ST[(1,b)]+=2 #sinon (elle est plus basse)
                        ST[(0,b)]=ST[(0,b)]-4
                        K[(0,b)]+=1
                    elif a==0 and b==0: #coin en haut à gauche
                        ST[(0,1)]+=1
                        if R[(1,0)]==R[(0,0)]: #si la case en dessous est de même hauteur
                            ST[(1,0)]+=1
                        else:               #sinon (elle est plus basse)
                            ST[(1,0)]+=2
                        ST[(0,0)]=ST[(0,0)]-4
                        K[(0,0)]+=1
                    elif a==0 and b==c-1: #coin en haut à droite
                        ST[(0,c-2)]+=1
                        if R[(1,c-1)]==R[(0,c-1)]: #si la case en dessous est à la même hauteur
                            ST[(1,c-1)]+=1
                        else:
                            ST[(1,c-1)]+=2 #si la case est plus basse 
                        K[(0,c-1)]+=1
                        ST[(0,c-1)]=ST[(0,c-1)]-4
                    elif a!=0 and a!=l-1 and b==0: #côté à gauche
                        if R[(a+1,0)]<=R[(a,0)]: #si la case en dessous est plus basse
                            ST[(a+1,0)]+=2
                        else:               #sinon (elle est à la même hauteur)
                            ST[(a+1,0)]+=1
                        if R[(a,1)]<R[(a,0)]: #si la case à droite est plus basse (sinon on ne fait rien)
                            ST[(a,1)]+=1
                        ST[(a,0)]=ST[(a,0)]-4
                        K[(a,0)]+=1
                    elif a==l-1 and b==0: #coin en bas à gauche
                        if R[(l-1,0)]>=R[(l-1,1)]:
                            ST[(l-1,1)]+=1
                        ST[(l-1,0)]=ST[(l-1,0)]-4
                        K[(l-1,0)]+=1
                    elif a==l-1 and b!=0 and b!=c-1: #côté en bas
                        if R[(l-1,b)]<R[(l-1,b-1)] and R[(l-1,b)]<R[(l-1,b+1)]:#la case est la plus basse
                            ST[(l-1,b)]=ST[(l-1,b)]-4
                        elif R[(l-1,b)]>=R[(l-1,b-1)] and R[(l-1,b)]<R[(l-1,b+1)]:#une case à côté est plus basse
                            ST[(l-1,b)]=ST[(l-1,b)]-4
                            ST[(l-1,b-1)]+=1
                        elif R[(l-1,b)]>=ST[(l-1,b-1)] and R[(l-1,b)]>=R[(l-1,b+1)]:#les deux cases sont plus basses
                            if R[(l-1,b-1)]>R[(l-1,b+1)]: #on compare les deux cases égales
                                ST[(l-1,b-1)]+=1
                                ST[(l-1,b)]=ST[(l-1,b)]-4
                            elif R[(l-1,b-1)]==R[(l-1,b+1)]:
                                ST[(l-1,b-1)]+=1
                                ST[(l-1,b+1)]+=1
                                ST[(l-1,b)]=ST[(l-1,b)]-4
                            else:
                                ST[(l-1,b+1)]+=1
                                ST[(l-1,b)]=ST[(l-1,b)]-4
                        K[(l-1,b)]+=1
                    elif a==l-1 and b==c-1: #coin en bas à droite
                        if R[(l-1,c-1)]>=R[(l-1,c-2)]: #si le coin est plus haut que la case d'à côté
                            ST[(l-1,c-2)]+=1
                        ST[(l-1,c-1)]=ST[(l-1,c-1)]-4
                        K[(l-1,c-1)]+=1
                    elif a!=0 and a!=l-1 and b==c-1:#côté à droite  
                        if R[(a+1,c-1)]==R[(a,c-1)]:#si la case en dessous est de la même hauteur
                            ST[(a+1,c-1)]+=1
                        else:             #sinon (elle est plus basse)
                            ST[(a+1,c-1)]+=2
                        if R[(a,c-1)]>=R[(a,c-2)]: #si la case à gauche est plus basse
                            ST[(a,c-2)]+=1
                        ST[(a,c-1)]=ST[(a,c-1)]-4
                        K[(a,c-1)]+=1
                    else:                       #on est au milieu
                        ST[(a+1,b)]+=2
                        if R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]>=R[(a,b)]:
                            ST[(a,b)]+=2
                        elif R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]<R[(a,b)]:
                            ST[(a,b+1)]+=1
                            ST[(a,b)]+=1
                        elif R[(a,b-1)]>=R[(a,b)] and R[(a,b+1)]<R[(a,b)]:
                            ST[(a,b-1)]+=1
                            ST[(a,b)]+=1
                        else:
                            if R[(a,b+1)]>=R[(a,b-1)]:
                                ST[(a,b-1)]+=1
                                ST[(a,b)]+=1
                            elif R[(a,b+1)]==R[(a,b-1)]:
                                ST[(a,b-1)]+=1
                                ST[(a,b+1)]+=1
                            else:
                                ST[(a,b+1)]+=1
                                ST[(a,b)]+=1
                        
                        ST[(a,b)]=ST[(a,b)]-4
                        K[(a,b)]+=1
                    if a>=1 and b>=1: #on revient à la case situé en haut à gauche 
                        a=a-1
                        b=b-1
                    else: #si elle n'existe pas, on revient à 0
                        a=0
                        b=0
                else:
                    if a!=l-1:
                        a=a+1
                    else:
                        a=0
                        b=b+1
        elif a==l-1 and b!=c-1: # si on est arrivé au bout de la ligne, mais pas au bout des colonnes 
            a=0 #on revient au début de la ligne 
            b=b+1 #on décale d'une colonne 
        print ST , (a,b)
    print 'le nombre déboulements est'
    print k
    print 'le tableau final est'
    print ST
    print 'la répartition des éboulements est'
    return K,k

#permet de simuler une chute de neige en haut d'une montagne de dimension (20,10)
#avec une 250 grains répartis sur une zone de danger, rectangulaire en haut de la montagne
#et prenant en compte une forêt de dimension 3x3 , dont le coin en haut à gauche est palcé en 
# (2,3)
T=np.zeros((20,10))
R=Relief(20,10)
Z=ZoneRisqueDegradeParticuliere(T,10,2,0,0,1,1)
ST=ChuteDeNeigeDegradeParticuliere(T,Z,250,0.7,0.15,0.1)
F=ForetParticuliere(20,10,2,3,3,2,3)
print R,ST,F
Y=input('êtes vous pret à lancer avalanche ? (1==oui, 0==non)')
if Y==1:
    print AvalancheFinal(4,10,ST,R,F)


    
