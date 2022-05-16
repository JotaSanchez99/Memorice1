import random

#se crea el tablero del memorice
tablero=[]

'''tablero de 3x3 '''
for x in range(0,3): 
 tablero.append(["O"] * 3)
 

'''Función para imprimir el tablero'''
def print_tablero(tablero):
	for row in tablero:
		print(" ".join(row))
  
##########  Se ingresan las fichas al tablero es decir se crean

#filas de tablero donde iran las figuras o imagenes.
realtablero = []
fila1=[]
fila2=[]
fila3=[]
fila4=[]
filas=[fila1,fila2,fila3]
## usamos 4 filas por comodidad personal me resulto mas facil asumir que eran un tablero de 4x4 8 pares 

# las figuras o bien las fichas con diferentes formas (ideal usar imagenes)

listImg=[]

#llenado  de las filas con las fichas usando el rango 

for i in range(0,16):
	if(i<4):
		fila1.append(listImg[i])
	elif(i<8 and i>3):
		fila2.append(listImg[i])
	elif(i<12 and i>7):
		fila3.append(listImg[i])
	elif(i>11):
		fila4.append(listImg[i])
  
  # para llenar el  tablero 
  
for i in filas:
    lenadotablero.append(i)