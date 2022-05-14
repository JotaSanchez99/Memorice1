import threading,wx

class Ventana(wx.Frame):
    def __init__(self):
        
            
        # Ventana principal: Tiene  un nombre, un estilo por defecto 
        # (no se puede maximizar y cambiar el tamanho
        # Tiene un tamnho de 800x600
        wx.Frame.__init__(self, None, title="Mensajeria", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800,600))
        
        # Un panel donde seran compuestos los widgets
        self.panel = wx.Panel(self)
        
        # Una barra de estado en el fondo de la ventana principal
        self.CreateStatusBar()
        # Se crea un menu pequenho
        filemenu= wx.Menu()
        # Se crea un separador
        filemenu.AppendSeparator()
        # Entrada de menu para salir de la aplicacion
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        # Entrada de menu para mostrar informacion sobre la aplicacion
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # Se enlazan las entradas del menu con acciones representadas por metodos
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Show(True)
        # Se crea una barra de menu donde ira el menu crado
        menuBar = wx.MenuBar()
        # Se adicionan los menus
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        # Se adiciona la barra del menu en la ventana principal
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        # Se crean los controles (widgets) en el panel de la ventana principal
        # StaticBox: un panel con nombre para agrupar controles 
        # StaticText: Labels o etiquetas
        # TextCtrl: Entradas de texto para ingresa la informacion
        # masked: enmascarar la entrada de texto
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, "Ingresar Mensaje", pos=(10,0),size=(790, 100))
        self.lbl2 = wx.StaticText(self.box1, -1, 'Mensaje:', pos =(180,25))
        self.txt1 = wx.TextCtrl(self.box1, style=wx.TE_LEFT, size=(250, 25), name = "txt1", pos = (245,23))
        self.btn1 = wx.Button(self.box1, label = "Guardar", size=(100, 25), pos=(505,23)) 
 
               
        self.box2 = wx.StaticBox(self.panel, wx.ID_ANY, "Mensaje Copiado", pos=(10,200),size=(790, 100))
        self.lbl2 = wx.StaticText(self.box2, -1, 'Mensaje:', pos =(180,25))
        self.txt2 = wx.TextCtrl(self.box2, style=wx.TE_LEFT, size=(250, 25), name = "txt2", pos = (245,23))
        
        
        
        

        # Adicionar los controles en un BoxSizer (layout) para organizar de forma vertical
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.box1, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.box2, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.panel.SetSizer(self.sizer) 
     
     
        # Eventos de Botones (Guardar)
        self.btn1.Bind(wx.EVT_BUTTON, self.OnSaveMessage)
        
        
        # Metodo para guardar mensaje
    def OnSaveMessage(self,e):
         
        # Se debe verificar que el DNI tampoco este vacio (Implementar)
        if self.txt2.GetLineLength(0) == 0: 
            dls= wx.MessageDialog( self, self.txt1.GetValue(), "Dialogo", wx.OK)
            dls.ShowModal() 
            dls.Destroy()
            wx.CallAfter(self.llamada, self.txt1.GetValue())
            
    def llamada(self,e):
        self.txt2.SetValue(e)
        
    
    # Metodo que especifica el comportamiento del about del menu    
    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "Algo", "Sobre el mensaje", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Metodo para salir del aplicativo
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    