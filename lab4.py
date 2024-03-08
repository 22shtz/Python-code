
import functools as f
def f1(lista,i=0):
                if(i==len(lista)):
                    return 0
                elif(lista[i]%2==0):
                    print(lista[i])
                return f1(lista,i+1)
f1([0,12,4,5,7,8])

def f2(lista,i=0):
                if(i==len(lista)):
                    return 0
                elif(len(lista[i])<3):
                     print(lista[i])
                return f2(lista,i+1)


f2(["abc","ac","abcd","ab"])
def f3(lista):
                lista.sort()
                print(lista)
                lista.reverse()
                print(lista)

f3([2,14,2.3,5])

def f4(lista):
            lista.sort(key=lambda x: x%10)
            print(lista)
f4([12,31,43,50])

def f5(lista):
            rezultat=f.reduce(lambda x,y: x*y,lista )
            print(rezultat)

f5([2,3,4,5])

def f6(lista):
            rezultat=list(map(lambda x: pow(x,3),lista))
            print(rezultat)

f6([2,3,5,7])

def prim(x,d=2):
              if(x<=d):
                  return 1
              elif(x%d==0):
                  return 0
              else:
                  return prim(x,d+1)
def f7(lista):
            rezultat=list(filter(lambda x: prim(x)==1,lista))
            print(rezultat)

f7([2,3,7,14,13,17,20])

def p2f1a(n,lista=[]):
                    if(n==0):
                        print(lista)
                        return 0
                    if(n%10%2==0):
                        lista.insert(0,n%10)
                    return p2f1a(int(n/10),lista)


p2f1a(1248767)
def par(x):
        if(x%2==0):
            return True
        else:
            return False


def p2f1b(n, lista=[]):
    if (n == 0):
        print(lista)
        return 0
    if (par(n%10)==True):
        lista.insert(0, n % 10)
    return p2f1a(int(n / 10), lista)

p2f1b(1248767)

def p2f1c(lista,n=0,i=0):
                        if(i==len(lista)):
                            print(int(n/10))
                            return 0
                        if(par(lista[i])==True):
                            return p2f1c(lista,(n+lista[i])*10,i+1)
                        else:
                            return p2f1c(lista,n,i+1)


p2f1c([2,4,6,2,8])

def p2f1c(lista,rezultat=[],p=0):
                        rezultat=list(filter(lambda x: x%2==0, lista))
                        p=f.reduce(lambda a,b: a*10+b,rezultat)
                        print(p)

p2f1c([2,4,9,8])

def nth(lista,n):
                return lista[n-1]

print(nth([2,4,56,7,8,9,12,3],5))
def firstin(lista,n,i=0,rez=[]):
                        if(i==n):
                            print(rez)
                            return 0
                        else:
                            rez.insert(i,lista[i])
                            return firstin(lista,n,i+1,rez)

firstin([2,5,6,7,8,9,23,456,6767,2,3],5)

def ff(x):
        if((x+3)%2==0):
            return True
        return False

def countif(lista,ff,rez=[]):
                            rez=list(filter(ff,lista))
                            return len(rez)

print(countif([1,3,5,6,2,4],ff))


def sumif(lista, ff, rez=[],p=0):
                                 rez = list(filter(ff, lista))
                                 p=f.reduce(lambda a,b: a+b,rez)
                                 return p


print(sumif([1, 3, 5, 6, 2, 4], ff))
print("ok")
def partition(lista,l=[],l2=[]):
                                l=list(filter(lambda x: x>5,lista))
                                l2=list(filter(lambda x: x<5,lista))
                                return l,l2
print(partition([2,3,4,5,7,8,9]))

def elimina_duplicatele(lista,i=0):
                                        if(i==len(lista)-1):
                                            return lista
                                        if(lista[i]==lista[i+1]):
                                            lista.pop(i)
                                        return elimina_duplicatele(lista,i+1)
print(elimina_duplicatele([2,4,7,7,8,9,9,2]))