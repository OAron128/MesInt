from random import choices, randint, randrange, random
import copy
import numpy as np
import random


def FlowShopMatrix(n,m,seed):
    np.random.seed(seed)
    return np.random.randint(1,500, size=(n,m))
#öröklődés miatt kell, seed alapján egy fajta randomizált értéket add vissza mátixba


def utemtervRand(n,seed2):
    np.random.seed(seed2)
    s = np.random.choice(range(n),n,replace=False)
    return s
#ugyan az mint a FlowShopMatrix


def CmaxSzamolasa(m,n,mat,s):
    kezdmunka = [[0 for x in range(n)] for y in range(m)]
    befmunka = [[0 for x in range(n)] for y in range(m)]
    cost = [0 for i in range(n)] #érték végigmegy a gépeken

    #print("kezdeti munka: \n",kezdmunka)
    #print("befejezési munka: \n: ",befmunka)
    #print("érték: \n: ",cost)

    for i in range(m): #munkákon megy végig majd
        for j in range(n): #gépeken
            c_max = cost[j]
            #print("C_max értéke most = ",c_max)
            
            if j > 0:
                c_max = max(cost[j-1], cost[j])
                
            cost[j] = c_max + mat[s[j] - 1][i]
            #print(j,". elem értéke = ",cost[j])


            befmunka[i][j] = cost[j]
            #print("befejezési munka: ",befmunka[i][j]) #ez mindig annyi mint a cost j. eleme

            kezdmunka[i][j] = befmunka[i][j] - mat[s[j] - 1][i]
               
            #print("A kezdeti munka kivonással = ",kezdmunka[i][j])
                
            c_max = befmunka[i][j]

    print("\n \n \n")
    print("C max értéke: ",c_max)
    print("Kezdeti érték = \n",kezdmunka)
    print("Befejezési érték = \n",befmunka)
    print("\n \n \n")

    return c_max  
 #   return{
 #       "c_max": c_max,
 #       "Kezdeti értékek ": kezdmunka,
 #       "Befejezési értékek ": befmunka
 #       }

def mutacio(s):
    temp=0
    mutans = copy.deepcopy(s)
    b = random.randint(0,len(mutans)-1)
    a = random.randint(0,len(mutans)-1)
    while a == b:
        b = random.randint(0,len(mutans)-1)
        
    mutans[a],mutans[b]=mutans[b],mutans[a]

    return mutans

def genetic(s,popmeret,genszama,mutszama,m,n,mat):
    populacio =[list(s)]
    for i in range(popmeret - 1):
        populacio.append(mutacio(s))
        
    best_megold = max(populacio, key=lambda ch: CmaxSzamolasa(m,n,mat,ch)) 
    best_c_max = CmaxSzamolasa(m,n,mat,best_megold)

    for j in range(genszama):
        for i in range(mutszama):
            populacio.append(mutacio(populacio[random.randint(0,len(populacio)-1)]))

        populacio = sorted(populacio, key = lambda ch: CmaxSzamolasa(m,n,mat,ch))
        populacio = populacio[:popmeret] #levágjuk a méretét a kívántra

        best_egyed = populacio[0]
        best_egyed_ido = CmaxSzamolasa(m,n,mat,best_egyed)

        if(best_egyed_ido < best_c_max):
            best_c_max = best_egyed_ido
            best_megold = best_egyed

    return best_megold


def main():

    n = 10 #munkák száma
    m = 5 #gépek száma
    seed = 0 #véletlen számgenerátor állapotának beállításához szükséges változó
    seed2=42

    popmeret= 10 #populáció mérete
    genszama = 5 #generáció száma/mennyisége
    mutszama = 2 #mutáció száma/mennyisége
 
    mat = np.array(FlowShopMatrix(n,m,seed))
    print("Szimuláció: ","\n",mat)
    
    s = utemtervRand(n,seed2)
    print("Ez az ütemterv:",s)

    print(CmaxSzamolasa(m,n,mat,s))

    print(mutacio(s))

    print(genetic(s,popmeret,genszama,mutszama,m,n,mat))

if __name__=="__main__":
    main()
