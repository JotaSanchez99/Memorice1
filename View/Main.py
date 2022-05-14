import wx
from View.Ventana import Ventana
        
if __name__ == "__main__":
    app = wx.App()
    Ventana().Show()
    app.MainLoop()
    