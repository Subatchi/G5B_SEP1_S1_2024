import math
import cmath
import numpy as np

Lista_datos_Lineas= [("6-7",0.099,0.156,125*100*math.pi*10**(-9))]; # (linea,r,x,b)

for i in Lista_datos_Lineas:
    L=5
    Linea=i[0].split("-")
    Linea_a=int(Linea[0])-1
    Linea_b=int(Linea[1])-1
    z = complex(i[1],i[2])
    y = complex(0,i[3])
    Z_modelo=z*L
    Y_Serie=1/Z_modelo
    Y_Shunt=y*L/2
    Y_Shunt=Y_Shunt.imag*1j
    print("Z=",Z_modelo,"\nY=",Y_Shunt )

