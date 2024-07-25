import customtkinter as ctk

from pathlib import Path
from PIL import Image

from GUI.alerts.config import windowsconfig



class FrameQuadro():
    
    def __init__(self, objeto) -> None:
        self.objeto_main = objeto
        self.run()
    
    
    def run(self):
        # self.areaImagem()
        self.areaTexto()
        
        
    def areaImagem(self):
        imagem = Image.open(windowsconfig.ICONS[self.objeto_main.status])
        self.campo_imagem = ctk.CTkLabel(self.objeto_main.master,text='', image=ctk.CTkImage(dark_image=imagem, light_image=imagem, size=(50,50)))
        self.campo_imagem.place(relx=0.05, rely=0.1)
    

    def areaTexto(self):
        texto = self.objeto_main.message
        self.campo_mensagem = ctk.CTkLabel(self.objeto_main.master, text=texto, wraplength=400, justify='left')
        self.campo_mensagem.place(relx=0.3, rely=0.1)
        
