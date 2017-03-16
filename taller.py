suma =3.5+2.0+4+1
print suma
x=10


a=20
b=30
print a*b


cA=50
cO=80
print cA**cO

sum,cad=0,""
for i in range(0,100,2):
 cad=cad+" "+str(i)
print(cad) 




a = 'ndlanldkarbolooinos'
b = len(a)
rsp = 0
for i in range(0,b,1):
    if(a[i]=='a'):
        c = i       
if(a[c]=='a'):
    x = c+1
    if(a[x]=='r'):
        x = x+1
        if(a[x]=='b'):
            x = x+1
            if(a[x]=='o'):
                x = x+1
                if(a[x]=='l'):
                    rsp = 1
if(rsp == 1):
    print('arbol')
else:
    print('no tiene la palabra arbol consecutivamente')









x = int(input("ingrese un numero "))
b = 500
c = 1000
if x < b:
  print ("es menor que 500")
elif x < c:
    print " es mayor que 1000"
