import customtkinter as ctk

from PIL import Image

from src.GUI.alerts.config import windowsconfig



class UsageFrame():
    
    def __init__(self, objeto) -> None:
        self.objeto_main = objeto
        self.run()
    
    
    def run(self):
        self.imageArea()
        self.textArea()
        
        
    def imageArea(self):
        image = Image.open(windowsconfig.ICONS[self.objeto_main.status])
        self.image_field = ctk.CTkLabel(self.objeto_main.master,text='', 
                                         image=ctk.CTkImage(dark_image=image, light_image=image, size=(50,50)))
        self.image_field.place(relx=0.05, rely=0.1)
    

    def textArea(self):
        text = self.objeto_main.message
        self.message_field = ctk.CTkLabel(self.objeto_main.master, text=text, wraplength=400, justify='left')
        self.message_field.place(relx=0.3, rely=0.1)
        
