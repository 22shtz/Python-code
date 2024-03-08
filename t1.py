import functools
def functie(d1,d2,d3=dict()):
        def f(acc,elem):
                cheie=elem
                if(cheie in d2):
                    d3[cheie]=d1[cheie]+d2[cheie]
        functools.reduce(f,d1,0)
        return d3
print(functie({'a':1,'b':2,'c':3,'d':4,'e':5},{'a':1,'d':2,'f':3,'g':4,'e':5}))
a = {1, 2, 3}
b = {4, 5, 6}
print(a.update(b))