#JuegoDeMemoria
#Todas las imagenes  estan en la carpeta llamada "Imagenes"


import wx, os, random, time

class MemoryGame(wx.Frame):
   
    def __init__(self):
        wx.Frame.__init__(self, None, title='Memorice')
        self.SetSize((900,700))
        self.Move((50,25))
        self.panel = wx.Panel(self)   
        
        
        #define que tan grande es el juego... puede ser util para hacer opciones de habilidades mas adelante
        self.numPairs = 12
        
     
        #Obtener todas las imagenes en el directorio llamado "Imagenes" y orden aleatorio
        self.imageArray = GetJpgList("./Imagenes")
        random.shuffle(self.imageArray)
        
        #crea una matriz con la cantidad de cartas necesarias y duplica para formar pares iguales        
        self.imagePairs = self.imageArray[0:self.numPairs]
        self.imagePairs = self.imagePairs * 2

        #porque se duplicaron, necesitamos volver a barajar el orden
        random.shuffle(self.imagePairs)
        
        
        #crea una tarjeta en blanco y da el nombre del archivo
        card = wx.Image('card.jpeg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.blankCards =[]
        for i in range(len(self.imagePairs)):
            self.blankCards.append(wx.StaticBitmap(self.panel,wx.ID_ANY, card,name=self.imagePairs[i]))
            
        #vincular clic izquierdo en cada tarjeta que llama a la funcion de verificacion
        for img in self.blankCards:
            img.Bind(wx.EVT_LEFT_DOWN, self.onClick)
            
      
        #Visual 
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        gs = wx.GridSizer(4, 6, 15, 15)
        gs.AddMany(self.blankCards)       
        hbox.Add(gs, proportion=0, flag = wx.LEFT | wx.TOP, border = 10)
        
        #title = wx.StaticText(self.panel, label="Memory Game")
        #hbox.Add(title,proportion=1, flag = wx.LEFT | wx.TOP | wx.RIGHT | wx.EXPAND, border = 10)
        
        self.panel.SetSizer(hbox)
        self.Show()
        
        self.foundMatches= 0 #Hace un seguimiento para ver si has ganado.
        self.clickCount = 0 #realiza un seguimiento del primer o segundo clic.
        self.card1 = '' #punto de espera si es el primer clic
        self.totalTries = 0

    #----------------------------------------------------------------------
    def onClick(self, event):
        self.clickCount += 1
        
        #haga clic en la tarjeta, cambie la imagen en blanco por la imagen por nombre de archivo
        newCard = event.GetEventObject()
        img = wx.Image(newCard.GetName(), wx.BITMAP_TYPE_ANY)
        newCard.SetBitmap(wx.BitmapFromImage(img))        
        
        if self.clickCount == 1:
            self.card1 = newCard #poner en espacio de espera si hace primer clic
            self.card1.Unbind(wx.EVT_LEFT_DOWN)
        
        else:
            #PAREJA ENCONTRADA: Desvincular eventos de clic. Actualizar rastreador de partidos
            self.totalTries += 1
            if (newCard.GetName() == self.card1.GetName()):
                for findItem in self.blankCards:
                    if findItem.GetName() == newCard.GetName():
                        findItem.Unbind(wx.EVT_LEFT_DOWN)
                self.foundMatches += 1
                print(self.foundMatches)
            else:  
                #PAREJA NO ENCONTRADA: espera y vuelve a ocultar ambas cartas.             
                time.sleep(1) #Esto basicamente congela la pantalla, pero aun se capturan los clics.
                blankCard = wx.Image('card.jpeg', wx.BITMAP_TYPE_ANY)
                newCard.SetBitmap(wx.BitmapFromImage(blankCard))
                self.card1.SetBitmap(wx.BitmapFromImage(blankCard))
                self.card1.Bind(wx.EVT_LEFT_DOWN, self.onClick)
            self.clickCount = 0
        
        if self.foundMatches == self.numPairs:  
            print("Total de Intentos = " + str(self.totalTries))
            total = ("Total de intentos = " + str(self.totalTries))
            dls= wx.MessageDialog( self, total, "Ganaste", wx.OK)
            dls.ShowModal() 
            dls.Destroy()

# obtener todos los archivos JPEG en un directorio que se pasa y devolver la matriz de nombres de imagen
def GetJpgList(loc):
    jpgs = [f for f in os.listdir(loc) if f[-4:] == ".jpg"]
    #print "JPGS son:", jpgs
    return [os.path.join(loc, f) for f in jpgs]
      

    
if __name__ == '__main__':
    app = wx.App(False)
    frame = MemoryGame()
    app.MainLoop()
