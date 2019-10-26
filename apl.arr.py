import numpy as np
import random
a = np.random.randint(18,34, size =(6,7))

a[4][3]=0
a[4][4]=0
a[4][5]=0
a[4][6]=0


dias = [["lu ma mi ju vi sa do"]]
lu = a[[0,], :]
ma = a[[1,], :]
mi = a[[2,], :]
ju = a[[3,], :]
vi = a[[4,], :]
s =  a[[4,], :-4]

#posicion de la mayor y menor temperatura por semana
d1 = np.argmax(lu)
d2 = np.argmax(ma)
d3 = np.argmax(mi)
d4 = np.argmax(ju)
d5 = np.argmax(vi)

d6 = np.argmin(lu)
d7 = np.argmin(ma)
d8 = np.argmin(mi)
d9 = np.argmin(ju)
d10= np.argmin(vi)


print("  Dias Semana",dias)
print("Primera Semana",lu)
print("Segunda Semana",ma)
print("Tercera Semana",mi)
print("Cuarta Semana ",ju)
print("Quinta Semana ",vi)

def funcion_diccionario(x):
    dias={0:"lunes",1:"martes",2:"miercoles",3:"jueves",4:"viernes",5:"sabado",6:"domingo",7:"lunes",8:"martes",9:"miercoles",10:"jueves",11:"viernes",12:"sabado",13:"domingo",14:"lunes",15:"martes",16:"miercoles",17:"jueves",18:"viernes",19:"sabado",20:"domingo",21:"lunes",22:"martes",23:"miercoles",24:"jueves",25:"viernes",26:"sabado",27:"domingo",28:"lunes",29:"martes",30:"miercoles",31:"jueves",32:"viernes",33:"sabado",34:"domingo"}
    dia = dias[x]
    
    return dia

d1f = funcion_diccionario(d1)
d2f = funcion_diccionario(d2)
d3f = funcion_diccionario(d3)
d4f = funcion_diccionario(d4)
d5f = funcion_diccionario(d5)
d6f = funcion_diccionario(d6)
d7f = funcion_diccionario(d7)
d8f = funcion_diccionario(d8)
d9f = funcion_diccionario(d9)
d10f = funcion_diccionario(d10)





u=0
d=0
t=0
c=0
q=0

u_max = 0
d_max = 0
t_max = 0
c_max = 0
q_max = 0

dia_s1 = 0
dia_s2 = 0
dia_s3 = 0
dia_s4 = 0
dia_s5 = 0

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

if(promu > promd and promu>promt and promu>promc and promu>promq):
            print("la semana mas calurosa fue la primera semana")
if(promd > promu and promd>promt and promd>promc and promd>promq):
            print("la semana mas calurosa fue la segunda semana")
if(promt > promu and promt>promd and promt>promc and promt>promq):
            print("la semana mas calurosa fue la tercera semana")
if(promc > promu and promc>promt and promc>promd and promc>promq):
            print("la semana mas calurosa fue la cuarta semana")
if(promq > promu and promq>promt and promq>promc and promq>promd):
            print("la semana mas calurosa fue la quinta semana")

 


#mayor temperatura
max_1 = np.max(lu)
max_2 = np.max(ma)
max_3 = np.max(mi)
max_4 = np.max(ju)
max_5 = np.max(vi)
print("")
print("TEMPERATURA MAXIMA DE CADA SEMANA")
print("temperatura mas alta en la primera semana :",max_1,"en el dia",d1f)
print("temperatura mas alta en la segunda semana :",max_2,"en el dia",d2f)
print("temperatura mas alta en la tercera semana :",max_3,"en el dia",d3f)
print("temperatura mas alta en la cuarta semana  :",max_4,"en el dia",d4f)
print("temperatura mas alta en la quinta semana  :",max_5,"en el dia",d5f)

#menor temperatura

min_1 = np.min(lu)
min_2 = np.min(ma)
min_3 = np.min(mi)
min_4 = np.min(ju)
min_5 = np.min(s)
print("")
print("TEMPERATURA MINIMA DE CADA SEMANA")
print("temperatura menor en la primera semana :",min_1,"en el dia",d6f)
print("temperatura menor en la segunda semana :",min_2,"en el dia",d7f)
print("temperatura menor en la tercera semana :",min_3,"en el dia",d8f)
print("temperatura menor en la cuarta semana  :",min_4,"en el dia",d9f)
print("temperatura menor en la quinta semana  :",min_5,"en el dia",d10f)

#MAXIMO Y MINIMO EN EL MES
print("TEMPERATURA MAXIMA Y MINIMA EN EL MES")
tem_mes = np.max(a)
print("")
print("temperatura maxima en el mes :",tem_mes)

a_1 = a[ :-4]

tem_mess= np.min(a_1)
print("")
print("temperatura minima en el mes :",tem_mess)












