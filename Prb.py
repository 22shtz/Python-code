# This is a smple Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#pb 1
#-----------------------------------------------------
def f1(x):
     return x%10

print (f1(23))

#pb2
#-----------------------------------------------------

def f2(a,b,c):
     return 12*a+b+16*c

print(f2(1,2,3))

#pb4
#-----------------------------------------------------
def f4(x):
     if(x%400==0):
         return True
     elif(x%100==0):
         return False
     elif(x%4==0):
         return True
     else:
         return False

print(f4(1200))

#pb5
#-----------------------------------------------------
def f5(x):
     if(x<-3):
         return 2*x+1
     elif(x==3):
         return 0
     else:
         return 3*(x**2)+6*x-5

print(f5(2))

#pb6
#-----------------------------------------------------
def f6(a,b,c):
     return c>=a and c<=b

print(f6(2,17,11))

#pb7
#-----------------------------------------------------
def f7(a,b,c):
     return max(a,b,c), min(max(a,b),max(b,c),max(a,c)), min(a,b,c)

print(f7(2,5,7))

#pb8
#-----------------------------------------------------
def f8(s1,s2):
     return int(s2[1:2])*3600+int(s2[3:4])*60+int(s2[7:8])-int(s1[1:2])*3600+int(s1[3:4])*60+int(s1[7:8])

print(f8('12:30:24','16:14:01'))

#pb9
#-----------------------------------------------------
def f9(x):
     return 2*3.14*x, 3.14*(x**2)

print(f9(5))

#pb10
#-----------------------------------------------------

def f10(a,b):
     if(a>b):
         c=a
         a=b
         b=c
     p=0
     while(a<b):
          if(f4(a)==True):
             p+=366
          else:
             p+=365
          a+=1
     return p

print(f10(2021,2022))