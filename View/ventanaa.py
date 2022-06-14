from ast import Lambda
from operator import truediv
from tkinter import*
from tkinter import messagebox
import random

class carta:
    def __init__(self):
        self.valor = 0
        self.posicion=0
        self.oculta= True
        self.imagen= PhotoImage(file="fondo.jph")
        
class Memorice:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.title("Memorice")
        self.ventana.geometry("500x500")
        
        #se guardan los botones de la intefeaz
        self.botones = []
        #para las cartas
        self.carta= []
        #para cuando se de clic sorbre la interfaz 
        #la carta se voltea y esta la guarda para ver si es par
        self.temporal =carta()
        #para guardar la posiicion de la otra carta
        self.a =0
        #para ver si se volteo la primera carta o a segunda
        self.par =0
        #es para que no se puedan hacer otras acciones mientras no se volten las cartas otra ves
        self.listo = True
        #para la imagen de fondo que tendria 
        
        self.fondo = PhotoImage(file="fondo.jpg")####es fondo de la carta
        
        self.crearTablero()
        self.revolver()
        self.ventana.mainloop()
        
    def crearTablero(self):
        
        i=0
        contador=0
        # para probar que pasa pero seria comun con un for
        while i<4:
            j=0
            while j<4:
                boton = Button(self.ventana,command=lambda a = contador:self.revisar(a),
                               height=70,width=70,imagen=self.fondo)
                ##parara dar una posicon al boton osea a imagen
                boton.place(x=(j+1)*70, y=(i+1)*70) # multiploca y asi ordena de forma burda explicado
                self.botones.append(boton)
                j+=1
                contador+=1
            i=1    
        
    
    def revolver(self):
        i = 1
        # de esta forma se crean las cartas para luego ordenar pero estas de una en una }
        #es decir en orden 
        while (i<8):
            carta1 =carta()
            carta1.valor = i
            carta1.foto = PhotoImage(file=str(i)+".jpg")
            carta2 =carta()
            carta2.valor= i
            carta2.foto = PhotoImage(file=str(i)+".jpg")
            self.carta.append(carta1)
            self.carta.append(carta2)
            i+=1
        cartaTemporal =[]
        while len(self.carta)>0:
            posicion = random.randrange(0,len(self.carta))
            cartaTemporal.append(self.carta.pop(posicion))
        self.carta = cartaTemporal
            
        
        
    def revisar(self,a):
       
        # listo es para que el usuario no pueda intentar voltear las cartas o aga algo 
       
        if self.listo == True and self.carta[a].oculta == True:
            self.botones[a].config(image=self.carta[a].imagen)
            if self.par ==0:
                self.temporal = self.carta[a]
                self.carta[a].oculta= False
                self.temporal.posicion =a
                self.par = 1
                
            elif self.par ==1:
                self.par = 0
                if self.temporal.valor == self.carta[a].valor:
                    self.carta[a].oculta = False
                    
                    bandera = True # revisara si  termino el juego 
                    
                    for elemento in self.carta:
                        if elemento.oculta == True:
                            bandera = False
                            break # para romper ciclo evita probleamas 
                    if bandera == True:
                        messagebox.showinfo("Para ganar siempre se pierde algo","Pero Felicidades ganaste ")
                
                #ahora si el juego no ha terminado
                else:
                    self.a =a
                    self.listo = False
                    #tapar es el metetodo  para tapar al cartas para que bno 
                    # no sean visibles
                    self.ventana.after(500,self.tapar) 
                    
    def tapar(self):
        self.carta[self.temporal.posicion].oculta =True
        self.botones[self.temporal.posicion].config(imagen=self.fondo)
        self.botones[self.a].config(imagen=self.fondo)
        self.listo = True
                    
                    
                        
                        
             
obj = Memorice()