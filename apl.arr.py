import numpy as np 
import random


a = np.random.randint(18,33, size =(5,7))

a[4][3]=0
a[4][4]=0
a[4][5]=0
a[4][6]=0

lu = a[[0,], :]
ma = a[[1,], :]
mi = a[[2,], :]
ju = a[[3,], :]
vi = a[[4,], :]
s = a[: ,[0]]





print("Primera Semana",lu)
print("Segunda Semana",ma)
print("Tercera Semana",mi)
print("Cuarta Semana ",ju)
print("Quinta Semana ",vi)

u=0
d=0
t=0
c=0
q=0

for i in range(5): 

    for j in range(7): 

        if(i==0): 

            u += a[i][j] 

        if(i==1): 

            d += a[i][j] 

        elif(i==2): 

            t += a[i][j] 
        if(i==3): 

            c += a[i][j]  

        elif(i==4): 

            q += a[i][j] 


promu= u/7
promd= d/7
promt= t/7
promc = c/7
promq= q/7

print("")
print("Promedio semana uno: "+str(promu)+"\n", 

    "Promedio semana dos: "+str(promd)+"\n", 

    "Promedio semana tres: "+str(promt)+"\n", 

    "Promedio semana cuatro: "+str(promc)+"\n",

    "promedio semana cinco: "+str(promq))














