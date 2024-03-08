
# Scrieți o funcție care ia o lista de mulțimi (de exemplu, de șiruri), și returnează reuniunea
# (variantă: intersectia) mulțimilor.
#Input: [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]; Output: reuniune: {1, 2, 3, 4, 5, 6, 7}; intersectie: {3}
#reuniune
def f5(lista, multime=set()):
        if(len(lista)==0):
            return multime
        else:
             multime=multime | lista[0]
             return f5(lista[1:],multime)

print(f5([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))

#intersectie
def f5_(lista, multime=set(),ok=0):
    if(ok==0):
        multime=multime | lista[0]
        ok=1
        return f5_(lista[1:],multime,ok)
    elif (len(lista) == 0):
        return multime
    else:
        multime = multime & lista[0]
        return f5_(lista[1:], multime,ok)


print(f5_([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))
#grafuri
#1. Scrieți o funcție care primește ca parametru un graf și afișează sub forma nod1 - nod2 toate:
#a) arcele sale, considerând că graful este orientat
#b) muchiile sale, considerând că graful este neorientat. (Aici veți tipări fiecare muchie o singură dată,
# spre exemplu dacă există o muchie între nodurile 1 și 2, veți afișa doar 1-2, nu și 2-1).
#Exemplu: Pentru graful reprezentat prin dicționarul {1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]} se va afișa:
print("AICI------")
import functools

def afisare_muchii(graf, muchii = set()):
    def functie(acc,elem):
        cheie, valoare = elem
        def f_multime(acc2,elem2):
            muchii.add((cheie,elem2))
        functools.reduce(f_multime, valoare, 0)
    functools.reduce(functie, graf.items(), 0)
    return muchii

print(afisare_muchii({1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}))
#adaugare muchii
print("adaugare muchii")
graf = {
   "a" : {"b","c"},
   "b" : {"a", "d"},
   "c" : {"a", "d"},
   "d" : {"e"},
   "e" : {"d"}
}

def adaugare_muchie_orientat(graf, muchie):
    if (muchie[0] in graf):
        graf[muchie[0]].add(muchie[1])
    else:
        graf[muchie[0]]=set(muchie[1])
    if (muchie[1] not in graf):
        graf[muchie[1]] = set()
    return graf
print(adaugare_muchie_orientat(graf,("a","d")))
#pb
#Pentru graful reprezentat prin dicționarul {1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
#și numerele 1 si 4 funcția returnează False.
#Pentru același graf, dar numerele 4 și 2, funcția returnează True,
#iar graful va fi acum {1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,2,3]}
def verif(graf,a,b):
        if(b not in graf[a]):
            return True
        else:
            return False
print(verif({1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]},4,2))
