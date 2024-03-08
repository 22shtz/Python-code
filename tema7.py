#pb8
def adaugare_muchie_orientat(graf, muchie):
    if(muchie==[]):
        return graf
    else:
        if (muchie[0][0] in graf):
            graf[muchie[0][0]].add(muchie[0][1])
        else:
            graf[muchie[0][0]]={muchie[0][1]}
        if (not muchie[0][1] in graf):
            graf[muchie[0][1]] = set()
        return adaugare_muchie_orientat(graf,muchie[1:])

print(adaugare_muchie_orientat({1:{2,3,4}, 2:{1,3}, 3:{1,4}, 4:{1,3}},[(2,4), (3,2)]))

def adaugare_muchie_neorientat(graf, muchie):
    if(muchie==[]):
        return graf
    else:
        if (muchie[0][0] in graf):
            graf[muchie[0][0]].add(muchie[0][1])
            graf[muchie[0][1]].add(muchie[0][0])

        else:
            graf[muchie[0][0]]={muchie[0][1]}
            graf[muchie[0][1]]={muchie[0][0]}
        if (not muchie[0][1] in graf):
            graf[muchie[0][1]] = set()
        return adaugare_muchie_neorientat(graf,muchie[1:])

print(adaugare_muchie_neorientat({1:{2,3,4}, 2:{1,3}, 3:{1,4}, 4:{1,3}},[(2,4), (3,2)]))

#pb9
def stergere_muchie_orientat(graf, muchie):
    if(muchie==[]):
        return graf
    else:
        if (muchie[0][0] in graf):
            graf[muchie[0][0]].discard(muchie[0][1])
        return stergere_muchie_orientat(graf,muchie[1:])

print(stergere_muchie_orientat({1:{2,3,4}, 2:{1,3}, 3:{1,4}, 4:{1,3}} ,[(2,1), (3,1)]))

def stergere_muchie_neorientat(graf, muchie):
    if(muchie==[]):
        return graf
    else:
        if (muchie[0][0] in graf):
            graf[muchie[0][0]].discard(muchie[0][1])
        if(muchie[0][1] in graf):
            graf[muchie[0][1]].discard(muchie[0][0])
        return stergere_muchie_neorientat(graf,muchie[1:])

print(stergere_muchie_neorientat({1:{2,3,4}, 2:{1,3}, 3:{1,4}, 4:{1,3}} ,[(2,1), (3,1)]))

